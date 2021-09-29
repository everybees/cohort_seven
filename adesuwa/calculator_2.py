import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,  # use operator.div for Python 2
    '%': operator.mod,
    '^': operator.xor,
}


def calculate_something():
    first_number = float(input())
    second_number = float(input())
    sign = input()

    if sign in ops.keys():
        answer = ops[sign](first_number, second_number)
        print(answer)

        while True:
            sign = input("enter an operator or exit to quit program\n")
            if sign == "exit":
                print(answer)
                break
            number = float(input())
            if sign in ops.keys():
                answer = ops[sign](answer, number)
                print(answer)
