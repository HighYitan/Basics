#Example
# def print_hi(name):
#     print(f'Hi, {name}')
#     if __name__ == '__main__':
#         print_hi('PyCharm')
#Hello
# def hello():
#     print(f'Hello world')
#
#
# hello()
n1 = int(input("Number 1"))
n2 = int(input("Number 2"))
def product(n1,n2):
    result = n1 * n2
    if result > 1000:
        result = n1 + n2
        return result
    else:
        return result

result = product(n1,n2)
print("\nResult is", result)
