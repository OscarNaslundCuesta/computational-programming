# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 14:27:37 2023

@author: ltuor
"""

class Interval:
    def __init__(self, *args):
        if len(args) == 1:
            self.left = args[0]
            self.right = args[0]
        elif len(args) == 2:
            self.left = args[0]
            self.right = args[1]
        else:
            # Error handling
            pass
        
        
    # Addition
    def __add__(self, other):
        if type(other) != Interval:
            other = Interval(other)
        return Interval(self.left + other.left, self.right + other.right)
    
    def __radd__(self, other):
        return self + other
    
    # Subtraction
    def __sub__(self, other):
        if type(other) != Interval:
            other = Interval(other)
        return Interval(self.left - other.right, self.right - other.left)
    
    def __rsub__(self, other):
        return self - other
    
    # Multiplication
    def __mul__(self, other):
        if type(other) != Interval:
            other = Interval(other)
        return Interval(min(self.left * other.left, self.left * other.right,
                            self.right * other.left, self.right * other.right),
                        max(self.left * other.left, self.left * other.right,
                            self.right * other.left, self.right * other.right))
    
    def __rmul__(self, other):
        return self * other
    
    # Division
    def __truediv__(self, other):
        if type(other) != Interval:
            other = Interval(other)
        return Interval(min(self.left / other.left, self.left / other.right,
                            self.right / other.left, self.right / other.right),
                        max(self.left / other.left, self.left / other.right,
                            self.right / other.left, self.right / other.right))
    
    def __rtruediv__(self, other):
        return self / other
    
    def __pow__(self, n):
        if n%2 == 0:
            if self.left >= 0:
                return Interval(self.left ** n, self.right ** n)
            elif self.right < 0:
                return Interval(self.right ** n, self.left ** n)
            else:
                return Interval(0, max(self.left ** n, self.right ** n))
        else:
            return Interval(self.left ** n, self.right ** n)
    
    def __neg__(self):
        return self * -1
    
    # Called when the 'in' keyword is used
    def __contains__(self, val):
        return(val >= self.left and val <= self.right)
    
    # String output
    def __str__(self):
        return f"[{self.left}, {self.right}]"
    
    # Define how the object is represented in console output
    def __repr__(self):
        return str(self)
    