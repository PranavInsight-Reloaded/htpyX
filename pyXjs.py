import re

_collected_js = []

class Transpiler:
    def __init__(self, debug=False):
        self.output = []
        self.declared_vars = set()
        self.indent_levels = [0]
        self.in_func = False
        self.debug = debug

    def transpile(self, code: str) -> str:
        self.output = []
        self.declared_vars = set()
        self.indent_levels = [0]
        self.in_func = False

        dom_shortcuts = ("el(", "txt(", "html(", "val(")

        # keep non-empty logical lines
        lines = [line for line in code.split('\n') if line.strip()]
        for raw in lines:
            indent = len(raw) - len(raw.lstrip(' '))
            content = raw.strip()

            # Close blocks according to indentation
            while len(self.indent_levels) > 1 and indent < self.indent_levels[-1]:
                self.indent_levels.pop()
                self.output.append('}')
                self.in_func = False

            # Comments
            if content.startswith('#'):
                self.output.append(f'// {content[1:].strip()}')
                continue

            # Pass DOM shortcuts through unchanged
            if any(content.startswith(x) for x in dom_shortcuts):
                self.output.append(content if content.endswith(";") else content + ";")
                continue

            # Function def
            func_match = re.match(r'def\s+(\w+)\((.*?)\):', content)
            if func_match:
                func_name, params = func_match.groups()
                self.output.append(f'function {func_name}({params}) {{')
                self.indent_levels.append(indent + 4)
                self.in_func = True
                continue

            # for i in range(...)
            for_match = re.match(r'for\s+(\w+)\s+in\s+range\((.*?)\):', content)
            if for_match:
                var, rng = for_match.groups()
                args = [a.strip() for a in rng.split(',') if a.strip()]
                if len(args) == 1:
                    start, stop = "0", args[0]
                else:
                    start, stop = args[0], args[1]
                self.output.append(f'for (let {var} = {start}; {var} < {stop}; {var}++) {{')
                self.indent_levels.append(indent + 4)
                continue

            # while
            while_match = re.match(r'while\s+(.+):', content)
            if while_match:
                cond = self._py_to_js_expr(while_match.group(1))
                self.output.append(f'while ({cond}) {{')
                self.indent_levels.append(indent + 4)
                continue

            # if/elif/else
            if_match = re.match(r'(if|elif)\s+(.+):', content)
            if if_match:
                typ, cond = if_match.groups()
                cond = self._py_to_js_expr(cond)
                if typ == "if":
                    self.output.append(f'if ({cond}) {{')
                else:
                    self.output.append(f'else if ({cond}) {{')
                self.indent_levels.append(indent + 4)
                continue
            if re.match(r'else:', content):
                self.output.append('else {')
                self.indent_levels.append(indent + 4)
                continue

            # try/except
            if content.startswith('try:'):
                self.output.append('try {')
                self.indent_levels.append(indent + 4)
                continue
            if content.startswith('except'):
                self.output.append('catch(e) {')
                self.indent_levels.append(indent + 4)
                continue

            # variable assignment (simple pattern)
            assign_match = re.match(r'(\w+)\s*=\s*(.+)', content)
            if assign_match and not content.startswith('print(') and not content.startswith('return '):
                var, expr = assign_match.groups()
                expr_js = self._py_to_js_expr(expr)
                # declare only at top-level once
                if not self.in_func and var not in self.declared_vars:
                    self.output.append(f'let {var} = {expr_js};')
                    self.declared_vars.add(var)
                else:
                    self.output.append(f'{var} = {expr_js};')
                continue

            # print(...)
            print_match = re.match(r'print\((.+)\)', content)
            if print_match:
                expr = self._py_to_js_expr(print_match.group(1))
                self.output.append(f'console.log({expr});')
                continue

            # return
            if content.startswith('return '):
                expr = self._py_to_js_expr(content[7:])
                self.output.append(f'return {expr};')
                continue

            # pass
            if content == 'pass':
                self.output.append('// pass')
                continue

            # bare expression / call
            self.output.append(self._py_to_js_expr(content) + ';')

        # Close remaining open blocks
        while len(self.indent_levels) > 1:
            self.indent_levels.pop()
            self.output.append('}')
            self.in_func = False

        result = '\n'.join(self.output)
        if self.debug:
            print("---- Transpiled JS ----\n" + result + "\n---- end ----")
        return result

    def _py_to_js_expr(self, expr: str) -> str:
        expr = expr.strip()

        # basic boolean/null replacements
        expr = expr.replace('True', 'true').replace('False', 'false').replace('None', 'null')
        expr = expr.replace(' and ', ' && ').replace(' or ', ' || ')
        expr = expr.replace(' not ', ' !')
        expr = expr.replace(' is not ', ' !== ').replace(' is ', ' === ')

        # list append -> push
        expr = expr.replace('.append(', '.push(')

        # NOTE: Removed automatic { ... } -> ${ ... } conversion.
        # Backtick template literals (e.g. `Counter A: ${counter_a}`) are passed through unchanged.
        # Quoted strings containing { ... } are NOT converted; if you want template substitution,
        # write a backtick string with explicit ${...} in your jsX.

        # += and -= transformations
        expr = re.sub(r'(\w+)\s*\+\s*=\s*(.+)', r'\1 += \2', expr)
        expr = re.sub(r'(\w+)\s*-\s*=\s*(.+)', r'\1 -= \2', expr)

        # simple builtin conversions
        expr = re.sub(r'str\((.+?)\)', r'\1.toString()', expr)
        expr = re.sub(r'int\((.+?)\)', r'parseInt(\1)', expr)
        expr = re.sub(r'len\((.+?)\)', r'\1.length', expr)

        return expr

def spark(var="", jsX="", extra_js="", debug=False):
    js_parts = []

    declared = set()
    # W-Tech global declarations - only once each
    if var.strip():
        js_parts.append('// W-Tech Declarations')
        for line in var.strip().split('\n'):
            line = line.strip()
            if not line:
                continue
            assign_match = re.match(r'^(\w+)\s*=\s*(.+)$', line)
            if assign_match:
                left, right = assign_match.groups()
                if left not in declared:
                    js_parts.append(f'let {left} = {right};')
                    declared.add(left)

    # Transpile pythonic-js block
    if jsX.strip():
        transpiler = Transpiler(debug=debug)
        js_code = transpiler.transpile(jsX)
        js_parts.append('// Transpiled JS')
        js_parts.append(js_code)

    # Extra raw JS
    if extra_js.strip():
        js_parts.append('// Extra custom JS')
        js_parts.append(extra_js)

    _collected_js.append('\n'.join(js_parts))

def get_js():
    return '\n\n'.join(_collected_js)

def reset():
    _collected_js.clear()

# Quick test when run directly
if __name__ == "__main__":
    sample = r'''
def update_results():
    txt("result-a", `Counter A: ${counter_a}`)
    txt("result-b", "Counter B: {counter_b}")  # will remain as-is
    txt("result-arr", `Array: ${test_arr.join(', ')}`)
    txt("result-obj", "Object: {JSON.stringify(test_obj)}")  # remains as-is
'''
    t = Transpiler(debug=True)
    print(t.transpile(sample))