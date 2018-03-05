Installing Packages
===================

Before you begin
----------------
- Create and activate a virtual environment.
- Make sure the various setup-releated packages are up-to-date:
  ```
  python -m pip install --upgrade pip setuptools wheel
  ```

Use Pip to Install From PyPI
----------------------------
Note, PyPI is the [Python Package Index][link01]

Here are some examples of ways to install packages using Pip:

command | result
--------|----------
`pip install 'SomeProject'` | install the latest version of 'SomeProject'
`pip install 'SomeProject==1.4' | install the specified version of the project
'pip install 'SomeProject>=1,<2' | install a version of the package at least v1 and less than v2







[link01]: https://pypi.python.org/pypi
