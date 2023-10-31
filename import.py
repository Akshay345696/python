class MathOperations:
    def add(self, *args):
        result = 0
        for num in args:
            result += num
        return result

math = MathOperations()

print(math.add(2, 3))
print(math.add(2, 3, 4, 5, 6))
print(math.add(1, 2, 3, 4, 5, 6))