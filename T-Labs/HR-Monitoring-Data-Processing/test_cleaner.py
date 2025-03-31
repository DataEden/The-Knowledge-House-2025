from cleaner import filter_nondigits
from test_run import assert_equal

from config import clean1_out, clean2_out, clean3_out

if __name__ == "__main__":
    print("filter_nondigits function test")

    in_data = ["1\n", "2\n", "3\n", "4\n", "5\n", "6\n", "7\n"]
    assert_equal(filter_nondigits(in_data), clean1_out, "1")

    in_data = ["1\n", "\n", "3\n", "4\n", "5\n", "\n", "7\n"]
    assert_equal(filter_nondigits(in_data), clean2_out, "2")

    in_data = ["1\n", "NO DATA\n", "3\n", "4\n", "5\n", "NO DATA\n", "7\n"]
    assert_equal(filter_nondigits(in_data), clean2_out, "3")

    in_data = []
    assert_equal(filter_nondigits(in_data), clean3_out, "4")

    in_data = ["H", "e", "l", "l", "o"]
    assert_equal(filter_nondigits(in_data), clean3_out, "5")
