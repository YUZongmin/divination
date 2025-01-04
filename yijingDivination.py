import random

class YijingDivination:
    def __init__(self):
        self.total_stalks = 49
        # 64卦的名称字典
        self.hexagram_names = {
            '111111': ('乾', 'Qián', '天'),
            '000000': ('坤', 'Kūn', '地'),
            '100010': ('屯', 'Zhūn', '屯'),
            '010001': ('蒙', 'Méng', '蒙'),
            '111010': ('需', 'Xū', '需'),
            '010111': ('讼', 'Sòng', '讼'),
            '010000': ('师', 'Shī', '师'),
            '000010': ('比', 'Bǐ', '比'),
            '111011': ('小畜', 'Xiǎo Chù', '小畜'),
            '110111': ('履', 'Lǚ', '履'),
            '111000': ('泰', 'Tài', '泰'),
            '000111': ('否', 'Pǐ', '否'),
            '101111': ('同人', 'Tóng Rén', '同人'),
            '111101': ('大有', 'Dà Yǒu', '大有'),
            '001000': ('谦', 'Qiān', '谦'),
            '000100': ('豫', 'Yù', '豫'),
            '100110': ('随', 'Suí', '随'),
            '011001': ('蛊', 'Gǔ', '蛊'),
            '110000': ('临', 'Lín', '临'),
            '000011': ('观', 'Guān', '观'),
            '100101': ('噬嗑', 'Shì Kè', '噬嗑'),
            '101001': ('贲', 'Bì', '贲'),
            '000001': ('剥', 'Bō', '剥'),
            '100000': ('复', 'Fù', '复'),
            '100111': ('无妄', 'Wú Wàng', '无妄'),
            '111001': ('大畜', 'Dà Chù', '大畜'),
            '100001': ('颐', 'Yí', '颐'),
            '011110': ('大过', 'Dà Guò', '大过'),
            '010010': ('坎', 'Kǎn', '坎'),
            '101101': ('离', 'Lí', '离'),
            '001110': ('咸', 'Xián', '咸'),
            '011100': ('恒', 'Héng', '恒'),
            '001111': ('遁', 'Dùn', '遁'),
            '111100': ('大壮', 'Dà Zhuàng', '大壮'),
            '000101': ('晋', 'Jìn', '晋'),
            '101000': ('明夷', 'Míng Yí', '明夷'),
            '101011': ('家人', 'Jiā Rén', '家人'),
            '110101': ('睽', 'Kuí', '睽'),
            '001010': ('蹇', 'Jiǎn', '蹇'),
            '010100': ('解', 'Xiè', '解'),
            '110001': ('损', 'Sǔn', '损'),
            '100011': ('益', 'Yì', '益'),
            '111110': ('夬', 'Guài', '夬'),
            '011111': ('姤', 'Gòu', '姤'),
            '000110': ('萃', 'Cuì', '萃'),
            '011000': ('升', 'Shēng', '升'),
            '010110': ('困', 'Kùn', '困'),
            '011010': ('井', 'Jǐng', '井'),
            '101110': ('革', 'Gé', '革'),
            '011101': ('鼎', 'Dǐng', '鼎'),
            '100100': ('震', 'Zhèn', '震'),
            '001001': ('艮', 'Gèn', '艮'),
            '001011': ('渐', 'Jiàn', '渐'),
            '110100': ('归妹', 'Guī Mèi', '归妹'),
            '001101': ('丰', 'Fēng', '丰'),
            '101100': ('旅', 'Lǚ', '旅'),
            '110110': ('巽', 'Xùn', '巽'),
            '011011': ('兑', 'Duì', '兑'),
            '110010': ('涣', 'Huàn', '涣'),
            '010011': ('节', 'Jié', '节'),
            '110011': ('中孚', 'Zhōng Fú', '中孚'),
            '001100': ('小过', 'Xiǎo Guò', '小过'),
            '101010': ('既济', 'Jì Jì', '既济'),
            '010101': ('未济', 'Wèi Jì', '未济')
        }

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

    def get_binary_hexagram(self, hexagram):
        """将卦象转换为二进制字符串"""
        binary = ''
        for yao in hexagram:
            binary = ('1' if yao == '———' else '0') + binary
        return binary

    def get_hexagram_name(self, hexagram):
        """获取卦象的名称"""
        binary = self.get_binary_hexagram(hexagram)
        if binary in self.hexagram_names:
            chinese, pinyin, name = self.hexagram_names[binary]
            return f"{chinese}卦 ({pinyin})"
        return "未知卦象"

    def get_transformed_hexagram(self, hexagram, natures):
        """获取变卦"""
        transformed = []
        for i, (yao, nature) in enumerate(zip(hexagram, natures)):
            if "变爻" in nature:  # 如果是变爻
                # 老阴变少阳，老阳变少阴
                transformed.append("———" if yao == "— —" else "— —")
            else:
                transformed.append(yao)
        return transformed

    def get_changing_lines(self, natures):
        """获取变爻的位置"""
        return [i + 1 for i, nature in enumerate(natures) if "变爻" in nature]

    def display_hexagram(self, hexagram, changing_lines=None, position=""):
        """显示卦象，标记变爻位置"""
        if changing_lines is None:
            changing_lines = []
        
        print(f"\n{position}卦象（自下而上）：")
        for i, yao in enumerate(reversed(hexagram), 1):
            line_num = 7 - i  # Convert to bottom-up numbering
            if line_num in changing_lines:
                print(f"{yao} ◈ ({line_num})")  # 变爻标记
            else:
                print(f"{yao}   ({line_num})")

def main():
    print("欢迎来到古代占卜模拟器！")
    input("请心中默想你的问题，然后按回车继续...")

    diviner = YijingDivination()
    hexagram, natures = diviner.cast_hexagram()
    
    # 获取变爻位置
    changing_lines = diviner.get_changing_lines(natures)
    
    print("\n========== 卦象解析 ==========")
    
    # 显示本卦
    original_name = diviner.get_hexagram_name(hexagram)
    print(f"\n本卦：{original_name}")
    diviner.display_hexagram(hexagram, changing_lines, "本")
    
    # 如果有变爻，显示变卦
    if changing_lines:
        transformed = diviner.get_transformed_hexagram(hexagram, natures)
        transformed_name = diviner.get_hexagram_name(transformed)
        print(f"\n之卦：{transformed_name}")
        diviner.display_hexagram(transformed, position="变")
        
        print("\n变爻位置：", end="")
        print("第" + "、第".join(str(pos) for pos in changing_lines) + "爻")
    else:
        print("\n无变爻")

    print("\n========== 爻的性质 ==========")
    for i, nature in enumerate(reversed(natures), 1):
        print(f"第{i}爻：{nature}")

if __name__ == "__main__":
    main()