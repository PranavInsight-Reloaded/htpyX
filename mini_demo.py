from core.htpyX_core import Site
from core.htpyX_elements import Div, Button

def build_site():
    site = Site('htpyX Mini Demo')
    site.add_css('.mini{padding:14px;border-radius:10px;background:rgba(255,255,255,0.8);}')
    b = Button('Hello')
    def cb(req, site=site):
        return {'toast':'Hello clicked!'}
    site.add(Div(children=[b], attrs={'class':'mini'}))
    b.on_click(cb)
    return site
