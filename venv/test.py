import numpy as np
def square(x):
    return x*x

x = np.random.randint(1,10)
y = square(x)
print("%d squared is %d" %(x,y))