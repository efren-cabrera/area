from codecs import open as codecs_open
from setuptools import setup

with codecs_open('README.rst', encoding='utf-8') as f:
    readme = f.read()
    
setup(name='geoarea',
      version=version,
      description="Calculate the area from latitude longitude coordinates list",
      long_description=readme,           
      url='https://github.com/efren-cabrera/geoarea',
      license='BSD-2-Clause',
      packages=['area'],
      include_package_data=True,
      zip_safe=False,
      test_suite="test",
      classifiers=[
          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: GIS',
          'License :: OSI Approved :: BSD License',
          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.          
          'Programming Language :: Python :: 3.7',
      ],
      )
