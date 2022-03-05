from ursina.prefabs.grid_editor import PixelEditor
from PIL import Image
from ursina import *
app = Ursina()
empty_texture = Texture(Image.new(mode='RGBA',
                                  size=(32, 32),
                                  color=(255, 255, 255, 255)))
PixelEditor(texture=empty_texture,)

app.run()