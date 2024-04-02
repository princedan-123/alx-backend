<h3>A tutorial project (0x01. Caching) in ALX backend specialization</h3>
<p>The project has a grade weight of 1 and started Apr 2, 2024 6:00 AM, should end by Apr 4, 2024 6:00 AM
</p>
<h4> Background Context </h4>
<p>In this project, you learn different caching algorithms.</p>

<p>Resources</p>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29">Cache replacement policies - FIFO</a><li>
<li><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29"> Cache replacement policies - LIFO</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29"> Cache replacement policies - LRU</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29"> Cache replacement policies - MRU</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29"> Cache replacement policies - LFU</a></li>
</ul>
<p> Learning Objectives </p>
<ul>
<li>What a caching system is<li>
<li>What FIFO means<li>
<li>What LIFO means<li>
<li>What LRU means<li>
<li>What MRU means<li>
<li>What LFU means<li>
<li>What the purpose of a caching system<li>
<li>What limits a caching system have<li>
</ul>
<h4> Requirements</h4>
<ul>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly #!/usr/bin/env python3</li>
<li>Your code should use the pycodestyle style (version 2.5)</li>
<li>A README.md file, at the root of the folder of the project, is mandatory</li>
<li>All your files must be executable</li>
<li>All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')</li>
<li>All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')</li>
<li>All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')</li>
<li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>
<h4>Parent class BaseCaching </h4>
<p>All your classes must inherit from BaseCaching defined below:</p>
"""
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
"""
<p>TASKS</p>
<ul>
<li>Create a class BasicCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None</li>
<li>Create a class FIFOCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.</li>
<li>Create a class LIFOCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the last item put in cache (LIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.</li>
<li>Create a class LRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least recently used item (LRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.</li>
<li>Create a class MRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the most recently used item (MRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.</li>
</ul>
<p>
Advanced Task
Please ensure you concentrate on the mandatory task before attempting the advanced task
<ul>
<li>Create a class LFUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least frequency used item (LFU algorithm)
if you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.</li>
</ul> 
<p>