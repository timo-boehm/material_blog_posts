# load the autoreload extension
%load_ext autoreload
# Set extension to reload modules every time before executing code
%autoreload 2

from helperfunctions import complicated_function_to_return_a_number

complicated_function_to_return_a_number()
# Output: 123

# Go to helperfunctions.py and change something withing the function

complicated_function_to_return_a_number()
# Output: 321