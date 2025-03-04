import numpy as np


sample = 1000

number = 90
choice = []
count = 0
for i in range(sample):
    step = 1
    while step < number:
        step += int(np.random.choice([1,2]))
        if step == number:
            count += 1
    
prob = count/sample
print(prob)



