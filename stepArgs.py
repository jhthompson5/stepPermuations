count = 0
valid_steps = [1,3,5]
steps = sorted(valid_steps,reverse=True)
def num(n):
    global steps   
    global count
    if n == 0:
        count += 1
    else:
        #iterate through valid steps in reverse (largest to smallest)
        for step in steps:
            if n - step >= 0:
                num(n-step)


for i in range(20):
    num(i)
    print(count)
    count = 0