import excalidraw
from PIL import Image

im = Image.open("test.jpeg", "r")
width, height = im.size
pixel_values = list(im.getdata())


scene = excalidraw.Excalidraw()

pixel_size = 16

for x in range(width):
    for y in range(height):
        color = "#%02x%02x%02x" % pixel_values[x + y * height]
        scene.add_rectangle(
            x * (pixel_size),
            y * (pixel_size),
            pixel_size,
            pixel_size,
            backgroundColor=color,
            strokeColor="transparent",
            fillStyle="solid",
            roughness=0,
        )

scene.save_as("image")
