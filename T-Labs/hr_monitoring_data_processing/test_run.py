import os.path
import glob
from main import run

from config import data1_out, data2_out, data3_out, data4_out

def assert_equal(result: list, correct: list, name: str) -> None:
    """
    A function to assert correct implementation of functions
    """
    if result == correct:
        print(f"Test {name}: ✅")
    else:
        print(f"Test {name} : ❌")
        print(f"Expected {correct}, got {result}")


if __name__ == "__main__":
    # test correct implementation of basic file
    print("PHASE 0 TEST")
    assert_equal(run("data/phase0.txt"), data1_out, "Functionality")

    # test correct implementation of buggy file
    print("PHASE 1 TEST")
    assert_equal(run("data/phase1.txt"), data2_out, "Functionality")

    # test correct implementation of file with 1 value
    print("PHASE 2 TEST")
    assert_equal(run("data/phase2.txt"), data3_out, "Functionality")

    # test correct implementation of file with 1 blank line
    print("PHASE 3 TEST")
    assert_equal(run("data/phase3.txt"), data4_out, "Functionality")
