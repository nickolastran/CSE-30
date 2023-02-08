import matplotlib.pyplot as plt                             # need for plotting an image
import matplotlib.image as mpimg                            # need for image loading and saving
import numpy as np                                          # need for manipulating arrays
from numpy import linalg as la                              # need for finding SVD

def compress(img, k, debug = False):
    X, Y, Z = img.shape            

    img_transposed = np.transpose(img, (2, 0, 1))           # apply SVD to all pixels at once
    U, s, Vt = la.svd(img_transposed)
    print(U.shape, s.shape, Vt.shape)
    Sigma = np.zeros((Z, X, Y))
    for j in range(3):
        np.fill_diagonal(Sigma[j, :, :], s[j, :])

    k = 50                                                  # choose significant values in the diagonal of SVD
    img_approx = U @ Sigma[..., :k] @ Vt[..., :k, :]
    img_approx = np.transpose(img_approx, (1, 2, 0))
    img_approx = img_approx - img_approx.min()
    img_approx = img_approx / img_approx.max()
    plt.imshow(img_approx)
    plt.show()
    plt.imsave("octopus_new.jpg", img_approx)

if __name__ == '__main__':
    img = mpimg.imread('octopus.jpg')                       # read the image file and display the image
    plt.imshow(img)
    plt.show()
    
    print(img.ndim)                                         # analyze the image array
    print(img.shape)
    print(img.dtype)
    print(img.max())
    print(img.min())

    img_approx = compress(img, 50)
    plt.imshow(img_approx)
    plt.show()
    plt.imsave("octopus_new.jpg", img_approx)
