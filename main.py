from svgeditor import modify_svg
from svgwriter import create_text_svg

# Create an initail text drawing

#TODO 1. Change the file name below (this will be the name of the new file you create) 
#TODO 2. Change the text that currently says "Hello World!" if you want to 
#TODO 3. You can pass another string to the color property. remember, it has to be lower case

dwg = create_text_svg("CHANGEME.svg", "Hello, World!", color="red")

# Read the file and modify the text

#TODO 1. Change the name of the .svg file name below if you want, this will be the name of the modified file
modify_svg(dwg,"modified_text.svg")






