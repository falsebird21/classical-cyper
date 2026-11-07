import random

word='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
left = random.sample(word,26)
mid = random.sample(word,26)
right = random.sample(word,26)
midCond = random.randint(0,26)
leftCond = random.randint(0,26)

def rotateRight():
    right = right[1:]+right[0]

def rotateMid():
    if right[0] == 'A' + midCond:
        mid = mid[1:]+mid[0]

def rotateLeft():
    if mid[0] == 'A'+ leftCond:
        left = left[1:] + left[0]

def permutation(t):
    for _ in t:
        loc = word.find(_)
        rotateLeft()
        rotateMid()
        rotateRight()
        _ = right[loc]

ptxt = input("Input your plaintext")
ctxt = permutation(ptxt)
print(ctxt)