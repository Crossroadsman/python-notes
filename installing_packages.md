Installing Packages
===================

Before you begin
----------------
- Create and activate a virtual environment.
- Make sure the various setup-related packages are up-to-date:
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
`pip install 'SomeProject==1.4'` | install the specified version of the project
`pip install 'SomeProject>=1,<2'` | install a version of the package at least v1 and less than v2


Use Pip to Install Requirements From a Project
----------------------------------------------
Suppose the project supplies two sets of package lists: `requirements.txt` for everything required to run the application and 
`test-requirements.txt` for any incremental packages (e.g., selenium) required for running tests.

```console
(venv) $ pip3 install -r requirements.txt
...
(venv) $ pip3 install -r test-requirements.txt
```

Use Pip to Create a `requirements.txt` File
-------------------------------------------
```console
(venv) $ pip3 freeze > requirements.txt
```




[link01]: https://pypi.python.org/pypi
