import xml.etree.ElementTree as ET

def modify_svg(starting_file, output_file, color=None, font_family=None, font_size=None, font_weight=None, font_style=None):
    # Parse the existing SVG file
    tree = ET.parse(starting_file)
    root = tree.getroot()


    # Print debugging information about the root element
    print(root.tag)

    # Specify the namespace, if your SVG uses one (common with SVG files)
    namespaces = {'svg': 'http://www.w3.org/2000/svg'}  # Adjust if different
    
    # Example: Changing the fill color of all 'rect' (rectangle) elements
    # You may need to change 'rect' to another tag depending on what you want to modify
    options = {
        "fill": color,
        "font-family":font_family,
        "font-size": font_size,
        "font-weight": font_weight,
        "font-style": font_style

    }

    
    # text_content, insert=text_position, fill=color,style=f"font-family: {font_family}; font-size: {font_size} font-weight: {font_weight}; font-style: {font_style}"))
    for element in root.findall('.//svg:text', namespaces=namespaces):
        for key,value in options.items():
            if value is not None:
             element.set(key, value)

    # Write the modified SVG to a new file
    tree.write(output_file)
