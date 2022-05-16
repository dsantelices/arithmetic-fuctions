import sys


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


def plus(val1: int, val2: int):
    return val1 + val2


def minus(val1: int, val2: int):
    return val1 - val2


def times(val1: int, val2: int):
    return val1 * val2


def divided_by(val1: int, val2: int):
    if val2 == 0:
        raise Exception('Error: divide by zero')
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

    # Guard condition for malformed input
    if len(function_components) != 3:
        print('Error in expression')

    # Get values from list and use to call as function. Use global because structure restriction in test statement
    str_value1 = function_components[0]
    str_value2 = function_components[2]
    val1 = globals()[str_value1]()
    val2 = globals()[str_value2]()

    # Get operation and call using dictionary to map strings to operation functions
    operation = function_components[1]
    result = operations[operation](val1, val2)

    return result


def main():
    if len(sys.argv) < 2:
        print('Missing input parameter')
        return

    expression = sys.argv[1]
    result = process(expression)
    print(result)


if __name__ == '__main__':
    main()
