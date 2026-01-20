def vector_maximum(vector):
  max_x = vector[0]
  for x in vector:
    if x > max_x:
      max_x = x
  return max_x

my_vector = [0.5, 4, 9, 0, -5]
print(vector_maximum(my_vector))
