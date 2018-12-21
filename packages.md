Packages
========

A package is defined by the existence of an __init__.py file in directory.

In the simplest case, it can be just an empty file, but it can also execute initialization code for the package or set the `__all__` variable.

You can define any variable at the package level. Doing this is convenient if a package defines something that will be imported frequently, in an API-like fashion.

[Example](https://stackoverflow.com/a/18979314):

__init__.py:

```python
import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(os.environ['DATABASE_URL'])
Session = sessionmaker(bind=engine)
```

Then from any module in the package:

example_module.py:
```python
from my_package import Session
session = Session()
```

