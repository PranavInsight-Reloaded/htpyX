#!/usr/bin/env python3
from core import element, w, export_html
from Xcss import CSSBuilder

Html = element("html")
Head = element("head")
Body = element("body")
Div = element("div")
H1 = element("h1")
H2 = element("h2")
H3 = element("h3")
P = element("p")
Title = element("title")
Button = element("button")
Section = element("section")
Pre = element("pre")
Meta = element("meta")
Style = element("style")
A = element("a")
Span = element("span")

app_name = "htpyX"
version = w("1.0.0", name="version")
release_date = w("2025", name="release_date")
tagline = "Write Python, Get HTML+JS+CSS"

feature_list = [
    "W-Tech Variable System",
    "CSS Generator with Glassmorphism",
    "DOM Element Builder",
    "Python-to-JS Transpiler (pyXjs)",
    "Responsive Design Utilities",
    "Release-ready Templates"
]
features = w(feature_list, name="features")

author = w("PranavInsight Reloaded", name="author")
github_url = w("https://github.com/PranavInsight-Reloaded/htpyx-pro", name="github_url")

# CSS inspired by the YouTube thumbnail with liquid glass effects
css = CSSBuilder()
css.var("primary-color", "#667eea")
css.var("accent-color", "#764ba2")
css.var("glass-blur", "20px")
css.var("text-primary", "#ffffff")
css.var("bg-gradient", "linear-gradient(135deg, #667eea 0%, #764ba2 100%)")

css.define("""
* { 
    margin: 0; 
    padding: 0; 
    box-sizing: border-box; 
}

body { 
    font-family: 'Inter', system-ui, -apple-system, sans-serif; 
    background: var(--bg-gradient); 
    color: var(--text-primary);
    line-height: 1.6;
    min-height: 100vh;
    overflow-x: hidden;
}

.container { 
    max-width: 1200px; 
    margin: 0 auto; 
    padding: 40px 24px; 
}

/* Main Glass Card - inspired by YouTube thumbnail */
.main-glass-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(var(--glass-blur));
    border-radius: 24px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.2);
    padding: 40px;
    margin-bottom: 30px;
    position: relative;
    overflow: hidden;
}

.main-glass-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, 
        transparent, 
        rgba(255, 255, 255, 0.4), 
        transparent
    );
}

/* Content Section */
.content-section {
    margin-bottom: 30px;
}

.content-heading {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 20px;
    text-align: center;
}

.content-heading italic {
    font-style: italic;
    opacity: 0.9;
}

.content-text {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(15px);
    border-radius: 16px;
    padding: 30px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    line-height: 1.8;
    font-size: 1.1rem;
}

.content-text strong {
    color: rgba(255, 255, 255, 0.95);
    font-weight: 600;
}

.content-text br {
    margin-bottom: 10px;
}

/* Feature Grid */
.feature-grid { 
    display: grid; 
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); 
    gap: 20px; 
    margin: 40px 0; 
}

.feature-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(15px);
    border-radius: 16px;
    padding: 24px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    text-align: center;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.feature-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg,
        transparent,
        rgba(255, 255, 255, 0.1),
        transparent
    );
    transition: left 0.6s ease;
}

.feature-card:hover::before {
    left: 100%;
}

.feature-card:hover {
    transform: translateY(-5px);
    border-color: rgba(255, 255, 255, 0.3);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

/* Liquid Glass Button */
.liquid-glass-btn {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    color: white;
    padding: 18px 40px;
    border-radius: 50px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    position: relative;
    overflow: hidden;
    margin: 20px auto;
    display: block;
    text-decoration: none;
    box-shadow: 
        0 8px 25px rgba(0, 0, 0, 0.2),
        inset 0 1px 0 rgba(255, 255, 255, 0.3);
    text-align: center;
    width: fit-content;
    min-width: 250px;
}

.liquid-glass-btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg,
        transparent,
        rgba(255, 255, 255, 0.4),
        transparent
    );
    transition: left 0.6s ease;
}

.liquid-glass-btn:hover::before {
    left: 100%;
}

.liquid-glass-btn:hover {
    background: rgba(255, 255, 255, 0.25);
    transform: translateY(-3px) scale(1.05);
    box-shadow: 
        0 15px 35px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.4);
    border-color: rgba(255, 255, 255, 0.4);
}

.liquid-glass-btn:active {
    transform: translateY(-1px) scale(1.02);
}

/* Hero Section */
.hero { 
    text-align: center; 
    padding: 60px 0 40px 0;
}

.hero h1 {
    font-size: 3.5rem;
    font-weight: 800;
    margin-bottom: 16px;
    text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.hero h2 {
    font-size: 1.4rem;
    opacity: 0.9;
    margin-bottom: 30px;
    font-weight: 400;
}

/* Code Blocks */
.code-block { 
    background: rgba(0, 0, 0, 0.3);
    padding: 20px;
    border-radius: 12px;
    overflow-x: auto;
    font-family: 'Fira Code', 'Monaco', 'Cascadia Code', monospace;
    font-size: 0.85rem;
    line-height: 1.5;
    border: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    margin: 20px 0;
}

/* Footer */
.footer { 
    margin-top: 60px; 
    text-align: center; 
    opacity: 0.8;
    padding: 40px 0 20px 0;
}

/* Typography */
h1, h2, h3 {
    font-weight: 700;
    line-height: 1.2;
}

h2 {
    font-size: 2.2rem;
    margin-bottom: 24px;
    text-align: center;
}

h3 {
    font-size: 1.3rem;
    margin-bottom: 12px;
    color: rgba(255, 255, 255, 0.9);
}

p {
    opacity: 0.8;
    margin-bottom: 16px;
}

/* Demo Section */
.demo-section {
    text-align: center;
    padding: 40px 0;
}

.feature-display {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(15px);
    border-radius: 16px;
    padding: 30px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    min-height: 140px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 30px 0;
    position: relative;
    overflow: hidden;
}

.feature-display::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, 
        transparent, 
        rgba(255, 255, 255, 0.3), 
        transparent
    );
}

/* Responsive */
@media (max-width: 768px) {
    .container {
        padding: 20px 16px;
    }
    
    .hero h1 {
        font-size: 2.5rem;
    }
    
    .feature-grid {
        grid-template-columns: 1fr;
        gap: 16px;
    }
    
    .main-glass-card {
        padding: 24px;
        border-radius: 20px;
    }
    
    .liquid-glass-btn {
        padding: 16px 32px;
        font-size: 1rem;
    }
    
    .content-heading {
        font-size: 2rem;
    }
    
    .content-text {
        padding: 20px;
        font-size: 1rem;
    }
}
""")

# Build the components with YouTube thumbnail inspired design
hero_content = Div(
    H1(app_name),
    H2(tagline),
    P("Transform Python code into stunning web applications with beautiful glassmorphic UI and zero runtime overhead.", 
      style="max-width: 600px; margin: 0 auto 30px; font-size: 1.1rem;"),
    class_="hero main-glass-card"
)

features_grid = Div(
    *[
        Div(
            H3(f"✨ {feature}"),
            P("Seamless integration with automatic type conversion and real-time updates."),
            class_="feature-card"
        ) for feature in feature_list
    ],
    class_="feature-grid"
)

code_examples = Section(
    H2("💻 See the Magic"),
    Div(
        Div(
            H3("Python Input"),
            Pre(
"""# htpyX Python Code
from core import w, export_html
from Xcss import CSSBuilder

# W-Tech Variables
app_name = w("My App", name="app_name")

# CSS with Glassmorphism
css = CSSBuilder()
css.var("primary-color", "#667eea")

# Build UI
app = Div(
    H1(app_name, class_="glass-card"),
    Button("Click me", class_="liquid-glass-btn")
)

export_html(app, "my_app.html")""",
                class_="code-block"
            ),
        ),
        Div(
            H3("Generated Output"),
            Pre(
"""<!-- Auto-generated HTML -->
<div>
  <h1 class="glass-card">My App</h1>
  <button class="liquid-glass-btn">
    Click me
  </button>
</div>

<style>
:root { --primary-color: #667eea; }
.liquid-glass-btn { 
  background: rgba(255,255,255,0.15);
  backdrop-filter: blur(20px);
}
</style>""",
                class_="code-block"
            ),
        ),
        class_="feature-grid"
    ),
    class_="main-glass-card"
)

# htpyX/core
core_content = Div(
    H1("htpyX/<strong>core</strong>", Span(">", style="font-style: italic; opacity: 0.9;")),
    Div(
        P('''This is the heart of the htpyX module. It contains code that transpiles htpyX code to html code. It also indirectly relies on the elements for functionality.'''),
        P('''The core module provides the fundamental building blocks for creating web applications using Python syntax.'''),
        class_="content-text"
    ),
    class_="content-section main-glass-card"
)

# htpyX/Xcss
xcss_content = Div(
    H1(Span("htpyX/Xcss", Span(">", style="font-style: italic; opacity: 0.9;"))),
    Div(
        P('''The Xcss module provides advanced CSS generation with built-in glassmorphism effects.'''),
        P('''Create stunning visual designs using Python syntax with automatic vendor prefixing.'''),
        class_="content-text"
    ),
    class_="content-section main-glass-card"
)

# htpyX/elements
elements_content = Div(
    H1("htpyX/elements", Span(">", style="font-style: italic; opacity: 0.9;")),
    Div(
        P('''Contains all HTML element constructors for building web interfaces with Python.'''),
        P('''Each HTML element is represented as a Python function for intuitive DOM construction.'''),
        class_="content-text"
    ),
    class_="content-section main-glass-card"
)

# htpyX/pyXjs
pyxjs_content = Div(
    H1("htpyX/pyXjs", Span(">", style="font-style: italic; opacity: 0.9;")),
    Div(
        P('''Python-to-JavaScript transpiler for seamless conversion of Python logic to client-side JS.'''),
        P('''Handles variables, functions, and control structures with W-Tech integration.'''),
        class_="content-text"
    ),
    class_="content-section main-glass-card"
)

# htpyX/W-Tech
wtech_content = Div(
    H1("W-Tech", Span(">", style="font-style: italic; opacity: 0.9;")),
    Div(
        P('''Revolutionary variable system for seamless data flow between Python and JavaScript.'''),
        P('''Handles variable synchronization and real-time updates across the full stack.'''),
        class_="content-text"
    ),
    class_="content-section main-glass-card"
)


live_demo = Section(
    H2("🔬 Live W-Tech Demo"),
    Div(
        P("💡 Click the liquid glass button to see the magic in action!", 
          style="text-align: center; margin-bottom: 10px;"),
        Div(
            P("✨ Ready to explore htpyX features...", 
              style="text-align: center; opacity: 0.8;"),
            id="featureDisplay", 
            class_="feature-display"
        ),
        Div(
            Button("🎯 Experience Liquid Glass", 
                   class_="liquid-glass-btn", 
                   onclick="showcaseWtech()"),
            style="text-align: center;"
        ),
    ),
    class_="demo-section main-glass-card"
)

footer = Div(
    H3(f"🌟 {app_name} v{version}"),
    P(f"Built with passion by {author}"),
    P(f"Released in {release_date}"),
    P(A(github_url, href=github_url, 
        style="color: rgba(255,255,255,0.9); text-decoration: none; font-weight: 600;")),
    class_="footer main-glass-card"
)

root = Html(
    Head(
        Title("htpyX 1.0 - The Pythonic Web Framework"),
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Style(css.generate())
    ),
    Body(
        Div(
            hero_content,
            Section(H2("✨ Core Features"), features_grid),
            code_examples,
            core_content,       
            xcss_content,         
            elements_content,   
            pyxjs_content,      
            wtech_content,      
            live_demo,
            footer,
            class_="container"
        )
    )
)

# JavaScript for liquid glass interactions
extra_js = '''
// Liquid Glass Interactive Functions
function showcaseWtech() {
    console.log('🎯 Demonstrating Liquid Glass Effect');
    
    const display = document.getElementById('featureDisplay');
    if (display) {
        // Create a liquid wave effect
        display.innerHTML = `
            <div style="text-align: center;">
                <h3 style="margin-bottom: 12px; color: rgba(255,255,255,0.9);">Liquid Glass Active! 🌊</h3>
                <p style="margin-bottom: 16px;">W-Tech System Running Smoothly</p>
                <div style="font-size: 0.9rem; opacity: 0.8; line-height: 1.6;">
                    <div>✨ ${features.length} Features Loaded</div>
                    <div>🎨 Glassmorphism Active</div>
                    <div>⚡ Zero Runtime Overhead</div>
                </div>
            </div>
        `;
        
        // Enhanced liquid effect
        display.style.background = 'rgba(255, 255, 255, 0.12)';
        display.style.borderColor = 'rgba(255, 255, 255, 0.3)';
        
        setTimeout(() => {
            display.style.background = '';
            display.style.borderColor = '';
        }, 2000);
    }
    
    // Add ripple effect to button
    const buttons = document.querySelectorAll('.liquid-glass-btn');
    buttons.forEach(btn => {
        btn.style.transform = 'translateY(-3px) scale(1.05)';
        setTimeout(() => {
            btn.style.transform = '';
        }, 300);
    });
}

let features = [
    "W-Tech Variable System",
    "CSS Generator with Glassmorphism",
    "DOM Element Builder", 
    "Python-to-JS Transpiler (pyXjs)",
    "Responsive Design Utilities",
    "Release-ready Templates"
];

// Add floating animation to feature cards
function initFloatingCards() {
    const cards = document.querySelectorAll('.feature-card');
    cards.forEach((card, index) => {
        card.style.animation = `float 3s ease-in-out ${index * 0.2}s infinite alternate`;
    });
}

// Add CSS for floating animation
const style = document.createElement('style');
style.textContent = `
    @keyframes float {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-10px); }
    }
    
    .feature-card {
        animation: float 3s ease-in-out infinite alternate;
    }
    
    .feature-card:nth-child(2) { animation-delay: 0.4s; }
    .feature-card:nth-child(3) { animation-delay: 0.8s; }
    .feature-card:nth-child(4) { animation-delay: 1.2s; }
    .feature-card:nth-child(5) { animation-delay: 1.6s; }
    .feature-card:nth-child(6) { animation-delay: 2s; }
`;

document.head.appendChild(style);

// Initialize when page loads
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 htpyX Liquid Glass Showcase Loaded');
    console.log(`🌟 ${app_name} v${version} ready with liquid glass effects`);
    initFloatingCards();
});
'''

export_html(root, "index.html", extra_js=extra_js)

print("✅ Liquid Glass htpyX showcase generated: htpyx_liquid_glass.html")
print(f"📊 Features showcased: {len(feature_list)}")
print("🎨 New additions:")
print("   • htpyX/core content section with description")
print("   • Styled italic heading with glassmorphism")
print("   • Enhanced content text with proper formatting")
print("   • Liquid glass button with centered text")
print("🌐 Open htpyx_liquid_glass.html in your browser")