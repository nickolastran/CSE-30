
import numpy as np

class Codec():
    def __init__(self, delimiter = "#"):
        self.name = "binary"
        self.delimiter = delimiter

    def encode(self, text):                             # convert text or numbers into binary form 
        if type(text) == str:
            return "".join([format(ord(i), "08b") for i in text])
        else:
            print("Format error")

    def decode(self, data):                             # convert binary data into text
        binary = []
        for i in range(0, len(data), 8):
            byte = data[i : i + 8]
            if byte == self.encode(self.delimiter):
                break
            binary.append(byte)
        text = ""
        for byte in binary:
            text += chr(int(byte, 2))
        return text 


class CaesarCypher(Codec):
    def __init__(self, shift = 3, delimiter = "#"):
        self.name = "caesar"
        self.delimiter = delimiter
        self.shift = shift
        self.chars = 256                                # total number of ASCII characters

    def encode(self, text):                             # convert text into binary form
        if type(text) == str:                           # your code should be similar to the corresponding code used for Codec
            return "".join([format((ord(i) + self.shift)%256, "08b") for i in text])
        else:
            print('Format error')


    def decode(self, data):                             # convert binary data into text
        binary = []                                     # your code should be similar to the corresponding code used for Codec
        for i in range(0, len(data), 8):
            byte = data[i : i + 8]
            if byte == self.encode(self.delimiter):
                break
            binary.append(byte)

        text = ""
        for byte in binary:
            try:
                text += chr(int(byte, 2) - self.shift)
            except:
                text += chr(255 + int(byte, 2) - self.shift)
        return text


class Node:
    def __init__(self, freq, symbol, left = None, right = None):
        self.left = left
        self.right = right
        self.freq = freq
        self.symbol = symbol
        self.code = ""


class HuffmanCodes(Codec):
    def __init__(self):
        self.nodes = None
        self.name = "huffman"
        self.data = {}
        self.delimiter = "#"

    # make a Huffman Tree
    def make_tree(self, data):
        nodes = []                                                                          # make nodes
        for char, freq in data.items():
            nodes.append(Node(freq, char))                                                  # assemble the nodes into a tree
        while len(nodes) > 1:
            nodes = sorted(nodes, key = lambda x : x.freq)                                  # sort the current nodes by frequency
            left = nodes[0]                                                                 # pick two nodes with the lowest frequencies
            right = nodes[1]
            left.code = "0"                                                                 # assign codes
            right.code = "1"
            root = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)    # combine the nodes into a tree
            nodes.remove(left)                                                              # remove the two nodes and add their parent to the list of nodes
            nodes.remove(right)
            nodes.append(root)
        return nodes 

    def make_key(self, node, val):
        next_val = val + node.code
        if(node.left):
            self.traverse_tree(node.left, next_val)
        if(node.right):
            self.traverse_tree(node.right, next_val)
        if(not node.left and not node.right):
            print(f"{node.symbol}->{next_val}")  # this is for debugging, you need to update this part of the code or rearrange it so it suits your need

    def traverse_tree(self, node, val):
        current_node = node
        output = ""
        for i in val:
            if (val[0] == "0"):
                try:
                    current_node.right.symbol
                    current_node = current_node.left
                    val = val[1:]
                except:
                    if (current_node.symbol == "#"):
                        break
                    output += current_node.symbol
                    current_node = node
            if (val[0] == "1"):
                try:
                    current_node.left.symbol
                    current_node = current_node.right
                    val = val[1:]
                except:
                    if (current_node.symbol == "#"):
                        break
                    output += current_node.symbol
                    current_node = node
        return output

    def encode(self, text):                         # convert text into binary form
        data = ""
        freq = {}
        for x in text:
            try:
                freq[x] += 1
            except:
                freq[x] = 1
        self.make_key(self.make_tree(freq), "")
        for x in text:
            data += self.data[x]
        return data

    def decode(self, data):                         # convert binary data into text
        output = ""
        key = ""
        for i in range(len(data)):
            key += data[i]
            if (key in list(self.data.values())):
                word = [i for i in self.data.keys() if self.data[i] == key]
                if (word[0] == "#"):
                    return output
                output += word[0]
                key = ""
        return self.traverse_tree(self.nodes, data)

if __name__ == '__main__':
    text = 'hello' 
    #text = 'Casino Royale 10:30 Order martini' 
    print('Original:', text)
    
    c = Codec()
    binary = c.encode(text + c.delimiter)
    # NOTE: binary should have a delimiter and text should not have a delimiter
    print('Binary:', binary) # should print '011010000110010101101100011011000110111100100011'
    data = c.decode(binary)  
    print('Text:', data)     # should print 'hello'
    
    cc = CaesarCypher()
    binary = cc.encode(text + cc.delimiter)
    # NOTE: binary should have a delimiter and text should not have a delimiter
    print('Binary:', binary)
    data = cc.decode(binary) 
    print('Text:', data)     # should print 'hello'
