import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")

a_input = input("\nEnter a single number for array 'a': ")
a = np.array(int(a_input))

b_input = input("Enter space-separated (ex.1 2 3) numbers for array 'b': ")
b = np.array([int(num) for num in b_input.split()])

c_input = input("Enter space-separated (ex.1 2 3) numbers for a 2D array 'c' (two rows): ")
c = np.array([[int(num) for num in c_input.split()]])

d_input1 = input("Enter space-separated (ex.1 2 3) umbers for a 3D array 'd' (first set of two rows): ")
d_input2 = input("Enter space-separated (ex.1 2 3) numbers for a 3D array 'd' (second set of two rows): ")
d = np.array([[[int(num) for num in d_input1.split()]], [[int(num) for num in d_input2.split()]]])

# Print the number of dimensions for each array
print("Number of dimensions for 'a':", a.ndim)
print("Number of dimensions for 'b':", b.ndim)
print("Number of dimensions for 'c':", c.ndim)
print("Number of dimensions for 'd':", d.ndim)
