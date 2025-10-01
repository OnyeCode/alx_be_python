FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR)

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR)

def main():
    temp = int(input("Enter the temperature to convert: "))
    temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    match temp_type:
        case 'C':
            print(f"{temp}°C is {convert_to_fahrenheit(temp)}")
        case 'F':
            print(f"{temp}°F is {convert_to_celsius(temp)}")
        case _:
            print("invalid temperature specification. Please type in 'C' or 'F', when asked")

if __name__ == "__main__":
    main()
