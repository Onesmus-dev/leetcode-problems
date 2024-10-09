"""we have a list and you search for n we use linear search """
pos = -1
def search(list,n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
    else:
        return False
    
list = [2,3,5,7,9,10,12]
n = 19

if search(list, n):
    print("found at ", pos)
else:
    print("not found")