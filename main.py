# Standard Python Libraty to modify svg files
import xml.etree.ElementTree as ET
# Standard Python Library to create svg files
import svgwrite


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


def create_text_svg(file_name,text_content, drawing_size =(300,300), text_position=(150,250), color="black", font_family="Arial", font_size="20px", font_weight="bold", font_style="normal"):
    """Creates a new svg file containing text.

    To call the function, you need to provide two pieces of information

    1. The name of the file you'd like to create
    2. The content of the text
    """
    dwg = svgwrite.Drawing(file_name, drawing_size)

    dwg.add(dwg.text(text_content, insert=text_position, fill=color,style=f"font-family: {font_family}; font-size: {font_size} font-weight: {font_weight}; font-style: {font_style}"))
     
    dwg.save()

    return file_name


# Create an initail text drawing
create_text_svg("text_drawing.svg", "Hello, World!", color="red")

# Read the file and modify the text
modify_svg("text_drawing.svg","modified_text.svg")






