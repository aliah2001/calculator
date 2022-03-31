from scipy import integrate
equation = []


def plus_func(list_of_numbers):
    for i in list_of_numbers:
        if i == '+':
            index_ = list_of_numbers.index(i)
            a = list_of_numbers[index_ - 1]
            b = list_of_numbers[index_ + 1]
            c = a + b
            list_of_numbers.insert(index_, c)
            list_of_numbers.remove(list_of_numbers[index_ - 1:index_ + 2])
    return list_of_numbers


def subtraction(list_of_numbers):
    for i in list_of_numbers:
        if i == '-':
            index_ = list_of_numbers.index(i)
            if index_ == 0:
                a = 0
            else:
                a = list_of_numbers[index_ - 1]
            b = list_of_numbers[index_ + 1]
            c = a - b
            list_of_numbers.insert(index_, c)
            if index_ == 0:
                list_of_numbers.remove(list_of_numbers[index_:index_ + 2])
            else:
                list_of_numbers.remove(list_of_numbers[index_ - 1:index_ + 2])
    return list_of_numbers


def multiple(list_of_numbers):
    for i in list_of_numbers:
        if i == '+':
            index_ = list_of_numbers.index(i)
            a = list_of_numbers[index_ - 1]
            b = list_of_numbers[index_ + 1]
            c = a * b
            list_of_numbers.insert(index_, c)
            list_of_numbers.remove(list_of_numbers[index_ - 1:index_ + 2])
    return list_of_numbers


def division(list_of_numbers):
    for i in list_of_numbers:
        if i == '/':
            index_ = list_of_numbers.index(i)
            a = list_of_numbers[index_ - 1]
            b = list_of_numbers[index_ + 1]
            c = a / b
            list_of_numbers.insert(index_, c)
            list_of_numbers.remove(list_of_numbers[index_ - 1:index_ + 2])
    return list_of_numbers
