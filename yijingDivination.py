import random

class YijingDivination:
    def __init__(self):
        self.total_stalks = 49  # 正确的蓍草数量是49根
        
    def divide_stalks(self):
        """模拟一次蓍草分配过程，返回6,7,8,9其中一个数字"""
        stalks = self.total_stalks
        
        # 第一次分配：分成左右两堆
        left = random.randint(20, 30)
        right = stalks - left
        
        # 取一根放在左手间
        right -= 1
        
        # 四份分配过程
        left_remainder = left % 4 or 4
        right_remainder = right % 4 or 4
        
        # 计算最终数字
        total_remainder = left_remainder + right_remainder
        
        # 根据传统计算方法转换成卦数
        number = 9 - (total_remainder // 2)
        return number
    
    def get_single_yao(self):
        """获取一个爻的值和性质"""
        number = self.divide_stalks()
        
        if number == 9:  # 老阳
            return "———", "老阳"
        elif number == 8:  # 少阴
            return "— —", "少阴"
        elif number == 7:  # 少阳
            return "———", "少阳"
        else:  # 老阴 (6)
            return "— —", "老阴"
    
    def cast_hexagram(self):
        """得到完整的卦象"""
        hexagram = []
        yao_nature = []
        
        print("【古代占卜者】：正在使用蓍草进行占卜...")
        for i in range(6):
            yao, nature = self.get_single_yao()
            hexagram.append(yao)
            yao_nature.append(nature)
            print(f"第{i+1}爻：{nature}")
            
        return hexagram, yao_nature

def main():
    print("欢迎来到古代占卜模拟器！")
    input("请心中默想你的问题，然后按回车继续...")
    
    diviner = YijingDivination()
    hexagram, natures = diviner.cast_hexagram()
    
    print("\n========== 卦象形成 ==========")
    # 从上到下打印卦象
    for yao in reversed(hexagram):
        print(yao)

if __name__ == "__main__":
    main()
