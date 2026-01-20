def euclidean_norm(vector):
    vec_sum = 0
    for x in vector: # v = (x1**2 + x2**2 + ... + xn**2)**0.5
        vec_sum += x**2

    vec_sum = vec_sum**0.5
    return(vec_sum)

import numpy as np
my_vector = [0.5, -1.2, 3.3, 4.5]
print(euclidean_norm(my_vector))



