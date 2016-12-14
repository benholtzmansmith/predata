import numpy as np
import math
from datetime import datetime, timedelta

def normalize(unnormalized_array):
    npArray = np.array(unnormalized_array)
    normalized_array = [ 100 * (int - npArray.min())/(npArray.max() - npArray.min()) for int in npArray]
    return normalized_array

def compute_linear_combination(json_data, weight):
    return sum(np.multiply(values, weight))

def filter_by_date(list_of_dates_values, target_dict, window):
    for date_value_dict in list_of_dates_values:
        if (
            date_value_dict['date'] <= target_dict['date']
                and
            date_value_dict['date'] >= (target_dict['date'] - timedelta(days=window))
        ): yield date_value_dict['value']

def compute_z_score(inclusive_values, value):
    if len(inclusive_values) == 0: return 0
    else:
        mean = np.mean(inclusive_values)
        standard_deviation = np.std(inclusive_values)
        if standard_deviation == 0: return 0
        else: return (value - mean) / standard_deviation

if __name__ == '__main__':
    main()