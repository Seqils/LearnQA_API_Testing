class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        assert a + b == 14

    def test_check_math2(self):
        a = 11
        b = 9
        expected_sum = 14
        assert a + b == 14, f"Sum not equal to {expected_sum}"
