import random
import math

main_data = []
for i in range(100):
    main_data.append(random.randint(1, 100))

mean = sum(main_data) / len(main_data)
print("Mean =", mean)

main_data.sort()
n = len(main_data)
if n % 2 == 0:
    median = (main_data[n//2 - 1] + main_data[n//2]) / 2
else:
    median = main_data[n//2]
print("Median =", median)
variance = 0

for x in main_data:
    variance += (x - mean) ** 2

variance = variance / len(main_data)

std_dev = math.sqrt(variance)

print("Standard Deviation =", std_dev)
