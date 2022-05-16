
def zero():
    return 0

def one():
    return 1

def two():
    return 2

def three():
    return 3

def four():
    return 4

def five():
    return 5

def six():
    return 6

def seven():
    return 7

def eight():
    return 8

def nine():
    return 9

def plus(val1 :int, val2 :int):
    return val1 + val2


def minus(val1 :int, val2 :int):
    return val1 - val2

def times(val1 :int, val2 :int):
    return val1 * val2

def divided_by(val1 :int, val2 :int):
    # TODO: Check val2 == 0
    return val1 // val2


operations = {
    'times': times,
    'plus': plus,
    'minus': minus,
    'divided_by': divided_by,

}

def process(expression: str):
    expression_cleaned = expression.replace('(', ',').replace(')', '').strip()
    function_components = expression_cleaned.split(',')
    function_components.pop(-1)
    if len(function_components) != 3:
        print('Error in expression')
    print(function_components)



def main():
    test = 'four(times(five()))'
    process(test)

if __name__ == '__main__':
    main()