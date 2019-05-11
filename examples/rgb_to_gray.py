import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

fname = 'img1.png'
image = Image.open(fname).convert("L")
arr = np.asarray(image)
plt.imshow(arr, cmap='gray', vmin=0, vmax=255)
plt.show()