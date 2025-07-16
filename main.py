import converter


def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        f = converter.celsius_to_fahrenheit(c)
        print(f"Temperature in Fahrenheit: {f:.2f}")
    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        c = converter.fahrenheit_to_celsius(f)
        print(f"Temperature in Celsius: {c:.2f}")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
