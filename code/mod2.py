import unittest

class Mod2Error(Exception):
    """ An exception class for Mod2 """
    pass

class Mod2(object):
    """ An element {0, 1} under mod 2 addition
    and multiplication"""
    
    def __init__(self, v):
        self.value = int(v) % 2
        
    def __str__(self):
        return str(self.value)

    def __eq__(self, e):
        """ Test equality """
        return (self.value == e.value)
        
    def __add__(self, e):
        """ Add a Mod2 element to this Mod2 element
        and return a new Mod2 element, but don't change
        this element's value."""
        return Mod2(self.value + e.value)
        
    def __radd__(self, e):
        return Mod2(e.value + self.value)
        
    def __mul__(self, e):
        """ Multiply this Mod2 element with another
        Mod2 and return a third Mod2."""
        return Mod2(self.value * e.value)
    
class Mod2Tests(unittest.TestCase):

    def testAdd(self):
        x1 = [Mod2(0), Mod2(0), Mod2(1), Mod2(1)]
        x2 = [Mod2(0), Mod2(1), Mod2(0), Mod2(1)]
        x3 = [pair[0] + pair[1] for pair in zip(x1, x2)]
        self.assertTrue(x3 == [Mod2(0), Mod2(1), Mod2(1), Mod2(0)])

    def testMult(self):        
        x1 = [Mod2(0), Mod2(0), Mod2(1), Mod2(1)]
        x2 = [Mod2(0), Mod2(1), Mod2(0), Mod2(1)]
        x3 = [pair[0] * pair[1] for pair in zip(x1, x2)]
        self.assertTrue(x3 == [Mod2(0), Mod2(0), Mod2(0), Mod2(1)])

if __name__ == "__main__":
    unittest.main()

