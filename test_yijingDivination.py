import unittest
from yijingDivination import YijingDivination

class TestYijingDivination(unittest.TestCase):
    def setUp(self):
        self.diviner = YijingDivination()

    def test_yao_values(self):
        """
        测试 get_yao_value 方法，确保返回的四种爻都能出现
        """
        line_counter = {
            "老阴（变爻）": 0,  # 6
            "少阳": 0,         # 7
            "少阴": 0,         # 8
            "老阳（变爻）": 0   # 9
        }

        # we test 1000 times
        for _ in range(1000):
            _, nature = self.diviner.get_yao_value()
            if nature in line_counter:
                line_counter[nature] += 1

        print("\n===== TEST RESULTS =====")
        for nature, count in line_counter.items():
            print(f"{nature}: {count}")
        print("========================")

        # ensure no line is stuck at 0
        for nature, count in line_counter.items():
            self.assertNotEqual(count, 0, f"{nature} did not appear at all!")

if __name__ == '__main__':
    unittest.main()