from htpyX_elements import *
from htpyX_core import export_html
from css_generator import CSSBuilder

# ======================
# 🎨 CSS STYLES
# ======================
css = CSSBuilder()

# CSS Variables
css.var("primary", "#6e8efb")
css.var("accent", "#a777e3")
css.var("glass-blur", "12px")
css.var("glass-alpha", "0.15")

# Base styles
css.define("body",
    background="linear-gradient(135deg, var(--primary), var(--accent))",
    background_attachment="fixed",
    margin="0",
    padding="0",
    font_family="'Segoe UI', system-ui",
    color="white",
    min_height="100vh"
)

# Glassmorphic sidebar
css.define(".sidebar",
    position="fixed",
    top="0",
    left="0",
    width="250px",
    height="100vh",
    background="rgba(255,255,255,0.1)",
    backdrop_filter="blur(var(--glass-blur))",
    border_right="1px solid rgba(255,255,255,0.1)",
    padding="2rem 1rem",
    box_shadow="0 8px 32px rgba(0,0,0,0.1)"
)

# User card
css.define(".user-card",
    display="flex",
    align_items="center",
    gap="1rem",
    padding="1rem",
    background="rgba(255,255,255,0.1)",
    border_radius="12px",
    margin_bottom="2rem"
)

css.define(".user-avatar",
    width="60px",
    height="60px",
    border_radius="50%",
    background="rgba(0,0,0,0.3)",
    display="flex",
    align_items="center",
    justify_content="center",
    font_size="1.5rem",
    font_weight="bold",
    color="var(--primary)"
)

css.define(".user-details h3",
    margin="0",
    font_size="1.2rem",
    font_weight="600"
)

css.define(".user-details p",
    margin="0.25rem 0 0",
    opacity="0.8",
    font_size="0.9rem"
)

# Menu items
css.define(".menu-item",
    display="flex",
    align_items="center",
    gap="1rem",
    padding="1rem",
    margin="0.5rem 0",
    border_radius="8px",
    cursor="pointer",
    transition="all 0.3s ease"
)

css.define(".menu-item:hover",
    background="rgba(255,255,255,0.15)",
    transform="translateX(5px)"
)

css.define(".menu-icon",
    font_size="1.2rem",
    width="24px",
    text_align="center"
)

# Content area
css.define(".content",
    margin_left="250px",
    padding="3rem"
)

css.define(".card",
    background="rgba(255,255,255,0.1)",
    backdrop_filter="blur(8px)",
    border_radius="12px",
    padding="2rem",
    margin_bottom="2rem",
    box_shadow="0 4px 12px rgba(0,0,0,0.1)"
)

css.define("h1",
    font_size="3rem",
    font_weight="700",
    margin_bottom="1rem",
    background="linear-gradient(90deg, #fff, rgba(255,255,255,0.7))",
    webkit_background_clip="text",
    background_clip="text",
    color="transparent"
)

css.define("p",
    font_size="1.1rem",
    line_height="1.6",
    opacity="0.9"
)

# ======================
# 🏗️ HTML STRUCTURE
# ======================
page = Html(
    Head(
        Title("Glassmorphic Dashboard"),
        Style(css.generate())
    ),
    Body(
        # Sidebar
        Div(
            # User Card
            Div(
                Div("</>", class_="user-avatar"),
                Div(
                    H3("DevMaster"),
                    P("Senior Developer"),
                    class_="user-details"
                ),
                class_="user-card"
            ),
            
            # Navigation Menu
            Nav(
                Div(
                    Span("🏠", class_="menu-icon"),
                    Span("Dashboard")
                , class_="menu-item"),
                
                Div(
                    Span("📊", class_="menu-icon"), 
                    Span("Analytics")
                , class_="menu-item"),
                
                Div(
                    Span("⚡", class_="menu-icon"),
                    Span("Performance")
                , class_="menu-item"),
                
                Div(
                    Span("🔧", class_="menu-icon"),
                    Span("Settings")
                , class_="menu-item"),
                
                Div(
                    Span("🚪", class_="menu-icon"),
                    Span("Logout")
                , class_="menu-item")
            ),
            
            class_="sidebar"
        ),
        
        # Main Content
        Div(
            H1("Welcome to Your Dashboard"),
            
            # Cards Grid
            Div(
                Div(
                    H2("Projects"),
                    P("Manage your ongoing projects and tasks"),
                    class_="card"
                ),
                
                Div(
                    H2("Analytics"),
                    P("View performance metrics and insights"),
                    class_="card"
                ),
                
                Div(
                    H2("Team"),
                    P("Collaborate with your team members"),
                    class_="card"
                ),
                
                style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;"
            ),
            
            # Stats Section
            Div(
                H2("Quick Stats"),
                P("Everything is working perfectly!"),
                P("Glassmorphism effects are active"),
                P("CSS variables are functioning"),
                P("Layout is responsive"),
                class_="card"
            ),
            
            class_="content"
        )
    )
)

# Export
export_html(page, "glassmorphic_dashboard.html")
print("✅ Glassmorphic dashboard created! Open 'glassmorphic_dashboard.html'")