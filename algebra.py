#coding: utf-8
#imports


#fraction class
class fraction():
    def __init__(self, numerator = 1, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator

    def setNumerator(self, value):
        self.numerator = value

    def numerator(self):
        return self.numerator

    def setDenominator(self, value):
        self.denominator = value

    def denominator(self):
        return self.denominator