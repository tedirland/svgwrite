import svgwrite

# Create a new drawing
dwg = svgwrite.Drawing('my_rect3.svg', size=('300px', '300px'))

dwg.add(dwg.rect(insert=(100, 100), size=(50, 20), fill='blue'))

# Add a red circle
dwg.add(dwg.circle(center=(120, 90), r=20, fill='red'))

# Add text without styling
dwg.add(dwg.text('Hello SVG', insert=(100, 110), fill='black'))


brian = {
    "first_name": "Brian",
    "last_name": "Keehner",
    "font": "Arial"
}
font_family = {"Arial"}

# Add text with styling
dwg.add(dwg.text('Hello SVG', insert=(10, 50), fill='green', 
                 style=f"font-family: {font_family}; font-size: 20px; font-weight: bold; font-style: italic;"))


dwg.save()