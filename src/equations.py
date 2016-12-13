import numpy as np

def normalize(unnormalized_array):
    npArray = np.array(unnormalized_array)
    normalized_array = [ 100 * (int - npArray.min())/(npArray.max() - npArray.min()) for int in npArray]
    return normalized_array

def compute_linear_combination(json_data, weight):
    values = [dict['value'] for dict in json_data]
    return sum([value * weight for value in values])
