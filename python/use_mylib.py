from ctypes import cdll, c_int
import glob

# Load the shared library
# find the shared library, the path depends on the platform and Python version
libfile = glob.glob("./build/*/mylib*.so")[0]

# 1. open the shared library
lib = cdll.LoadLibrary(libfile)

# lib = cdll.LoadLibrary("../build/mylib.so")

# Set the return type of the add function
lib.add.restype = c_int

# Set the argument types of the add function
lib.add.argtypes = [c_int, c_int]

# Call the C function add from Python
result = lib.add(3, 4)
print("The result of 3 + 4 is:", result)


#### CLASS

from ctypes import cdll, c_int, POINTER

libfile = glob.glob("./build/*/myclass*.so")[0]

# Load the shared library
lib = cdll.LoadLibrary(libfile)

# Define the C wrapper function prototypes
lib.MyClass_new.argtypes = [c_int]
lib.MyClass_new.restype = POINTER(c_int)

lib.MyClass_add.argtypes = [POINTER(c_int), c_int]
lib.MyClass_add.restype = None

lib.MyClass_get.argtypes = [POINTER(c_int)]
lib.MyClass_get.restype = c_int

lib.MyClass_delete.argtypes = [POINTER(c_int)]
lib.MyClass_delete.restype = None

# Use the C++ class from Python
obj = lib.MyClass_new(10)
lib.MyClass_add(obj, 5)
result = lib.MyClass_get(obj)
print("The result is:", result)

# Clean up and delete the object
lib.MyClass_delete(obj)
