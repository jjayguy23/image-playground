from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img =img.filter(ImageFilter.FIND_EDGES)
filtered_img.save("edges.png", 'png')