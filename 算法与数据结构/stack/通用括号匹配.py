from stackop import Stack



def is_match(left_bkt, right_bkt):
    left_bkts = '([{'
    right_bkts = ')]}'
    return left_bkts.index(left_bkt) == right_bkts.index(right_bkt)

def par_checker(symbol_string):
    s = Stack()
    balanced = True

    for i in range(len(symbol_string)):
        smbl = symbol_string[i]
        if smbl in '([{':
            s.push(smbl)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not is_match(top,smbl):
                    balanced = False
    if balanced and s.is_empty():
        return True
    return False

if __name__ == "__main__":
    print(par_checker('(({{}}))'))
