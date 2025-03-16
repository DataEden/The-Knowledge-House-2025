from metrics import average, maximum, standard_deviation
from test_run import assert_equal

from config import avg, empty, maxi, stddev


if __name__ == "__main__":
    print("average function test")
    result = average([1, 2, 3, 4, 5, 6, 7])
    assert_equal(result, avg, "1")

    result = average([])
    assert_equal(result, empty, "2")

    print("max function test")
    result = maximum([1, 2, 3, 4, 5, 6, 7])
    assert_equal(result, maxi, "1")

    result = maximum([])
    assert_equal(result, empty, "2")

    print("standard_deviation function test")
    result = standard_deviation([1, 2, 3, 4, 5, 6, 7])
    assert_equal(result, stddev, "1")

    result = standard_deviation([])
    assert_equal(result, empty, "2")
