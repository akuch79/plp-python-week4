import toolbox


def main():
    print("Welcome to the Python Toolbox!")
    name = input("What is your name? ")
    print(toolbox.greet(name))

    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    print(f"\n{x} + {y} = {toolbox.add(x, y)}")
    print(f"{x} - {y} = {toolbox.subtract(x, y)}")
    print(f"{x} * {y} = {toolbox.multiply(x, y)}")

    try:
        print(f"{x} / {y} = {toolbox.divide(x, y)}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
