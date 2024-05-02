def sumList(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# sample List:
numbers = [9, 2, 3, 5, 8]
result = sumList(numbers)
print("The sum of the numbers in the list is:", result)



def calculate_triangle_area(base, height):
    return 0.5 * base * height

def main():
    try:
        base = float(input("Enter the base of the triangel: "))
        height = float(input("Enter the height of the triangle: "))

        area = calculate_triangle_area(base, height)

        print("The area of the triangle is:", area)
    except ValueError:
        print("Please enter valid numeric values for base and height.")

if __name__ == "__main__":
    main()

def temperatureConversion():
    print('Temperature Converter')
    print('1 Celsius to Fahrenheit')
    print('2 Fahrenheit to Celsius')

    option = int(input('Select your choice (1 or 2): '))

    if option == 1:
        celsius = float(input('Enter temperature in Celsius degrees: '))
        fahrenheit = (9/5 * celsius) + 32
        print(f'{celsius} C is equal to {fahrenheit} F')
    elif option == 2:
        fahrenheit = float(input('Enter temperature in Fahrenheit degrees: '))
        celsius = (5/9 * (fahrenheit - 32))
        print(f'{fahrenheit} F is equal to {celsius} C')
    else:
        print('Invalid option!')

temperatureConversion()


def calculateGrade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "E"
    else:
        return "Fail"

def main():
    percentage = float(input("Enter the student percentage score: "))
    grade = calculateGrade(percentage)

    print("The grade for the student percentage score", percentage, "is:", grade)

if __name__ == "__main__":
    main()