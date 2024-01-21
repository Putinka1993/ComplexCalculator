class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary


class ComplexCalculator:
    def add(self, num1, num2):
        real = num1.real + num2.real
        imaginary = num1.imaginary + num2.imaginary

        return ComplexNumber(real, imaginary)

    def subtract(self, num1, num2):
        real = num1.real - num2.real
        imaginary = num1.imaginary - num2.imaginary

        return ComplexNumber(real, imaginary)

    def multiply(self, num1, num2):
        real = num1.real * num2.real - num1.imaginary * num2.imaginary
        imaginary = num1.real * num2.imaginary + num2.real * num1.imaginary

        return ComplexNumber(real, imaginary)

    def divide(self, num1, num2):
        denominator = num2.real**2 + num2.imaginary**2
        real = (num1.real * num2.real + num1.imaginary * num2.imaginary) / denominator
        imaginary = (num1.imaginary * num2.real - num1.real * num2.imaginary) / denominator

        return ComplexNumber(real, imaginary)
