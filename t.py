import scipy
from scipy import stats
import sys


def get_t_value_from_csv(csv_file):
    data = scipy.genfromtxt(csv_file, delimiter=",")
    t, p = scipy.stats.ttest_rel([x[0] for x in data], [x[1] for x in data])
    return t


def main():
    t = get_t_value_from_csv(sys.argv[1])
    print(t)


if __name__ == '__main__':
    main()