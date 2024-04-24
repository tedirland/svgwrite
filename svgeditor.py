import xml.etree.ElementTree as ET
def modify_svg(starting_file, output_file):
    # Parse the existing SVG file
    tree = ET.parse(starting_file)
    root = tree.getroot()

    # Print debugging information about the root element
    print(root.tag)

    # Specify the namespace, if your SVG uses one (common with SVG files)
    namespaces = {'svg': 'http://www.w3.org/2000/svg'}  # Adjust if different
    
    # Example: Changing the fill color of all 'rect' (rectangle) elements
    # You may need to change 'rect' to another tag depending on what you want to modify
    for element in root.findall('.//svg:text', namespaces=namespaces):
        element.set("fill", 'blue')

    # Write the modified SVG to a new file
    tree.write(output_file)
