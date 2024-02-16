def pattern(numOfLines):
    for i in range(numOfLines):
        str(numOfLines)
        print(" " * numOfLines - 1, end='')
        print("* ")
        print(" " * numOfLines - 1, end='')
        i += 1

pattern(4)

"""
___*
__*_*
_*_*_*
*_*_*_*
"""