Tips
====

Always start with a module-level docstring to describe the 'elevator pitch' for what the module is supposed to do.

Then, before writing any code, add a class-level docstring.

Hettinger: ["Init isn't a constructor. It's[sic] job is to initialize the instance variables"](https://youtu.be/HTLu2DFOdTg?t=447)


Features of Python Classes
--------------------------

Example class:

```python
"""Circuitous: Advanced Circle Stuff"""
import math


class Circle():
    """An advanced circle analytic toolkit
    
    If this class might be deployed in a Python 2 environment, inherit from
    `object`. Modern (Python 3) classes have all the `object` features built-in
    """
  
    # class variables
    # ---------------
    version = '0.5b'
    __perimeter = perimeter
  
  
    # properties
    # ----------
    """These convert dotted access to method calls. Put another way, they
    enable us to transparently replace attribute access with method access
    """
    @property
    def radius(self):
        """Radius of a circle.
        
        Another government mandate, this time (fictional) ISO 22220 
        requires that circles store their internal representations using
        diameters instead of radii
        """
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0
    
    
    # alternative constructors
    # ------------------------
    @classmethod
    def from_bbd(cls, bbd):
        """Construct a circle from a bounding box diagonal
        
        It is common for alternative constructors to be named 'from_<x>'
        
        Note that the `cls` parameter gives us access to the particular
        class. This allows us to return an instance of whatever class
        called the constructor and not just the base class (as would
        be the case if we returned `Circle(radius)`.
        """
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)


    # static methods
    # --------------
    """The purpose of static methods is to attach functions (i.e., methods
    that don't need any values from `self` or `cls`) to classes
    """
    @staticmethod
    def angle_to_grade(angle):
        """Convert a specified angle in degrees to a percentage grade.
        
        This is provided as a static method on Circle rather than a regular 
        function because this provides the context for where this trigonometry
        will work (i.e., it works for circles, not for spheres).
        
        It also enhances discoverability, as users know to find Circle-related
        functionality in the Circle class.
        """
        return math.tan(math.radians(angle)) * 100.0


    # methods
    # -------
    def __init__(self, radius):
        """The only job of `init` is to initialize the instance variables"""
        self.radius = radius
        
    ## replaced by new version below.
    #def area(self):
    #    """Perform quadrature on a shape of uniform radius"""
    #    return math.pi * self.radius ** 2.0

    def area(self):
        """Determine area using mandated (fictional) ISO-11110 formula.
        
        On the face of it, this looks innocuous enough, but this breaks
        subclasses that have overridden or extended `perimeter()`, as
        with the Tire subclass.
        
        One way we can avoid this is to create a copy of the base
        perimeter method and use that in this method.
        
        However, this is pretty wasteful, carrying an extra copy of methods
        just in case someone subclasses our base class. It's also dangerous
        because just creating the copy invites subclasses to override or
        extend the copy, too.
        
        Python's solution to this is the double underscore method which
        automatically associates the method with the current class's
        copy ('class-local reference': ensure that `self` just refers to 
        self rather than self + children).
        
        For more explanation, see:
        https://docs.python.org/3/tutorial/classes.html#private-variables
        
        and specifically, Python's use of 'name mangling'.
        """
        p = self.__perimeter()
        r = p / math.pi / 2.0
        return math.pi * r ** 2.0

    def perimeter(self):
        """Compute the perimeter of the circle"""
        return 2.0 * math.pi * self.radius
        

class Tire(Circle):
    """Tires are circles with a corrected perimeter"""
    
    def perimeter(self):
        """circumference corrected for the rubber.
        
        Because we access the parent's `perimeter` method, we are 'extending'
        the method. If we didn't access the parent's method, would be 
        'overriding'.
        """
        return Circle.perimeter(self) * 1.25

    # note, the following doesn't break `area()` because of name mangling
    # (internally, python redefines a `__variable` as 
    # `_<CurrentClass>__variable` which means that Circle's `__perimeter`
    # becomes `_Circle__perimeter` and the following line gets redefined
    # to `_Tire__perimeter`
    __perimeter = perimeter
```


