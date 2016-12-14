import unittest
import numpy as np
import equations

def isclose(a, b, rel_tol=1e-09, abs_tol=1e-09):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

class EquationsTest(unittest.TestCase):

    def test_compute_z_score(self):
        self.assertTrue(isclose(equations.compute_z_score([1, 2, 3], 3), 1.224744871391589))

if __name__ == '__main__':
    unittest.main()