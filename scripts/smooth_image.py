import matplotlib.pyplot as plt
from envtest import rand_array, smooth_image
from scipy import misc
shape = (3, 3)
image = misc.ascent()
sigma = 5 
smoothed_image = smooth_image(image, sigma)

f = plt.figure()
f.add_subplot(1, 2, 1)
plt.imshow(image)
f.add_subplot(1, 2, 2)
plt.imshow(smoothed_image)
plt.show(block=True)

print(rand_array(shape))
