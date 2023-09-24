from stackop import Stack


def par_checker(symbol_string):
    s = Stack()
    balanced = True

    for i in range(len(symbol_string)):
        symbol = symbol_string[i]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
    if balanced and s.is_empty():
        return True
    return False


if __name__ == "__main__":
    print(par_checker('((()))'))
    print(par_checker('((())))'))
    print(par_checker('(((())8)'))