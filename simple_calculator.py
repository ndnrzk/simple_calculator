# sequence
# conditional
# looping

# start of the calculator function
def calculator():
    first_number = input("First Number: ")
    second_number = input("Second Number: ")
    operation = input("Your operation: ")
    result = None
    if operation == "+":
        result = int(first_number) + int(second_number)
    if operation == "-":
        result = int (first_number) - int (second_number)
    print(first_number + " " + operation + " " + second_number + " = " + str(result))

calculator()