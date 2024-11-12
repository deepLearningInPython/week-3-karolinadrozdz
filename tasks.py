import numpy as np

# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.

# Task 1: Compute Output Size for 1D Convolution
# Instructions:
# Write a function that takes two one-dimensional numpy arrays (input_array, kernel_array) as arguments.
# The function should return the length of the convolution output (assuming no padding and a stride of one).
# The output length can be computed as follows:
# (input_length - kernel_length + 1)

# Your code heree:
# -----------------------------------------------

def compute_output_size_1d(input_array, kernel_array):
    input_length = len(input_array)
    kernel_length = len(kernel_array)
    output_size = input_length - kernel_length +1
    return output_size

# -----------------------------------------------
# Example:
input_array = np.array([1, 2, 3, 4, 5])
kernel_array = np.array([1, 0, -1])
print(compute_output_size_1d(input_array, kernel_array))


# Task 2: 1D Convolution
# Instructions:
# Write a function that takes a one-dimensional numpy array (input_array) and a one-dimensional kernel array (kernel_array)
# and returns their convolution (no padding, stride 1).

# Your code here:
#lala
# -----------------------------------------------

def convolve_1d(input_array, kernel_array):

    # Tip: start by initializing an empty output array (you can use your function above to calculate the correct size).
    # Then fill the cells in the array with a loop.
    output_length = compute_output_size_1d(input_array, kernel_array)
    output_array = np.zeros(output_length)
    for i in range(output_length):
        output_array[i] = np.dot(input_array[i:i + len(kernel_array)], kernel_array)
    return output_array

# -----------------------------------------------
# Another tip: write test cases like this, so you can easily test your function.
input_array = np.array([1, 2, 3, 4, 5])
kernel_array = np.array([1, 0, -1])
print(convolve_1d(input_array, kernel_array))

# Task 3: Compute Output Size for 2D Convolution
# Instructions:
# Write a function that takes two two-dimensional numpy matrices (input_matrix, kernel_matrix) as arguments.
# The function should return a tuple with the dimensions of the convolution of both matrices.
# The dimensions of the output (assuming no padding and a stride of one) can be computed as follows:
# (input_height - kernel_height + 1, input_width - kernel_width + 1)

# Your code here:
# -----------------------------------------------

def compute_output_size_2d(input_matrix, kernel_matrix):
    input_height = len(input_matrix)        
    input_width = len(input_matrix[0])   

    kernel_height = len(kernel_matrix)     
    kernel_width = len(kernel_matrix[0]) 

    height = input_height - kernel_height + 1
    width = input_width - kernel_width + 1
    output = (height, width)
    return output


# -----------------------------------------------


# Task 4: 2D Convolution
# Instructions:
# Write a function that computes the convolution (no padding, stride 1) of two matrices (input_matrix, kernel_matrix).
# Your function will likely use lots of looping and you can reuse the functions you made above.

# Your code here:
# -----------------------------------------------
def convolute_2d(input_matrix, kernel_matrix):
    # Calculate the output dimensions using compute_output_size_2d
    output_height, output_width = compute_output_size_2d(input_matrix, kernel_matrix)
    
    # Initialize the output matrix as a list of lists
    output_matrix = [[0] * output_width for _ in range(output_height)]
    
    # Get the dimensions of the kernel
    kernel_height = len(kernel_matrix)
    kernel_width = len(kernel_matrix[0])
    
    # Perform the convolution
    for i in range(output_height):
        for j in range(output_width):
            # Compute the convolution sum for each position (i, j)
            conv_sum = 0
            for ki in range(kernel_height):
                for kj in range(kernel_width):
                    conv_sum += input_matrix[i + ki][j + kj] * kernel_matrix[ki][kj]
            output_matrix[i][j] = conv_sum
    
    
    return output_matrix



# -----------------------------------------------