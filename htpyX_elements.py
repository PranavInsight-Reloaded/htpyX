import html, uuid

class Element:
    def __init__(self, tag='div', children=None, id=None, attrs=None):
        self.tag = tag
        self.children = children or []
        self.id = id or f'htpyx-{uuid.uuid4().hex[:8]}'
        self.attrs = attrs or {}
        self.site = None

    def set_attr(self, k, v):
        self.attrs[k]=v
        return self

    def render_attrs(self):
        parts=[]
        for k,v in self.attrs.items():
            parts.append(f'{k}="{html.escape(str(v))}"')
        parts.append(f'data-htpyx-id="{self.id}"')
        return ' '.join(parts)

    def render(self):
        inner = ''.join([c.render() if isinstance(c, Element) else html.escape(str(c)) for c in self.children])
        return f'<{self.tag} {self.render_attrs()}>{inner}</{self.tag}>'

class Label(Element):
    def __init__(self, text, **kwargs):
        super().__init__('span', children=[text], **kwargs)

class Div(Element):
    def __init__(self, children=None, **kwargs):
        super().__init__('div', children=children or [], **kwargs)

class Button(Element):
    def __init__(self, label, **kwargs):
        super().__init__('button', children=[label], **kwargs)
        self.set_attr('class','htpyx-btn')

    def on_click(self, callback):
        # register server-side callback in attached site
        if self.site is None:
            raise RuntimeError('Add button to a Site before registering handlers')
        self.site.register_event(self.id, callback)
        # mark element type for client-side wiring
        self.set_attr('data-htpyx-type','click')
        return self

class Input(Element):
    def __init__(self, placeholder='', **kwargs):
        super().__init__('input', **kwargs)
        self.set_attr('placeholder',placeholder)

class Image(Element):
    def __init__(self, src, alt='', **kwargs):
        super().__init__('img', **kwargs)
        self.set_attr('src',src)
        self.set_attr('alt',alt)

class NavSpacer(Element):
    def __init__(self, children=None, **kwargs):
        super().__init__('div', children=children or [], **kwargs)
        self.set_attr('style','display:flex;gap:10px;align-items:center;')

