import random

class YijingDivination:
    def __init__(self):
        self.total_stalks = 49

    def single_division(self, stalks):
        """
        单次蓍草分配过程，返回剩余的蓍草数和本次分堆的余数总和
        传统算法：
        1. 分成左右两堆
        2. 取出右堆中的一根
        3. 分别取4的余数，0视为4
        4. 计算余数之和
        """
        if stalks < 3:
            return 0, 8  # Return a reasonable default

        # 随机分堆，但确保每堆至少有1根
        left = random.randint(stalks // 3, 2 * stalks // 3)  # More balanced distribution
        right = stalks - left

        # 从右堆取出一根
        right -= 1

        # 求左右堆余数 (mod 4)，将0当作4
        left_remainder = left % 4 or 4
        right_remainder = right % 4 or 4

        # 计算余数之和
        r_sum = left_remainder + right_remainder

        # 更新剩余的蓍草数：总数减去余数和被取出的那一根
        remaining_stalks = stalks - (left_remainder + right_remainder + 1)

        return remaining_stalks, r_sum

    def get_yao_value(self):
        """
        三次变换，返回单爻(6~9)。
        简化算法，保持传统概率分布：
        老阴(6): 1/8
        少阳(7): 3/8
        少阴(8): 3/8
        老阳(9): 1/8
        """
        # Generate a random number between 1 and 8
        value = random.randint(1, 8)
        
        if value == 1:
            return "— —", "老阴（变爻）"  # 6 (probability 1/8)
        elif value <= 4:
            return "———", "少阳"          # 7 (probability 3/8)
        elif value <= 7:
            return "— —", "少阴"          # 8 (probability 3/8)
        else:
            return "———", "老阳（变爻）"   # 9 (probability 1/8)

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

if __name__ == "__main__":
    main()