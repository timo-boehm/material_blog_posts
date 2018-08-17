import numpy as np
from numpy.random import randint

# A function to simulate one million dice throws.
def one_million_dice():
    return randint(low=1, high=7, size=1000000)

# Let's try %time first
%time throws = one_million_dice()
%time mean = np.mean(throws)

# Outputs:
# Wall time: 20.6 ms
# Wall time: 3.01 ms

# Let's do the same with %timeit
%timeit throws = one_million_dice()
%timeit mean = np.mean(throws)

# Outputs:
# 10 loops, best of 3: 22.2 ms per loop
# 100 loops, best of 3: 2.86 ms per loop

# And finally %%time
%%time
throws = one_million_dice()
mean = np.mean(throws)

# Outputs:
# Wall time: 36.6 ms