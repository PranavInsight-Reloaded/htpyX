# htpyX Developer Guide (mini)

API Highlights:

- `Site()` : root container. `site.add(el)` to register an element.
- Elements: `Button`, `Label`, `Div`, `Image`. Each element has a unique `id`.
- `Button.on_click(callback)` : register a Python callable. When the page posts an event for that button,
  the callable is invoked with the payload `req` and should return a JSON-serializable dict.
- `site.render()` : returns the full HTML document as a string.

Client-side:
- Buttons and elements include `data-htpyx-id` attributes and the client JS POSTs to `/event`.
- The server responds with optional `update` array: `[{id: 'el-id', html: '<b>new</b>'}]` to change innerHTML.

This is a minimal prototype intended for local development and experimentation.
