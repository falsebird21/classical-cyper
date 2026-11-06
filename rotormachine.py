import random

word='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def init():
    word_list=list(word)
    left=random.sample(word_list)
    mid=random.sample(word_list)
    right=random.sample(word_list)

def rotateRight():