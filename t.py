from scipy import stats
import sys
import csv

def load(name):
    l1 = []
    l2 = []
    with open(name, 'r') as fp:
        reader = csv.reader(fp)

        for row in reader:
            if row[0]:
                l1.append(float(row[0]))
            if row[1]:
                l2.append(float(row[1]))
    return l1, l2


if __name__ == '__main__':
    l1, l2 = load(sys.argv[1])
    t, p = stats.ttest_rel(l1, l2)
    print(t)
