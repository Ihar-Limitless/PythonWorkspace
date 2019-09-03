import sys


def countLines(name):
    f = open(name, "r")
    line = f.readlines()
    return print(len(line))


def countChars(name):
    f = open(name, "r")
    line = f.read()
    return print(len(line))


def test(name):
    countLines(name)
    countChars(name)


