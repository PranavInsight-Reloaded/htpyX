import html
import json
import os
from typing import List, Dict

class Site:
    def __init__(self, title='htpyX Demo'):
        self.title = title
        self.elements = []
        self.event_registry = {}  # id -> callback
        self.state = {}
        self.css_snippets = []
        self.js_snippets = []

    def add(self, el):
        el.site = self
        self.elements.append(el)
        return el

    def register_event(self, el_id, callback):
        self.event_registry[el_id] = callback

    def add_css(self, css):
        self.css_snippets.append(css)

    def add_js(self, js):
        self.js_snippets.append(js)

    def render(self):
        css = "\n".join(self.css_snippets)
        js = "\n".join(self.js_snippets)
        body = "\n".join([el.render() for el in self.elements])
        html_doc = f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>{html.escape(self.title)}</title>
  <style>
:root{
  --bg:#f2f6fb; --card:#ffffff; --text:#0f1724; --glass: rgba(255,255,255,0.6);
}
.dark{{--bg:#0b1220; --card:#0e1724; --text:#e6eef8; --glass: rgba(255,255,255,0.03);}}
body{{margin:0; font-family:Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; background:var(--bg); color:var(--text);}}
.container{{max-width:980px; margin:36px auto; padding:24px;}}
.glass-card{{backdrop-filter: blur(8px); background:var(--glass); border-radius:12px; padding:18px; box-shadow: 0 6px 18px rgba(8,12,20,0.08); border:1px solid rgba(255,255,255,0.06)}}
button.htpyx-btn{{padding:10px 14px; border-radius:8px; border:0; cursor:pointer; font-weight:600;}}
.navbar{{display:flex; align-items:center; justify-content:space-between; gap:12px; padding:12px 18px;}}
.topbar{{background:transparent;}}
{css}
  </style>
</head>
<body>
  <div class="topbar">
    <div class="container">
      <div class="navbar">
        <div><strong>{html.escape(self.title)}</strong></div>
        <div id="nav-controls"></div>
      </div>
    </div>
  </div>

  <main class="container" id="htpyx-root">
    {body}
  </main>

  <script>
// Core client-side event wiring: sends POST /event with {id, action}
function sendEvent(id, action='click', payload={{}}){{
  fetch('/event', {{
    method:'POST',
    headers:{{'Content-Type':'application/json'}},
    body: JSON.stringify({{id, action, payload}})
  }})
  .then(r=>r.json())
  .then(j=>{{
    // call any client-side hooks returned
    if(j && j.update){{
      for(const upd of j.update){{
        const el = document.getElementById(upd.id);
        if(el) el.innerHTML = upd.html;
      }}
    }}
    if(j && j.toast) {{
      console.log('toast:', j.toast)
    }}
  }})
  .catch(e=>console.error('event error', e));
}}

// attach listeners for buttons
document.addEventListener('click', (e)=>{
  const el = e.target.closest('[data-htpyx-id]');
  if(!el) return;
  const id = el.getAttribute('data-htpyx-id');
  const type = el.getAttribute('data-htpyx-type') || 'click';
  if(type === 'click') {{
    sendEvent(id,'click',{{}});
  }}
}});

// theme toggle helper
function htpyx_set_theme(theme){{
  if(theme==='dark') document.documentElement.classList.add('dark');
  else document.documentElement.classList.remove('dark');
}}
// restore saved theme
try{{ const t=localStorage.getItem('htpyx_theme')||'light'; htpyx_set_theme(t); }}catch(e){{}}

{js}
  </script>
</body>
</html>
"""
        return html_doc

