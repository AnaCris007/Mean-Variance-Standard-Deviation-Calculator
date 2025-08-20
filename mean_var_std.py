import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    array = np.array([[list]])
    Narray = array.reshape(3, 3)
    dic = {
        'mean': [np.mean(Narray, axis = 0).tolist(), 
                 np.mean(Narray, axis = 1).tolist(), 
                 np.mean(Narray).tolist()],

        'variance': [np.var(Narray, axis = 0).tolist(), 
                     np.var(Narray, axis = 1).tolist(), 
                     np.var(Narray).tolist()],

        'standard deviation': [np.std(Narray, axis = 0).tolist(),
                               np.std(Narray, axis = 1).tolist(),
                               np.std(Narray).tolist()],
    
        'max': [np.max(Narray, axis = 0).tolist(),
                np.max(Narray, axis = 1).tolist(),
                np.max(Narray).tolist()],

        'min': [np.min(Narray, axis = 0).tolist(),
                np.min(Narray, axis = 1).tolist(),
                np.min(Narray).tolist()],
        
        'sum': [np.sum(Narray, axis = 0).tolist(),
                np.sum(Narray, axis = 1).tolist(),
                np.sum(Narray).tolist()]
    }
    return dic


