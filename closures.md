Closures
========

Reminder: What Closures Are
---------------------------
TODO

Closures in Python
------------------
TODO

Common Gotchas
--------------
Consider the following:
```python
>>> def outer():
...     n = 0
...     def inner():
...         n += 1
...         return n
...     return inner()
...
>>> counter = outer()
>>> counter()  # We might be expecting 1
Traceback (most recent call last):
...
UnboundLocalError: local variable 'n' referenced before assignment
```

You could be forgiven for thinking, "Aren't nested functions supposed to be 
closures? Why can't `inner()` see `n` in `outer()`?"

Yes, nested functions are closures, but this is not the reason why `inner()` is
raising.

The reason is the general rule in Python functions that:
- An attempt to mutate a shared reference on an immutable object will trigger
  Python to assume we are instantiating a new local variable.
- Since the new local variable had no previous value, we cannot add one to it,
  so we get the UnboundLocalError.

We can prove that the inner function can, indeed, see the outer variable 
as follows:

```python
>>> def outer():
...     n = 0
...     def inner():
...         return n
...     return inner
...
>>> counter = outer()
>>> counter()
0
```

This may not be very useful, but at least we can see that inner is closing over
the variables in outer.

Now let's illustrate by recreating the original example with a mutable value in
outer:

```python
>>> def outer():
...     n = [0]
...     def inner():
...         n[0] += 1
...         return n[0]
...     return inner
...
>>> counter = outer()
>>> counter()
1
>>> counter()
2
>>> counter()
3
```

Finally, let's recreate the original function by expressly telling Python not 
to create a local variable:

```python
>>> def outer():
...     n = 0
...     def inner():
...         nonlocal n
...         n += 1
...         return n
...     return inner
...
>>> counter = outer()
>>> counter()
1
>>> counter()
2
>>> counter()
3
```
