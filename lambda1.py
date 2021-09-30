

def name(tom, jerry):
    return [val for val in tom if jerry(val)]

myList = [1, 2, 3, 4, 5, 6]

yourlist = name(myList, lambda x: x != 5)

print(yourlist)