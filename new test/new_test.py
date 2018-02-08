x = list(range(11))
import random
random.shuffle(x)
x.sort()
print x
alist = [i*i for i in x]
print alist
