#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1

    if len(sys.argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    first_arg = int(sys.argv[1])
    sec_arg = int(sys.argv[3])

    if sys.argv[2] == "+":
        operation1 = calculator_1.add(first_arg, sec_arg)
        print("{} + {} = {}".format(first_arg, sec_arg, operation))
    
    elif sys.argv[2] == "-":
        operation2 = calculator_1.sub(first_arg, sec_arg)
        print("{} - {} = {}".format(first_arg, sec_arg, operation))

    elif sys.argv[2] == "*":
        operation3 = calculator_1.mul(first_arg, sec_arg)
        print("{} * {} = {}".format(first_arg, sec_arg, operation))
    
    elif sys.argv[2] == "/":
        operation4 = calculator_1.div(first_arg, sec_arg)
        print("{} / {} = {}".format(first_arg, sec_arg, operation))
    
    else:
        print("Unknown operator. Available operators: +, -, * and /")
