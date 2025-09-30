"""
CSS Generator with W-Tech integration
Supports variables, nested rules, and responsive design
"""

def to_kebab_case(s):
    """Convert python_case to css-case"""
    return s.replace("_", "-")

class CSSBuilder:
    def __init__(self):
        self.variables = {}
        self.classes = {}
        self.media_queries = {}
        self.animations = {}
        
    def var(self, name, value):
        """Define CSS variable"""
        self.variables[name] = value
        return self
        
    def define(self, selector, **styles):
        """Define a CSS rule"""
        self.classes[selector] = styles
        return self
        
    def media(self, query, rules):
        """Define media query with nested rules"""
        self.media_queries[query] = rules
        return self
        
    def keyframes(self, name, frames):
        """Define CSS animations"""
        self.animations[name] = frames
        return self
        
    def glassmorphism(self, blur="10px", transparency="0.1", color="255,255,255"):
        """Quick glassmorphism effect"""
        return {
            "background": f"rgba({color}, {transparency})",
            "backdrop_filter": f"blur({blur})",
            "border": f"1px solid rgba({color}, {transparency})"
        }
        
    def gradient(self, direction, *colors):
        """Create gradient background"""
        colors_str = ", ".join(colors)
        return {
            "background": f"linear-gradient({direction}, {colors_str})"
        }
        
    def shadow(self, x=0, y=4, blur=12, spread=0, color="rgba(0,0,0,0.1)"):
        """Create box shadow"""
        return {
            "box_shadow": f"{x}px {y}px {blur}px {spread}px {color}"
        }
        
    def generate(self):
        """Generate complete CSS"""
        lines = []
        
        # CSS Variables
        if self.variables:
            lines.append(":root {")
            for k, v in self.variables.items():
                lines.append(f"  --{to_kebab_case(k)}: {v};")
            lines.append("}")
            lines.append("")  # Empty line
            
        # Animations
        for name, frames in self.animations.items():
            lines.append(f"@keyframes {name} {{")
            for percentage, styles in frames.items():
                lines.append(f"  {percentage}% {{")
                for prop, val in styles.items():
                    lines.append(f"    {to_kebab_case(prop)}: {val};")
                lines.append("  }")
            lines.append("}")
            lines.append("")
            
        # Regular classes
        for selector, styles in self.classes.items():
            lines.append(f"{selector} {{")
            for prop, val in styles.items():
                lines.append(f"  {to_kebab_case(prop)}: {val};")
            lines.append("}")
            lines.append("")
            
        # Media queries
        for query, rules in self.media_queries.items():
            lines.append(f"@media {query} {{")
            for selector, styles in rules.items():
                lines.append(f"  {selector} {{")
                for prop, val in styles.items():
                    lines.append(f"    {to_kebab_case(prop)}: {val};")
                lines.append("  }")
            lines.append("}")
            lines.append("")
            
        return "\n".join(lines).strip()
    
    def save(self, filename="styles.css"):
        """Save CSS to file"""
        css_content = self.generate()
        with open(filename, "w") as f:
            f.write(css_content)
        return css_content

# Quick utility functions
def glassmorph(blur="10px", transparency="0.1"):
    return CSSBuilder().glassmorphism(blur, transparency)

def quick_gradient(*colors):
    return CSSBuilder().gradient("135deg", *colors)
