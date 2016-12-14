import unittest
import numpy as np
import equations
from datetime import datetime

def isclose(a, b, rel_tol=1e-09, abs_tol=1e-09):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

class EquationsTest(unittest.TestCase):

    def test_filter_by_date_inclusive(self):
        data = [
            {"date": datetime.strptime('2011-03-07','%Y-%m-%d'), "value":2},
            {"date": datetime.strptime('2011-03-10','%Y-%m-%d'), "value":4},
            {"date": datetime.strptime('2011-04-07','%Y-%m-%d'), "value":6},
            {"date": datetime.strptime('2011-06-07','%Y-%m-%d'), "value":8}
        ]

        target_dict = {"date": datetime.strptime('2011-04-07','%Y-%m-%d'), "value":2}

        result = equations.filter_by_date_inclusive(data, target_dict, 31)

        expected_result = [2,4,6]

        self.assertEqual(result, expected_result)

    def test_compute_z_score(self):
        self.assertTrue(isclose(equations.compute_z_score([1, 2, 3], 3), 1.224744871391589))

    def test_integration(self):
        taget_dict = {'date': datetime(2005, 2, 14, 0, 0), 'value': 52.15}

        test_data = [
            {'date': datetime(2005, 2, 14, 0, 0), 'value': 52.15},
            {'date': datetime(2005, 2, 11, 0, 0), 'value': 52.1},
            {'date': datetime(2005, 2, 10, 0, 0), 'value': 52.26},
            {'date': datetime(2005, 2, 9, 0, 0), 'value': 52.52},
            {'date': datetime(2005, 2, 8, 0, 0), 'value': 53.2},
            {'date': datetime(2005, 2, 7, 0, 0), 'value': 53.51},
            {'date': datetime(2005, 2, 4, 0, 0), 'value': 53.46},
            {'date': datetime(2005, 2, 3, 0, 0), 'value': 53.42},
            {'date': datetime(2005, 2, 2, 0, 0), 'value': 53.06},
            {'date': datetime(2005, 2, 1, 0, 0), 'value': 52.61},
            {'date': datetime(2005, 1, 31, 0, 0), 'value': 52.4},
            {'date': datetime(2005, 1, 28, 0, 0), 'value': 52.43},
            {'date': datetime(2005, 1, 27, 0, 0), 'value': 53.08},
            {'date': datetime(2005, 1, 26, 0, 0), 'value': 53.28},
            {'date': datetime(2005, 1, 25, 0, 0), 'value': 53.28},
            {'date': datetime(2005, 1, 24, 0, 0), 'value': 53.07},
            {'date': datetime(2005, 1, 21, 0, 0), 'value': 53.01},
            {'date': datetime(2005, 1, 20, 0, 0), 'value': 53.37},
            {'date': datetime(2005, 1, 19, 0, 0), 'value': 53.78},
            {'date': datetime(2005, 1, 18, 0, 0), 'value': 54.49},
            {'date': datetime(2005, 1, 14, 0, 0), 'value': 53.99},
            {'date': datetime(2005, 1, 13, 0, 0), 'value': 53.64},
            {'date': datetime(2005, 1, 12, 0, 0), 'value': 54.08},
            {'date': datetime(2005, 1, 11, 0, 0), 'value': 53.59},
            {'date': datetime(2005, 1, 10, 0, 0), 'value': 53.72},
            {'date': datetime(2005, 1, 7, 0, 0), 'value': 53.99},
            {'date': datetime(2005, 1, 6, 0, 0), 'value': 54.05},
            {'date': datetime(2005, 1, 5, 0, 0), 'value': 53.29},
            {'date': datetime(2005, 1, 4, 0, 0), 'value': 53.22},
            {'date': datetime(2005, 1, 3, 0, 0), 'value': 53.35}
        ]

        t = taget_dict['date']

        window = 30

        v = taget_dict['value']

        filtered_data = equations.filter_by_date_inclusive(test_data, t, window)

        z_score_test1 = equations.compute_z_score( filtered_data ,v )

        z_score_test2 = equations.compute_z_score( [x['value'] for x in test_data] ,v )

        self.assertTrue(isclose(z_score_test1, -1.7881655074403577))

        self.assertTrue(isclose(z_score_test2, -1.7881655074403577))



if __name__ == '__main__':
    unittest.main()