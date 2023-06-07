def seq_sum(sequence):
    result = 0
    for i in sequence:
        if isinstance(i, int):
            result += i
        elif isinstance(i, list): # elif isinstance(i, list or tuple):
            result += seq_sum(i)
        elif isinstance(i, tuple):
            result += seq_sum(i)
    return result
  
sequence = [1,2,3,[4,5, (6,7)]]

print(seq_sum(sequence))
