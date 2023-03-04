
# assignment: programming assignment 4
# author: Nickolas Tran
# date: 3/1/2023
# converts infix to postfix and calculates the output using evalute from tree

from stack import Stack
from tree import ExpTree

def infix_to_postfix(infix):
    s = Stack()
    num = ""
    postfix = []
    priority = {"(": 0,         # giving priority values to the operators
                "+": 1,
                "-": 1,
                "*": 2,
                "/": 2,
                "^": 3}

    for char in infix:
        if char.isdigit() or char == ".":
            num += char
        else:
            if num:
                postfix.append(num)
                num = ""
            if char not in "+-*/^()":
                postfix.append(char)
            elif char == "(":
                s.push(char)
            elif char == ")":
                while s.peek() != "(":
                    postfix.append(s.pop())
                s.pop()
            else:
                while not s.isEmpty() and s.peek() != "(" and priority[s.peek()] >= priority[char]:
                    postfix.append(s.pop())
                s.push(char)
    if num:
        postfix.append(num)
    while not s.isEmpty():
        postfix.append(s.pop())
    return " ".join(postfix)

def calculate(infix):
    user_input = infix_to_postfix(infix)                        # infix -> postfix
    tree = ExpTree.make_tree(user_input.split())                # use postfix to make a tree -> makeTree()
    return ExpTree.evaluate(tree)                               # return the evaluation


# print(infix_to_postfix("51+20*(4-2)^3"))                      # print statements to test postfix output
# print(infix_to_postfix("(1.3+2.7)*((2.02-0.02)+1)+6.5"))
# print(infix_to_postfix("((3^2-4)*(5-2))-(2^3+1)"))

# a driver to test calculate module
if __name__ == "__main__":
    assert infix_to_postfix("(5+2)*3") == "5 2 + 3 *"
    assert infix_to_postfix("5+2*3") == "5 2 3 * +"

    # test calculate function
    assert calculate("(5+2)*3") == 21.0
    assert calculate("5+2*3") == 11.0

    print("Welcome to Calculator Program!")
    while True:
        user_input = input("Please enter your expression here. To quit enter \"quit\" or \"q\":\n")
        if user_input == "quit" or user_input == "q":
            print("Goodbye!")
            break
        print(calculate(user_input))