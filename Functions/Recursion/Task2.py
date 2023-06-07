
def linear_seq(sequence):
    result = []
    for i in sequence:
        if isinstance(i, int):
            result.append(i)
        elif isinstance(i, list): # elif isinstance(i, list or tuple):
            result.extend(linear_seq(i))
        elif isinstance(i, tuple):
            result.extend(linear_seq(i))
    return result
  
sequence = [1,2,3,[4,5, (6,7)]]

print(linear_seq(sequence))
[1,2,3,4,5,6,7]