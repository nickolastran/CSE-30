
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes


class Steganography():

    def __init__(self):
        self.text = ""
        self.binary = ""
        self.delimiter = "#"
        self.codec = None

    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)
        #print(image) for debugging
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8        # calculate available bytes
        print("Maximum bytes available:", max_bytes)

        if codec == "binary":                                       # convert into binary
            self.codec = Codec()
        elif codec == "caesar":
            self.codec = CaesarCypher()
        elif codec == "huffman":
            self.codec = HuffmanCodes()

        binary = self.codec.encode(message + self.delimiter)
        num_bytes = ceil(len(binary)//8) + 1                        # check if possible to encode the message

        if  num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes)
            self.text = message
            self.binary = binary
            count = 0
            for pos, x in np.ndenumerate(image):
                value = image[pos[0]][pos[1]][pos[2]]
                if (self.binary[count] == "0") and (value % 2 != 0):
                    if (value == 255):
                        image[pos[0]][pos[1]][pos[2]] -= 1
                    else:
                        image[pos[0]][pos[1]][pos[2]] += 1
                elif (self.binary[count] == "1") and (value % 2 == 0):
                    image[pos[0]][pos[1]][pos[2]] += 1
                count += 1
                if (count >= len(binary)):
                    break
            cv2.imwrite(fileout, image)

    def decode(self, filein, codec):
        image = cv2.imread(filein)
        # print(image) for debugging
        flag = True
        if codec == "binary":                                           # convert into text
            self.codec = Codec()
        elif codec == "caesar":
            self.codec = CaesarCypher()
        elif codec == "huffman":
            if self.codec == None or self.codec.name != "huffman":
                print("A Huffman tree is not set!")
                flag = False

        if flag:
            binary_data = ""                                            # you may create an additional method that extract bits from the image array
            for i in np.nditer(image):
                binary_data += str(i % 2)
            # update the data attributes:
            self.text = self.codec.decode(binary_data)
        print(self.text)

    def print(self):
        if self.text == "":
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)

    def show(self, filename):
        print(mpimg.imread(filename))
        plt.imshow(mpimg.imread(filename))
        plt.show()

if __name__ == "__main__":
    
    s = Steganography()

    s.encode("fractal.jpg", "fractal.png", "hello", "binary")
    # NOTE: binary should have a delimiter and text should not have a delimiter
    assert s.text == "hello"
    assert s.binary == "011010000110010101101100011011000110111100100011"

    s.decode("fractal.png", "binary")
    # NOTE: binary should have a delimiter and text should not have a delimiter
    assert s.text == "hello"
    assert s.binary == "011010000110010101101100011011000110111100100011"

    print("Everything works!!!")
