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

See also: [Python Types and Objects (archived)][chaturvedi_01]

From the [Python docs][python_01] on mutability:
> Some objects contain references to other objects; these are called 
> *containers*. Examples of containers are tuples, lists and dictionaries. The
> references are part of a container's value. In most cases, when we talk about
> the value of a container, we imply the values, not the identities of the
> contained objects; however, when we talk about the mutability of a container,
> only the identities of the immediately contained objects are implied. So, if
> an immutable container (like a tuple) contains a reference to a mutable 
> object, its value changes if that mutable object is changed.

From the [Python docs][python_01] on types:
> Types affect almost all aspects of object behaviour. Even the importance of 
> object identity is affected in some sense: for immutable types, operations
> that compute new values may actually return a reference to any existing object
> with the same type and value, while for mutable objects this is not allowed.
> E.g., after `a = 1; b = 1`, `a` or `b` may or may not refer to the same object
> with the value one, depending on the \[Python] implementation, but after
> `c = []; d = []`, `c` and `d` are guaranteed to refer to two different, 
> unique, newly created empty lists. (Note that `c = d = []` assigns the same
> object to both `c` and `d`. **\[ASK: This is equivalent to `d = []; c = d`]**)

Names
-----
From [Lundh: Python Objects][lundh_01]:

> \[N]ames are a bit different — they’re not really properties of the object, 
> and the object itself doesn’t know what it’s called.
> 
> An object can have any number of names, or no name at all.
> 
> Names live in *namespaces* (such as a module namespace, an instance namespace,
> a function’s local namespace).
> 
> Namespaces are collections of (name, object reference) pairs (implemented 
> using dictionaries).
> 
> When you call a function or a method, its namespace is initialized with the 
> arguments you call it with (the names are taken from the function’s argument 
> list, the objects are those you pass in).
> 
> Assignment statements modify namespaces, not objects.
> 
> In other words,
> 
> ```python
> name = 10
> ```
> 
> means that you’re adding the name “name” to your local namespace, and making 
> it refer to an integer object containing the value 10.
> 
> If the name is already present, the assignment replaces the original name:
> 
> ```python
> name = 10
> name = 20
> ```
> 
> means that you’re first adding the name “name” to the local namespace, and 
> making it refer to an integer object containing the value 10. You’re then 
> replacing the name, making it point to an integer object containing the 
> value 20.

From the [Python Docs][python_03] on names and namespaces:
> ### A Word About Names and Objects ###
> Objects have individuality, and multiple names (in multiple scopes) can be
> bound to the same object. This is known as aliasing in other languages. This
> is usually not appreciated on a first glance at Python, and can be safely
> ignored when dealing with immutable basic types (numbers, strings, tuples).
> However, aliasing has a possibly surprising effect on the semantics of Python
> code involving mutable objects such as lists, dictionaries, and most other 
> types. This is usually used to the benefit of the program, sicne aliases
> behave like pointers in some respects. For example, passing an object is cheap
> since only a pointer is passed by the implementation; and if a function 
> modifies an object passed in as an argument, the caller will see the change —
> this eliminates the need for two different argument passing mechanisms as 
> in Pascal.
>
> ### Python Scopes and Namespaces
> 
> ...
> 
> A *namespace* is a mapping from names to objects. Most namespaces are 
> currently implemented as Python dictionaries, but that's not normally 
> noticeable in any way (except for performance), and it may change in the 
> future. Examples of namespaces are:
> - the set of built-in names (containing functions such as `abs()`, and
>   built-in exception names);
> - the global names in a module; and
> - the local names in a function invocation.
> In a sense the set of attributes of an object also form a namespace.
> 
> ...
> 
> Namespaces are created at different moments and have different lifetimes. The
> namespace containing the built-in names is created when the Python interpreter
> starts up, and is never deleted. The global namespace for a module if created
> when the module definition is read in; normally, module namespaces also last
> until the interpreter quits. The statements executed by the top-level 
> invocation of the interpreter, either read from a script file or 
> interactively, are considered part of a module called `__main__`, so they have
> their own global namespace.
> 
> ...
> 
> Although scores are determined statically, they are used dynamically. At any
> time during execution, there are at least three nested scopes whose namespaces
> are directly accessible:
> - the innermost scope, which is searched first, contains the local names;
> - the scopes of any enclosing functions, which are searched starting with the
>   nearest enclosing scope, contains non-local, but also non-global names;
> - the next-to-last scope contains the current module's global names;
> - the outermost scope (searched last) is the namespace containing built-in 
>   names.
> 
> ...
> 
> A special quirk of Python is that - if no `global` statement is in effect - 
> assignments to names always go into the innermost scope. Assignments do not
> copy data — they just bind names to objects.

Call by Sharing (aka Call by Object)
------------------------------------
Python uses the call by sharing evaluation strategy pioneered in CLU, and
extensively described by Barbara Liskov (the project head).

From [Lundh: Call By Object][lundh_02]:

> Python’s model is neither “call by value” nor “call by reference”.
> The most accurate description is CLU’s “call by object” or “call by sharing”.
> Or, if you prefer, “call by object reference”.

From [Liskov et al.: Abstraction Mechanisms in CLU][liskov_01]:
> 3.1 Objects and Variables
> 
> The basic elements of CLU semantics are *objects* and *variables*. Objects are
> the data entities that are created and manipulated by CLU programs. Variables
> are just the names used in a program to refer to objects.
> 
> ...
> 
> An object may *refer* to objects. For example, a record object refers to the 
> objects that are the components of the record. This notion is one of logical,
> not physical, containment. In particular, it is possible for two distinct
> record objects to refer to (or *share*) the same component object. In the case
> of a cyclic structure, it is even possible to have recursive data structure
> definitions and shared data objects without explicit reference types.
> 
> ...
> 
> An object may exhibit time-varying behaviour. Such an object, called a 
> *mutable* object, has a state which may be modified by certain operations
> without changing the identity of the object.
> 
> ...
> 
> If a mutable object *m* is shared by two other objects *x* and *y*, then a 
> modification made to *m* made via *x* will be visible when *m* is examined
> via *y*.
>
> Objects that do not exhibit time-varying behaviour are called *immutable*
> objects, or *constants*. Examples of constants are integers, booleans,
> characters, and strings. The value of a constant object can not be modified.
> For example, new strings may be computed from old ones, but existing strings
> do not change.
> 
> ...
> 
> Variables are names used in CLU programs to *denote* particular objects at
> execution time. Unlike variables in many common programming languages, which
> *are* objects that *contain* values, CLU variables are simply names that the
> programmer uses to refer to objects. As such, it is possible for two variables
> to denote (or *share*) the same object. CLU variables are much like those in
> Lisp and are similar to pointer variables in other languages. However, CLU
> variables are *not* objects; they cannot be denoted by other variables or
> referred to by objects. Thus variables are completely private to the procedure
> in which they are declared and cannot be accessed or modified by any other 
> procedure.
> 
> 3.2 Assignment and Procedure Invocation
> The basic actions in CLU are *assignment* and *procedure invocation*. The
> assignment primitive:
> ```clu
> x := E
> ```
> where `x` is a variable and `E` is an expression, causes `x` to denote the 
> object resulting from the evaluation of `E`. For example, if `E` is a simple
> variable `y`, then the assignment:
> ```clu
> x := y
> ```
> causes `x` to denote the object denoted by `y`. The object is *not* copied; 
> after assignment is performed, it will be *shared* by `x` and `y`. Assignment
> does not affect the state of any object.
> 
> ...
> 
> Procedure invocation involves passing argument objects from the caller to the
> called procedure and returning result objects from the procedure to 
> the caller. The formal arguments of a procedure are considered to be local
> variables of the procedure and are initialized, by assignment, to the objects
> resulting from the evaluation of the argument expressions. Thus argument 
> objects are shared between the caller and the called procedure. A procedure
> may modify mutable argument objects (e.g., records), but of course it cannot
> modify immutable ones (e.g., integers). A procedure has no access to the 
> variables of its caller.

From the [CLU Reference Manual][clu_01]:
> We call the argument passing techique *call by sharing*, because the argument
> objects are shared between the caller and the called routine. The technique
> does not correspond to most traditional argument passing techniques (it is
> similar to argument passing in LISP). In particular it is not call by value
> because mutations of arguments performed by the called routine will be
> visible to the caller. And it is not call by reference because access is not
> given to the variables of the caller, but merely certain objects.

From [Liskov: A History of CLU][liskov_02]:
> CLU looks like an Algol-like language, but its semantics is like that of Lsip:
> CLU objects reside in an object universe (or heap), and a variable just 
> identifies (or refers to) an object. We decided early on to have objects in 
> the heap, although we had numerous discussions about the cost of garbage
> collection.
> 
> ...
> 
> A language that allocates objects only on the stack is not sufficiently
> expressive; the heap is needed for objects whose sizes must change and for
> objects whose lifetime exceeds that of the procedure that creates them.
> 
> ...
> 
> Therefore, the choice is: just heap, or both.
> 
> Here are the reasons why we chose the heap approach...:
> 1. Declarations are simple to process when objects are on the heap: the
>    compiler just allocates space for a pointer. ...
> 2. The heap approach allows us to separate variable and object creation:
>    variables are created by declarations, while objects are created explicitly
>    by calling an operation. ...
> 3. The heap approach allows variable and object lifetimes to be different;
>    with the stack approach they must be the same. ...
> 4. Assignment has a type-independent meaning with the heap approach;
>    ```clu
>    x := e
>    ```
>    causes `x` to refer to the object obtained by evaluating expression `e`.
>    With the stack approach, evaluating an expression produces a value that
>    must be copied into the assigned variable.
> 
> ...
> 
> CLU procedures do not share variables at all. In addition to there being no 
> free variables, there is no call-by-reference. Instead arguments are passed
> "by object"; the (pointer to the) object resulting from evaluating the actual
> argument expression is assigned to the formal. (Thus passing a parameter is
> just doing an assignment to the formal.) Similarly, a pointer to a result 
> object is returned to the caller.
> 
> A CLU procedure can have side effects only if the argument objects can be 
> modified (since it cannot access the caller's variables **\[ASK: and there are
> no global variables]**). This led us to the concept of "mutable" objects. Every
> CLU object has a state. The states of some objects, such as integers and 
> strings, cannot change; these objects are "immutable". Mutable objects (e.g., 
> records and arrays) can have a succession of states.
>
> ...
> 
> CLU assignment causes sharing: after executing `x := y`, variables `x` and `y`
> both refer to the same object. If this object is immutable, programs cannot 
> detect the sharing, but they can if the shared object is mutable, since a 
> modification made via one variable will be visible via the other one. People
> sometimes argue that sharing of mutable objects makes reasoning about programs
> more difficult. This has not been our experience in using CLU. I believe this
> is true in large part because we do not manipulate pointers explicitly.
> Pointer manipulation is clearly both a nuisance and a source of errors in 
> other languages.
> The cost of using the heap is greatly reduced by keeping small immutable
> objects of built-in types, such as integers and booleans, directly in the
> variables that refer to them. These objects fit in the variables (they are no
> bigger than pointers) and storing them there is safe since they are immutable:
> Even though in this case assignment does a copy of the object, no program can
> detect it.

See also:
- [Stack Overflow: succinct answer](https://stackoverflow.com/a/8140747)
- [Stack Overflow: longer answer](https://stackoverflow.com/a/986145)
- [Python Docs: Data Model: Objects, values and types][python_01]
- [Python Docs: FAQ: How do I write a function with output parameters (call 
  by reference)][python_02]
- [A couple of examples of mutability-related gotchas](https://python-docs.readthedocs.io/en/latest/writing/gotchas.html)




[chaturvedi_01]: https://web.archive.org/web/20170805220114/http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html 'Shalabh Chaturvedi: Python Types and Objects (Internet Archive)'
[clu_01]: https://web.archive.org/web/20161204101433/http://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TR-225.pdf 'CLU Reference Manual (Internet Archive)'
[liskov_01]: https://web.archive.org/web/20070613194110/http://www.cs.berkeley.edu/~jcondit/pl-prelim/liskov77clu.pdf 'Liskov et al.: Abstraction Mechanisms in CLU (Internet Archive)'
[liskov_02]: https://web.archive.org/web/20171026085616/http://publications.csail.mit.edu:80/lcs/pubs/pdf/MIT-LCS-TR-561.pdf 'Liskov: A History of CLU (Internet Archive)'
[lundh_01]: http://effbot.org/zone/python-objects.htm 'Fredrik Lundh: Python Objects'
[lundh_02]: http://effbot.org/zone/call-by-object.htm 'Fredrik Lundh: Call By Objects'
[python_01]: https://docs.python.org/3/reference/datamodel.html#objects-values-and-types 'Python: Data Model: Objects, values and types'
[python_02]: https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference 'Python Programming FAQ: How do I write a function with output parameters (call by reference)'
[python_03]: https://docs.python.org/3/tutorial/classes.html#a-word-about-names-and-objects 'Python: Tutorial: Classes: A Word About names and Objects'
