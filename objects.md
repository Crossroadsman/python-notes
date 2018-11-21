Objects
=======

All types in Python are objects.

Illustration:
```python
>>> two = 2
>>> type(two)
<class 'int'>
>>> type( type(two) )
<class 'type'>
>>> type( type( type(two) ))
<class 'type'>
```

Although `type` is of type `type`, it does have a 'base' class of `object` (which is also of type `type`):

```python
>>> t = type( type( type(two) ))  # <class 'type'>
>>> dir(2)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', 
'__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', 
'__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', 
'__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', 
'__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', 
'__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', 
'__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', 
'__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', 
'__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', 
'__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', 
'__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 
'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 
'real', 'to_bytes']
>>> dir(t)  # note that <class 'type'> has the methods __base__ and __bases__
['__abstractmethods__', '__base__', '__bases__', '__basicsize__', '__call__', 
'__class__', '__delattr__', '__dict__', '__dictoffset__', '__dir__', '__doc__', 
'__eq__', '__flags__', '__format__', '__ge__', '__getattribute__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__instancecheck__', 
'__itemsize__', '__le__', '__lt__', '__module__', '__mro__', '__name__', 
'__ne__', '__new__', '__prepare__', '__qualname__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
'__subclasscheck__', '__subclasses__', '__subclasshook__', 
'__text_signature__', '__weakrefoffset__', 'mro']
>>> t.__base__
<class 'object'>
>>> type(t.__base__)
<class 'type'>
>>> dir(t.__base__)  # note that <class 'object'> does not have a __base__
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
'__subclasshook__']
```

Thus `type` is the type of all types; `object` is the base of all types (except 
itself). These are the two primitive objects in Python.

In Python, 'types' and 'classes' are the same thing (at least since Python 2.2).
12345678901234567890123456789012345678901234567890123456789012345678901234567890

See also: [Python Types and Objects (archived)][chaturvedi_01]



[chaturvedi_01]: https://web.archive.org/web/20170805220114/http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html 'Shalabh Chaturvedi: Python Types and Objects (Internet Archive)'
