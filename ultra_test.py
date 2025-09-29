# A demo site that showcases navbar, theme toggle, glass card, and a server-backed counter.
from core.htpyX_core import Site
from core.htpyX_elements import Div, Button, Label, NavSpacer

def build_site():
    site = Site('htpyX Ultra Test')

    # add a tiny CSS snippet for demo tweaks
    site.add_css('''
    .counter { font-size:28px; font-weight:700; margin:10px 0; }
    .controls { display:flex; gap:10px; align-items:center; margin-top:8px; }
    ''')

    # header controls (theme toggle)
    def theme_toggle_cb(req, site=site):
        # server receives theme in payload; store and respond no-op
        t = req.get('payload', {}).get('theme', 'light')
        site.state['theme'] = t
        return {{'toast': f'Set theme: '+t}}

    nav_spacer = NavSpacer()
    theme_btn = Button('Toggle Theme')
    # when clicked from client, JS will toggle theme locally and also POST event
    def theme_cb(req, site=site):
        # flip theme on server-side
        cur = site.state.get('theme','light')
        new = 'dark' if cur=='light' else 'light'
        site.state['theme']=new
        return {{'toast':f'theme->'+new}}
    site.add(nav_spacer)
    site.add(theme_btn)
    theme_btn.on_click(theme_cb)

    # main glass card
    counter_label = Label('Counter: ')
    counter_value = Label('0', attrs={{'id':'counter-value'}})
    increment = Button('Increment')
    def inc_cb(req, site=site):
        c = site.state.get('count',0) + 1
        site.state['count']=c
        # instruct client to update DOM
        return {{'update':[{{'id':'counter-value','html':str(c)}}], 'toast': f'Count is {c}'}}
    site.add(Div(children=[Div(children=['\n']), Div(children=['\n'])]))  # spacing
    site.add(Div(children=[
        Div(children=[
            Div(children=[
                Div(children=[
                    Div(children=[counter_label, counter_value], attrs={{'class':'counter'}}),
                    Div(children=[increment], attrs={{'class':'controls'}}),
                ], attrs={{'class':'glass-card'}})
            ])
        ])
    ]))
    increment.on_click(inc_cb)

    # attach a simple script to nav-controls to toggle theme locally
    site.add_js("""(function(){{
        // place a small theme toggle button in nav-area
        const pc = document.getElementById('nav-controls');
        const btn = document.createElement('button');
        btn.innerText='Dark/Light';
        btn.onclick = function(){{
          const cur = document.documentElement.classList.contains('dark')?'dark':'light';
          const next = cur==='dark'?'light':'dark';
          document.documentElement.classList.toggle('dark');
          localStorage.setItem('htpyx_theme', next);
          // also notify server
          sendEvent('{theme_btn_id}','click',{{'theme':next}});
        }};
        pc.appendChild(btn);
    }})();""".replace('{theme_btn_id}', theme_btn.id))

    return site
