import svgwrite

def create_text_svg(file_name,text_content, drawing_size =(1000,1000), text_position=(150,250), color="black", font_family="Arial", font_size="20px", font_weight="bold", font_style="normal"):
    """Creates a new svg file containing text.

    To call the function, you need to provide two pieces of information

    1. The name of the file you'd like to create
    2. The content of the text
    """
    dwg = svgwrite.Drawing(file_name, drawing_size)

    dwg.add(dwg.text(text_content, insert=text_position, fill=color))
     
    dwg.save()

    return file_name