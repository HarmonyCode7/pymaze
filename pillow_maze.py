from PIL import Image, ImageDraw

img  = Image.new('RGB', (50*4, 50*4), color='green')
img.save('green-pillow.png')

