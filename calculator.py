
def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(" Only numbers write!")

def calculator():
    print("\n" + "="*35)
    print("      Python Calculator")
    print("="*35)

    while True:
        print("\nOperations:")
        print("  1. Add       (+)")
        print("  2. Subtract  (-)")
        print("  3. Multiply  (*)")
        print("  4. Divide    (/)")
        print("  5. Exit")
        print("-"*35)

        choice = input("Choice (1-5): ").strip()

        if choice == "5":
            print("\nBye! :)")
            break

        if choice not in ("1", "2", "3", "4"):
            print("  Wrong choice! 1-5 type.")
            continue

        a = get_number("Number 1: ")
        b = get_number("Number 2: ")

        ops = {
            "1": ("+", add),
            "2": ("-", subtract),
            "3": ("*", multiply),
            "4": ("/", divide),
        }
        symbol, func = ops[choice]
        result = func(a, b)

        # Clean display
        if isinstance(result, float) and result == int(result):
            result = int(result)

        print(f"\n  {a} {symbol} {b} = {result}")

if __name__ == "__main__":
    calculator()
