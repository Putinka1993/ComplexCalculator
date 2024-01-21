
from UX import ComplexCalculator
from UI import ComplexCalculatorUI


def main():
    calculator = ComplexCalculator()
    ui = ComplexCalculatorUI(calculator)

    operation = input("Choose an operation ( + - * / ): ")
    if operation in ["+", "-", "*", "/"]:
        num1, num2 = ComplexCalculatorUI.inp_nums()
        if operation == "+":
            result = calculator.add(num1, num2)
        elif operation == "-":
            result = calculator.subtract(num1, num2)
        elif operation == "*":
            result = calculator.multiply(num1, num2)
        elif operation == "/":
            result = calculator.divide(num1, num2)

        ui.out_display_result(result)

    else:
        print("Invalid operation")