from setuptools import *
setup(
  name='mypthonlib',
  packages=find_packages(include=['pymath']),
  version='0.1.0',
  author ='SaturnLang',
  license='MIT',
  install_requires = [],
  setup_requires =['pytest-runner'],
  test_require=['pytest=4.4.1'],
  test_suite ='tests',
