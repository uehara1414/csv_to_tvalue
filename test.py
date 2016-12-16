import unittest

from t import get_t_value_from_csv


class Test(unittest.TestCase):

    def test_get_value_from_csv(self):
        self.assertAlmostEqual(get_t_value_from_csv('sample.csv'), -1.957909937)


if __name__ == '__main__':
    unittest.main()