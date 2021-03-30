#coding: utf-8

#imports


#fraction class
class fraction():
    def __init__(self, numerator = 1, denominator = 1):
        self.numeratorValue = numerator
        self.denominatorValue = denominator

    def setNumerator(self, value):
        self.numeratorValue = value

    def setDenominator(self, value):
        self.denominatorValue = value

    def decimalApproximation(self):
        return float(self.numeratorValue)/float(self.denominatorValue)

