from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
...
array = ft_load("landscape.jpg")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_invert.__doc__)

from PIL import Image

Image.fromarray(ft_invert(array)).show()
Image.fromarray(ft_red(array)).show()