import random

class YijingDivination:
    def __init__(self):
        self.total_stalks = 49

    def single_division(self, stalks):
        """
        单次蓍草分配过程
        确保每次分堆后的余数总和为 2 或 3，以保证总和在 6-9 之间
        返回剩余的蓍草数和本次分堆的余数总和
        """
        while True:
            # 随机将蓍草分成左右两堆，确保每堆至少有一根
            left = random.randint(1, stalks - 1)
            right = stalks - left

            # 取出一根作为中间蓍草
            if right <= 0:
                continue  # 无效分堆，重新分堆
            right -= 1  # 移除一根放置一边

            # 计算余数
            left_remainder = left % 4 or 4
            right_remainder = right % 4 or 4

            # 计算本次分堆的余数总和
            remainder_sum = left_remainder + right_remainder

            # 确保余数总和为 2 或 3
            if remainder_sum in [2, 3]:
                remaining_stalks = stalks - left_remainder - right_remainder - 1
                return remaining_stalks, remainder_sum
            # 否则，重新分堆

    def get_yao_value(self):
        """
        完整的三次变换过程，返回单一爻的值
        确保总和在 6-9 之间
        """
        stalks = self.total_stalks
        total = 0

        for _ in range(3):
            stalks, remainder = self.single_division(stalks)
            total += remainder

        # 根据传统六爻对应
        if total == 6:
            return "— —", "老阴（变爻）"
        elif total == 7:
            return "———", "少阳"
        elif total == 8:
            return "— —", "少阴"
        elif total == 9:
            return "———", "老阳（变爻）"
        else:
            # 理论上不会出现，因为单次分堆保证总和为 6-9
            return "———", "未知"

    def cast_hexagram(self):
        """
        获取完整卦象
        """
        hexagram = []
        yao_nature = []

        print("【古代占卜者】：正在使用蓍草进行占卜...")
        for i in range(6):
            print(f"\n第{i + 1}爻占卜过程：")
            yao, nature = self.get_yao_value()
            hexagram.append(yao)
            yao_nature.append(nature)
            print(f"得到：{nature}")

        return hexagram, yao_nature

def main():
    print("欢迎来到古代占卜模拟器！")
    input("请心中默想你的问题，然后按回车继续...")

    diviner = YijingDivination()
    hexagram, natures = diviner.cast_hexagram()

    print("\n========== 卦象形成 ==========")
    print("卦象（自下而上）：")
    for yao in reversed(hexagram):
        print(yao)

    print("\n========== 爻的性质 ==========")
    for i, nature in enumerate(reversed(natures), 1):
        print(f"第{i}爻：{nature}")

    # 可选：输出卦象的整体解释
    # 这里可以根据六十四卦的列表，添加对应卦象的解释

if __name__ == "__main__":
    main()