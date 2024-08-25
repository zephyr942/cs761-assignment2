import operator

# 定义一个映射字典，将字符串映射到运算符函数
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

# 示例：假设我们有两个数字和一个运算符字符串
a = 10
b = 5
operator_str = '+'

# 使用字典来调用相应的运算符函数
result = operations[operator_str](a, b)
print(result)