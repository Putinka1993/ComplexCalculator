from UX import ComplexCalculator
from UX import ComplexNumber
class ComplexCalculatorUI:
    def __init__(self, calculator):
        self.calculator = calculator

    def inp_nums(self):
        real1 = float(input("Enter the real part of the FIRST complex number: "))
        imaginary1 = float(input("Enter the imaginary part of the FIRST complex number: "))

        real2 = float(input("Enter the real part of the SECOND complex number: "))
        imaginary2 = float(input("Enter the imaginary part of the SECOND complex number: "))

        num1 = ComplexNumber(real1, imaginary1)
        num2 = ComplexNumber(real2, imaginary2)

        return num1, num2

    def out_display_result(self, result):
        return print(f"The result is {result.real} + {result.imaginary} i.")


