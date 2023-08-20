def add_name():
    names=[]
    n=0
    while n<11:
        name=input('Enter a name here: ')
        names.append(name)
        n+=1

    # return names
    for i in names:
        print(i)
    return names

# print(add_name())
add_name()
 