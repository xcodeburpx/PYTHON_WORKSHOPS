from scipy import misc,ndimage
import numpy as np
import matplotlib.pyplot as plt

f = misc.face()
misc.imsave("face.png",f)

plt.imshow(f)
plt.show()

face = misc.face(gray = True)
plt.imshow(face)
plt.show()

lx, ly = face.shape

# Cropping
crop_face = face[lx // 4: - lx // 4, ly // 4: - ly // 4]
plt.imshow(crop_face)
plt.show()


im = np.zeros((256,256))
im[64:-64, 64:-64] = 1
im[90:-90,90:-90] = 2

im = ndimage.gaussian_filter(im,8)

plt.imshow(im)
plt.show()

sx = ndimage.sobel(im, axis = 0, mode = 'constant')
sy = ndimage.sobel(im, axis = 1, mode = 'constant')
sob = np.hypot(sx, sy)

plt.imshow(sob)
plt.show()