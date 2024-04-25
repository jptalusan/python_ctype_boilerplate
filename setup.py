from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import os
import platform

# Define the name of the C library
library_name = "mylib"
py_folder = "python"

# C++ extension modules
ext_modules = [
    Extension(
        "mylib",  # Module name in Python
        sources=["src/mylib.cpp"],  # Source files
        include_dirs=["include"],  # Include directories
        language="c++",  # Language is C++
    ),
    Extension(
        "myclass",  # Module name in Python
        sources=["src/myclass.cpp"],  # Source files
        include_dirs=["include"],  # Include directories
        language="c++",  # Language is C++
    ),
]


# Custom build_ext to ensure C++ standards are set properly
class BuildExt(build_ext):
    def build_extensions(self):
        # If you use C++11 or later features, you need to add the flag here,
        # for example with C++11 you can uncomment the following line:
        # self.compiler.compiler_so.append('-std=c++11')

        build_ext.build_extensions(self)


setup(
    name=library_name,
    version="1.0",
    description="A package with C++ extensions",
    ext_modules=ext_modules,
    cmdclass={
        "build_ext": BuildExt,
    },
    py_modules=["use_mylib"],
    package_dir={"": py_folder},
)

# # Define the extension module
# extension_mod = Extension("mylib", sources=["src/mylib.c"], include_dirs=["include"])

# setup(
#     name=library_name,
#     version="1.0",
#     description="Python package with C extension",
#     ext_modules=[extension_mod],
#     package_dir={"": py_folder},
#     py_modules=["use_mylib"],
# )
