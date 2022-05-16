

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