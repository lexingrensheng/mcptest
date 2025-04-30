class Calculator:
    def add(self, x, y):
        """加法运算"""
        return x + y
    
    def subtract(self, x, y):
        """减法运算"""
        return x - y
    
    def multiply(self, x, y):
        """乘法运算"""
        return x * y
    
    def divide(self, x, y):
        """除法运算"""
        if y == 0:
            raise ValueError("除数不能为零")
        return x / y