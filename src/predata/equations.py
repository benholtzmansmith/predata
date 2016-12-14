import numpy as np
import math
from datetime import datetime, timedelta

def normalize(unnormalized_array):
    npArray = np.array(unnormalized_array)
    normalized_array = [ 100 * (int - npArray.min())/(npArray.max() - npArray.min()) for int in npArray]
    return normalized_array

def compute_linear_combination(values, weight):
    return sum(np.multiply(values, weight))

def filter_by_date_inclusive(list_of_dates_values, date, window):
    filtered_data = [date_value_dict['value'] for date_value_dict in list_of_dates_values
        if (
            date_value_dict['date'] <= date
                and
            date_value_dict['date'] >= (date - timedelta(days=window))
        )]
    return list(filtered_data)

def compute_z_score(inclusive_values, value):
    if len(inclusive_values) == 0: return 0
    else:
        mean = np.mean(inclusive_values)
        standard_deviation = np.std(inclusive_values)
        if standard_deviation == 0: return 0
        else: return (value - mean) / standard_deviation

def format_dates(json_data):
    values = [x['value'] for x in json_data]
    formated_dates = [datetime.strptime(x['date'],'%Y-%m-%d') for x in json_data]
    return [ {"date":date, "value":value} for date, value in zip(formated_dates, values)]

if __name__ == '__main__':
    main()