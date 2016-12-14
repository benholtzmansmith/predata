import numpy as np
import math
from datetime import datetime, timedelta

def normalize(unnormalized_array):
    npArray = np.array(unnormalized_array)
    normalized_array = [ 100 * (int - npArray.min())/(npArray.max() - npArray.min()) for int in npArray]
    return normalized_array

def compute_linear_combination(json_data, weight):
    values = [dict['value'] for dict in json_data]
    return sum([value * weight for value in values])

def filter_by_date(list_of_dates_values, target_dict, window):
    for date_value_dict in list_of_dates_values:
        if (
            date_value_dict['date'] <= target_dict['date']
                and
            date_value_dict['date'] >= (target_dict['date'] - timedelta(days=window))
        ): yield date_value_dict

def compute_variance(list_of_values, mean):
    if len(list_of_values) == 0: return None
    else: return sum([ (value - mean) **2 for value in list_of_values]) / float(len(list_of_values))

def compute_z_score(list_of_date_value, current_value):
    list_values = [date_value_dict['value'] for date_value_dict in list_of_date_value]
    if len(list_values) == 0: return 0
    else:
        mean = sum(list_values)/float(len(list_values))
        variance = compute_variance(list_values, mean)
        standard_deviation = math.sqrt(variance)
        if standard_deviation == 0: return 0
        else: return (current_value - mean) / standard_deviation
