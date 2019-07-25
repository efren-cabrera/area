from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    readme = f.read()


setup(name='geoarea',
      version="V0.1.2",
      description="Calculate the area from latitude longitude coordinates list",
      long_description_content_type='text/markdown',
      long_description=readme,      
      author="Efren Cabrera",
      author_email="efren@cabrera.dev",
      url='https://github.com/efren-cabrera/geoarea',
      license='BSD-2-Clause',
      packages=['geoarea'],
      include_package_data=True,
      zip_safe=False,
      test_suite="test",
      classifiers=[
          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: GIS',
          'License :: OSI Approved :: BSD License',                   
          'Programming Language :: Python :: 3.7',
      ]
)
