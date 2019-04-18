import numpy as np
from pprint import pprint
def arr():
    np_arr = np.array([1,2,3,4,5])
    print(np_arr)
    print(np_arr.shape)
    print(type(np_arr))

def arr_initialize():
    zeros = np.zeros(5)
    ones = np.ones((2, 3))

    pprint(zeros)
    pprint(ones)

def extract_line():
    test = np.random.random((3,3))
    pprint(test)
    print(test[:, 0])
    print(test[:, :2])

def mat_mul():
    a = np.array([[1, 2], [2, 1]])
    b = np.array([[1, 2], [2, 1]])
    print(a*b)
    print(a.dot(b))

def plot():
    import matplotlib.pyplot as plt
    a = np.linspace(0, 2 * np.pi, 50)
    b = np.sin(a)
    plt.plot(a, b)
    mask = b >= 0
    plt.plot(a[mask], b[mask], 'bo')
    mask = (b >= 0) & (a <= np.pi / 2)
    plt.plot(a[mask], b[mask], 'go')
    plt.show()

def test_index():
    a = np.arange(0, 100, 10)
    b = a[:5]
    c = a[a >= 50]
    print(b)  # >>>[ 0 10 20 30 40]
    print(c)  # >>>[50 60 70 80 90]

def test_where():
    a = np.arange(0, 100, 10)
    b = a[np.where(a < 50)]
    c = a[np.where(a >= 50)]
    print(b)  # >>>(array([0, 1, 2, 3, 4]),)
    print(c)  # >>>[5 6 7 8 9]

test_where()