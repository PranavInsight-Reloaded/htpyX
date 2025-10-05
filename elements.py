from core import element

# Structural
Html = element("html")
Head = element("head") 
Body = element("body")
Div = element("div")
Span = element("span")
Section = element("section")
Article = element("article")
Footer = element("footer")
Header = element("header")
Nav = element("nav")
Main = element("main")

# Text
H1 = element("h1")
H2 = element("h2") 
H3 = element("h3")
H4 = element("h4")
H5 = element("h5")
H6 = element("h6")
P = element("p")
Title = element("title")
A = element("a")

# Forms
Button = element("button")
Input = element("input")
Label = element("label")
Form = element("form")
Select = element("select")
Option = element("option")
Textarea = element("textarea")

# Media
Img = element("img")
Video = element("video")
Audio = element("audio")
Source = element("source")

# Lists
Ul = element("ul")
Ol = element("ol")
Li = element("li")

# Tables
Table = element("table")
Thead = element("thead")
Tbody = element("tbody")
Tr = element("tr")
Th = element("th")
Td = element("td")

# Special
Script = element("script")
Style = element("style")
Link = element("link")
Meta = element("meta")
Br = element("br")
Hr = element("hr")

# HTML5 extras
Canvas = element("canvas")
Progress = element("progress")
Meter = element("meter")
Details = element("details")
Summary = element("summary")

# htpyX() extra
def tag(name: str, content: str = "", **attrs) -> str:
    attributes = " ".join([f'{key}="{value}"' for key, value in attrs.items()])
    if attributes:
        return f"<{name} {attributes}>{content}</{name}>"
    return f"<{name}>{content}</{name}>"

