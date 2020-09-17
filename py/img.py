import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

img = misc.face()
type(img)
plt.imshow(img)
plt.show()
print(img.shape)
print(img.ndim)
