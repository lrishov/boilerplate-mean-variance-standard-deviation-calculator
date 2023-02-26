import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
   
    sarray = np.array(list).reshape((3,3))
    calculations = {}
    calculations['mean'] = [sarray.mean(axis = x).tolist() for x in [0, 1, None]]
    calculations['variance'] = [sarray.var(axis = x).tolist() for x in [0, 1, None]]
    calculations['standard deviation'] = [sarray.std(axis = x).tolist() for x in [0, 1, None]]
    calculations['max'] = [sarray.max(axis = x).tolist() for x in [0, 1, None]]
    calculations['min'] = [sarray.min(axis = x).tolist() for x in [0, 1, None]]
    calculations['sum'] = [sarray.sum(axis = x).tolist() for x in [0, 1, None]]

    return calculations
