sum = 0
range_end = int(input("Enter the ending number of the range: "))

for i in range(1, range_end + 1):
    sum += i
print("The sum of all numbers from 1 to", range_end, "is:", sum)