from distutils.core import setup
from distutils.extension import Extension

setup(name="PackageName",
    ext_modules=[
      Extension("goodbye", ["goodbyemodule.cpp"],
        libraries = ["boost_python"]
    ])
