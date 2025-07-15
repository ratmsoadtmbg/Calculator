def main():
    #operators = ["+", "-", "*", "x", "/", "reset", "exit"]

    a = int(input("Please enter first number: "))
    op = input("Please enter an operator: ").lower()
    b = int(input("Please enter second number: "))

    match op:
        case "+":
            end = "sum"
            result = a + b
        case "-":
            end = "difference"
            result = a - b
        case "*":
            end = "product"
            result = a * b
        case "x":
            end = "product"
            result = a * b
        case "/":
            end = "quotient"
            result = a / b
        case _:
            raise ValueError('Invalid operator entered.')
    
    print(f"The {end} of the two numbers is {result}!")
    go_again = input('Type "retry" to try another operation, or "exit" to exit the program: ').lower()
    if go_again != "exit" and go_again != "retry":
        go_again = input('Please only type either "retry" or "exit": ')
    if go_again == "retry":
        main()

main()