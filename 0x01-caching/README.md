# Project Name
**0x01. Caching**

## Resources
**Read or watch**:

-   [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29 "Cache replacement policies - FIFO")
-   [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29 "Cache replacement policies - LIFO")
-   [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29 "Cache replacement policies - LRU")
-   [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29 "Cache replacement policies - MRU")
-   [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29 "Cache replacement policies - LFU")

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
Learn what a caching system is.
What FIFO means.
What LIFO means.
What LRU means.
What MRU means.
What LFU means.
What the purpose of a caching system.
What limits a caching system have.


* **0. Basic dictionary** - Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system with the given requirements. - `0-basic_cache.py`.
* **1. FIFO caching** - Create a class `FIFOCache` that inherits from `BaseCaching` and is a caching system with the given requirements. - `1-fifo_cache.py`.
* **2. LIFO Caching** - Create a class `LIFOCache` that inherits from `BaseCaching` and is a caching system with the given requirements. - `2-lifo_cache.py`.
* **3. LRU Caching** - Create a class `LRUCache` that inherits from `BaseCaching` and is a caching system with the given requirements. - `3-lru_cache.py`.
* **4. MRU Caching** - Create a class `MRUCache` that inherits from `BaseCaching` and is a caching system with the given requirements. - `4-mru_cache.py`.
