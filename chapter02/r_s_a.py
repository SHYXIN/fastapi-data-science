class Example:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Example({self.value!r})"

    def __str__(self):
        return f"Example value is {self.value}"

obj = Example("hello")
print(f"Using repr: {obj!r}")  # 调用 __repr__ 方法
print(f"Using str: {obj!s}")   # 调用 __str__ 方法
print(f"Using ascii: {obj!a}") # 调用 __repr__ 方法并使用 ascii 转换

# 示例：直接使用字符串
value = "hello"
non_ascii_value = "你好"
print(f"Using repr: {value!r}")  # 输出: 'hello'
print(f"Using str: {value!s}")   # 输出: hello
print(f"Using ascii: {value!a}") # 输出: 'hello'
print(f"Using ascii with non-ASCII: {non_ascii_value!a}") # 输出: '\u4f60\u597d'
