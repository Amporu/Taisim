"""
info:This module contains the implememntation of the SparkVerse Simulator
autor: Tucudean Adrian-Ionut
date: 17.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""

import os
from setuptools import setup, find_packages
#from src.tucu.external_data import VERSION
here = os.path.abspath(os.path.dirname(__file__))
#README = open(os.path.join(here, 'README-pypi.rst')).read()



install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
    'requests'	
]


setup(name='tucu',
    version='0.0.1',
    description="Simple python3 simulator for advance driving systems",
    keywords='Simulator computer vision Advanced Driving',
    author='Tucudean Adrian-Ionut',
    author_email='Tucudean.Adrian.Ionut@outlook.com',
    url='https://github.com/Amporu/SparkVerse',
    license='MIT',
    packages=find_packages('src','src/tucu/data'),
    package_dir = {'': 'src'},include_package_data=True,
    package_data={'tucu':['data/*.png',"*.py"]},
    zip_safe=False,
    install_requires=['opencv-python','pygame'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
    'console_scripts': [
        'tucu = tucu:main',
    ],
},
)
