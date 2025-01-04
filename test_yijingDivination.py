import unittest
from yijingDivination import YijingDivination

class TestYijingDivination(unittest.TestCase):
    def setUp(self):
        self.diviner = YijingDivination()

    def test_yao_values(self):
        """
        测试 get_yao_value 方法，确保返回的值在 6-9 之间
        """
        valid_totals = {6, 7, 8, 9}
        iterations = 1000  # 运行多次以统计结果
        results = {6:0, 7:0, 8:0, 9:0, 'unknown':0}

        for _ in range(iterations):
            yao, nature = self.diviner.get_yao_value()
            if nature == "老阴（变爻）":
                results[6] +=1
            elif nature == "少阳":
                results[7] +=1
            elif nature == "少阴":
                results[8] +=1
            elif nature == "老阳（变爻）":
                results[9] +=1
            else:
                results['unknown'] +=1

        print("\n========== 测试结果 ==========")
        for key, value in results.items():
            print(f"{key}: {value} 次")

        # 确保没有 'unknown' 结果
        self.assertEqual(results['unknown'], 0, "存在未知的爻值")

        # 确保各个爻值都有出现
        self.assertTrue(all(results[val] > 0 for val in valid_totals), "某些爻值未出现")

if __name__ == '__main__':
    unittest.main()