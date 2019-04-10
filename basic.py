count = 0
def num(n):
    global count
    if n == 0:
        count += 1
    else:
        #subtract 2 and check if greater than 0. If so call recursive
        if n - 2 >= 0:
            num(n-2)

        #subtract 1 and call recursive    
        num(n-1)
    




for i in range(0,11):
    num(i)
    print(count)
    count = 0
