# Add this import at the top
from htpyX_debug import debug, Debug

# W-Tech Core
class WVar:
    def __init__(self, value, name=None):
        self.value = value
        self.name = name
        self._declared = False
        
    def __str__(self):
        return f"WVar({self.value})"
    
    def declare(self, vartype="let"):
        if not self.name:
            raise Exception("WVar needs a name to declare!")
        self._declared = True
        return f"{vartype} {self.name} = {self._js_value(self.value)};"
    
    def _js_value(self, val):
        if isinstance(val, bool): return "true" if val else "false"
        elif val is None: return "null"
        elif isinstance(val, (int, float)): return str(val)
        elif isinstance(val, str): return f'"{val}"'
        elif isinstance(val, WVar): return val.name
        elif isinstance(val, list): 
            return "[" + ", ".join(self._js_value(v) for v in val) + "]"
        elif isinstance(val, dict):
            items = [f"{k}: {self._js_value(v)}" for k, v in val.items()]
            return "{" + ", ".join(items) + "}"
        else: return f'"{str(val)}"'

# Global W-Tech registry
_wvars = {}

def w(value, name=None):
    """Create a W-Var (Weird Technologia)"""
    var = WVar(value, name)
    if name:
        _wvars[name] = var
    return var

def declare_all():
    """Declare all W-Vars at once"""
    declarations = []
    for name, var in _wvars.items():
        if not var._declared:
            declarations.append(var.declare())
    return "\n".join(declarations)

def clear_wvars():
    """Clear W-Var registry"""
    _wvars.clear()

# HTML Element System
def element(tag):
    def creator(*kids, **attrs):
        # Handle W-Vars in attributes and content
        processed_attrs = {}
        for k, v in attrs.items():
            clean_key = k.rstrip('_')
            processed_attrs[clean_key] = _unwrap_wvar(v)
        
        # Process children (unwrap W-Vars)
        processed_kids = []
        for kid in kids:
            if isinstance(kid, WVar):
                processed_kids.append(kid.name)  # Use variable name in JS
            else:
                processed_kids.append(str(kid))
        
        attrs_str = " ".join(f'{k}="{v}"' for k, v in processed_attrs.items())
        if attrs_str: attrs_str = " " + attrs_str
            
        kids_str = "".join(processed_kids)
        
        if tag in ["img", "input", "br", "hr", "meta", "link"]:
            return f"<{tag}{attrs_str}>"
        return f"<{tag}{attrs_str}>{kids_str}</{tag}>"
    return creator

def _unwrap_wvar(value):
    """Extract value from WVar or return as-is"""
    if isinstance(value, WVar):
        return value.name  # Use variable name in HTML
    return str(value)

def export_html(root, filename="index.html", extra_js=""):
    """Export with W-Tech declarations"""
    try:
        from pyXjs import get_js
        
        html_content = f"""<!DOCTYPE html>
{str(root)}
<script>
// W-Tech Declarations (Weird! 🚡)
{declare_all()}

// Transpiled JS
{get_js()}

// Additional JS  
{extra_js}
</script>"""
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        debug(f"✅ W-Tech HTML exported to {filename}")
        clear_wvars()  # Reset for next build
        
    except Exception as e:
        Debug.error(f"W-Tech export failed: {str(e)}")