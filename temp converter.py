def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    print("Welcome to Temperature Converter!")
    
    while True:
        choice = input("Choose an option:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Quit\n")
        
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f}°F\n")
        
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius:.2f}°C\n")
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    temperature_converter()
