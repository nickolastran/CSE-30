import matplotlib.pyplot as plt                             # need for plotting an image
import matplotlib.image as mpimg                            # need for image loading and saving
import numpy as np                                          # need for manipulating arrays
from numpy import linalg as la                              # need for finding SVD

def compress(img, k, debug = False):
    X, Y, Z = img.shape 

    # red pixels
    red = img[:, :, 0]
    print('red pixels:')
    print(red)
    # green pixels
    green = img[:, :, 1]
    print('green pixels:')
    print(green)
    # blue pixels
    blue = img[:, :, 2]
    print('blue pixels:')
    print(blue)

    # find SVD
    U, s, Vt = la.svd(red)
    print(U.shape, s.shape, Vt.shape)
    U, s, Vt = la.svd(green)
    print(U.shape, s.shape, Vt.shape)
    U, s, Vt = la.svd(blue)
    print(U.shape, s.shape, Vt.shape)

    # verify SVD
    Sigma = np.zeros((X, Y))  # convert s (a 1D array) into Sigma (a 2D-array)
    for i in range(X):
        Sigma[i, i] = s[ i]
    print(np.allclose(red, U @ Sigma @ Vt)) # verify the equality of the original array and decomposed array
    plt.plot(s) # visualize the diagonal values of SVD
    plt.show()

    # choose significant values in the diagonal of SVD
    # red octopus
    k = 50
    red_approx = U @ Sigma[:, :k] @ Vt[:k, :]
    print(red_approx.shape)
    plt.imshow(red_approx, cmap = "Reds")
    plt.show()
    # green octopus
    k = 50
    green_approx = U @ Sigma[:, :k] @ Vt[:k, :]
    print(green_approx.shape)
    plt.imshow(green_approx, cmap = "Greens")
    plt.show()
    # blue octopus
    k = 50
    blue_approx = U @ Sigma[:, :k] @ Vt[:k, :]
    print(blue_approx.shape)
    plt.imshow(blue_approx, cmap = "Blues")
    plt.show()

    img_approx = np.stack((red, green, blue), axis=2)
    img_approx = img_approx - img_approx.min() 
    img_approx = img_approx / img_approx.max()
    plt.imshow(img_approx)
    plt.show()

if __name__ == '__main__':
    img = mpimg.imread('octopus.jpg')                       # read the image file and display the image
    plt.imshow(img)
    plt.show()
    
    print(img.ndim)                                         # analyze the image array
    print(img.shape)
    print(img.dtype)
    print(img.max())
    print(img.min())

    img_approx = compress(img, 100)
    plt.imshow(img_approx)
    plt.show()
    plt.imsave("octopus_new.jpg", img_approx)