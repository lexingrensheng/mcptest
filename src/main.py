from src.calculator import Calculator

def main():
    calc = Calculator()
    
    print("简单计算器示例")
    print("==============")
    
    # 加法示例
    result = calc.add(10, 5)
    print(f"10 + 5 = {result}")
    
    # 减法示例
    result = calc.subtract(10, 5)
    print(f"10 - 5 = {result}")
    
    # 乘法示例
    result = calc.multiply(10, 5)
    print(f"10 * 5 = {result}")
    
    # 除法示例
    try:
        result = calc.divide(10, 5)
        print(f"10 / 5 = {result}")
    except ValueError as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    main()