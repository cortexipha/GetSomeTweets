import dictionary


class wordNode(object):
    def __init__(self):
        self.childNodes = []
        self.title = None
        self.type = None


firstNode = wordNode()
lastNode = firstNode
wordStart = 0


def addToNode(word, type):
    global lastNode
    newNode = wordNode()
    newNode.title = word
    newNode.type = type
    lastNode.childNodes.append(newNode)
    lastNode = newNode


def saveFunc(sentence):
    global emptySide, wordStart
    splitedValu = sentence.split(' ')
    for row in splitedValu:
        if (row in dictionary.dict):
            addToNode(row, input(row + ' kelimesinin type\'i nedir? : '))
            wordStart = 1
        else:
            if wordStart == 1:
                ans = input(row + ' kelimesi, ' + lastNode.title + ' ile alakali mi? [e/h]')
                if ans == 'e':
                    addToNode(row, input(row + ' kelimesinin type\'i nedir? : '))
                else:
                    wordStart = 0


def printNode(node):
    print('{' + node.type + '}' + node.title)


def toSub(node):
    printNode(node)
    if node.childNodes:
        for subNode in node.childNodes:
            if subNode.childNodes:
                return toSub(subNode)


def readWholdeTree():
    toSub(firstNode)
