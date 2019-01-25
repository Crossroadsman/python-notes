Class vs Instance Variables
===========================

Creation
--------
Any variable defined at the class level is a class variable. Variables defined
inside methods (usually, but not necessarily, `__init__`) are instance 
variables.


Differences
-----------
Here are some examples of how class variables behave differently from instance 
variables. In all cases, assume the following classes have been defined:
```python
>>> class C:
...     v = 1
...
>>> class I:
...    def __init__(self):
...        self.v = 1
...
```

### 1: Shared State ###
All instances share state of all class variables.

Changing the value of a class variable will mutate all existing and future 
instances with that class variable.

Example:
```python
>>> c1 = C()
>>> c1.v
1
>>> C.v = 2
>>> c1.v
2
```

Note that setting the variable directly on an instance will turn that variable 
from a class- to an instance- variable for that instance. Thus subsequent 
mutations of the class variable will not affect that instance.

Example:
```python
>>> c1, c2 = C(), C()
>>> c1.v
1
>>> c2.v
1
>>> c1.v = 2
>>> c1.v
2
>>> c2.v
1
>>> C.v = 3
>>> c1.v
2
>>> c2.v
3
```

### 2: Is ###

Example:
```python
>>> c1, c2 = C(), C()
>>> c1.v is c2.v
True
>>> C.v is c1.v
True
>>> i1, i2 = I(), I()
>>> i1.v is i2.v
False
```

### 3: Variable Access ###

You can access a class variable on the class or the instance, you can only 
access an instance variable on the instance.

