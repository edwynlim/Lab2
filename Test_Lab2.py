import Lab2

print("Test_Lab2")


def test_calc_average():
    num_list = [1, 2, 2, 1, 4]
    result = Lab2.calc_average(num_list)

    assert (result == 2)