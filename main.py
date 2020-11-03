#Example of Pycharm
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
#Multi and sum
# n1 = int(input("Number 1 "))
# n2 = int(input("Number 2 "))
# def product(n1,n2):
#     result = n1 * n2
#     if result > 1000:
#         result = n1 + n2
#         return result
#     else:
#         return result
#
# result = product(n1,n2)
# print("\nResult is", result)
#Range iteration
def Ranged(number):
    lastnumber = 0
    for iteration in range(number):
        sum = lastnumber + iteration
        print(f"Our number,", iteration, "Last number,", lastnumber, "Sum", sum)
        lastnumber = iteration
n = 10
print("Printing until", n,"the number and lastnumber and their sum \n")
Ranged(n)