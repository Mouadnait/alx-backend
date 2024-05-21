# Project Name
**0x00. Pagination**

## Resources
**Read or watch:**

-   [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination "REST API Design: Pagination")
-   [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS "HATEOAS")

##  Requirements

### Python Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using gcc, using python3 (version 3.8.5).
*   All your files should end with a new line.
*   The `main.py` files are used to test your functions, but you don’t have to push them to your repo.
*   The first line of all your files should be exactly `#!/usr/bin/env python3`.
*   Your code should use the pycodestyle (version `2.8.*`).
*   All your files must be executable.
*   The length of your files will be tested using `wc`.
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)`' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified).
*   All your functions and coroutines must be type-annotated.

## Project Description
Learn how to paginate a dataset with simple page and page_size parameters.
How to paginate a dataset with hypermedia metadata.
How to paginate in a deletion-resilient manner.


* **0. Basic annotations - add** - Write a function named `index_range` that takes two integer arguments `page` and `page_size`. - `0-simple_helper_function.py`.
* **1. Basic annotations - concat** - Implement a method named `get_page` that takes two integer arguments `page` with default value 1 and `page_size` with default value 10. - `1-simple_pagination.py`.
* **2. Hypermedia pagination** - Implement a `get_hyper` method that takes the same arguments (and defaults) as `get_page` and returns a dictionary containing the given key-value pairs. - `2-hypermedia_pagination.py`.
* **3. Deletion-resilient hypermedia pagination** - Implement a `get_hyper_index` method with two integer arguments: `index` with a `None` default value and `page_size` with default value of 10. - `3-hypermedia_del_pagination.py`.
