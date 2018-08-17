from numpy.random import randint
import matplotlib.pyplot as plt

# Sample 1000 random values to create a scatterplot
x = randint(low=1, high=1000, size=100)
y = randint(low=1, high=1000, size=100)

# This will show nothing in a Jupyter Notebook
plt.scatter(x, y)
plt.show()

# Let the magic happen!
%matplotlib inline
plt.scatter(x, y)
plt.show()