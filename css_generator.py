# Simple CSS helper for prototype; not heavily used in this demo.
def mk_css(**kwargs):
    lines = []
    for k,v in kwargs.items():
        lines.append(f"{k} {{ {v} }}")
    return '\n'.join(lines)
