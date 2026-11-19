def add(a1, a2):
    return a1 + a2

def subtract(s1, s2):
    return s1 - s2

def times(t1, t2):
    return t1 * t2

def divide(d1, d2):
    return d1 / d2

try:
    def calculator(num1, num2):
        print("Choose an option")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        operation = int(input(""))

        if operation == 1:
            result = add(num1, num2)
        elif operation == 2:
            result = subtract(num1, num2)
        elif operation == 3:
            result = times(num1, num2)
        elif operation == 4:
            result = divide(num1, num2)
        else:
            print("Please enter one of the operation listed only type 1, 2, 3 or 4.")
            calculator(num1, num2)

        return result

except ValueError:
    print("Please enter a correct number.")
except ZeroDivisionError:
    print("You cannot divide by 0.")

try:
    inp1 = float(input("Please enter the first number. "))
    inp2 = float(input("Please enter the second number. "))
    print(calculator(inp1, inp2))
except ValueError:
    print("Please enter a correct number.")
except ZeroDivisionError:
    print("You cannot divide by 0.")
