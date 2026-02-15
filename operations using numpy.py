import numpy as np

# 1. Create an array consisting of linearly spaced elements between 0 to 9
arr = np.linspace(0, 9, 10, dtype=int)
print("Original Array:")
print(arr)

# 2. Replace all odd numbers with -1 without modifying original array
new_arr = arr.copy()
for i in range(len(new_arr)):
    if new_arr[i] % 2 != 0:
        new_arr[i] = -1

print("\nArray after replacing odd numbers with -1:")
print(new_arr)

# 3. Convert original 1D array into 2D array with two rows
two_d = arr.reshape(2, 5)
print("\n2D Array with two rows:")
print(two_d)

# 4. Iterate through original array and find sum of all even numbers
even_sum = 0
for num in arr:
    if num % 2 == 0:
        even_sum += num

print("\nSum of all even numbers:")
print(even_sum)

print("\nProgram Completed Successfully!")
