# The bad version of tree.py code. It is functional, but is deemed bad 
# because you cannot understand what is going on. 

from math import radians
from Tree.core import Tree
from PIL import Image

tree = Tree((0, 0, 0, -200), [(0.75, radians(-30)), (0.75, radians(30))])
tree.grow(10)
tree.move_in_rectangle()
image = Image.new("RGB", tree.get_size(), (200, 240, 250))
tree.draw_on(image, (50, 40, 0, 180, 130, 30), (30, 160, 30), 25)
image.show()