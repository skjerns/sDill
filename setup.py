from setuptools import setup

setup(name='sdill',
      version='0.20',
      description='A Dill wrapper to call dill with file strings',
      url='http://github.com/skjerns/sDill',
      author='skjerns',
      author_email='nomail',
      license='GNU',
      packages=['sdill'],
      install_requires=['dill',],
      zip_safe=False)