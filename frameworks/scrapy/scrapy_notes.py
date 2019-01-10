"""scrapy_notes.py

Examples of using the scrapy library

Links
-----
homepage: https://scrapy.org
documentation: https://docs.scrapy.org/en/latest/

Installation
------------
```console
(venv) $ pip3 install scrapy
```

Usage
------

You can write a scrapy project from scratch (see the example at:
https://docs.scrapy.org/en/latest/intro/overview.html#walk-through-of-an-example-spider
). Or you can tell scrapy to create a template project:
```
(venv) $ scrapy startproject MySpider    
```

(Note, you can optionally supply a destination path. If none specified, it will
use the project name as the path inside the current directory)

A template project is initialised with the following files:
```
MySpider
├── MySpider
│   ├── __init__.py
│   ├── __pycache__
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
│       └── __pycache__
└── scrapy.cfg
```

Files:
- `scrapy.cfg` : deployment configuration
- `items.py` : custom data models
- `pipelines.py` : custom data cleaning/processing
- `spiders/` : the directory where we save our spiders

scrapy outputs Python dicts. We can use `items.py` to build custom data 
structures that provide a better, structured representation of the data in
the dicts.
"""
