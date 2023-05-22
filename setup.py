"""
info:This is a simple example on starting the simulator
autor: Tucudean Adrian-Ionut
date: 19.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
#README = open(os.path.join(here, 'README-pypi.rst')).read()



VERSION = '0.0.3'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
    'requests'	
]


setup(name='sparkverse',
    version=VERSION,
    description="Simple python3 simulator for advance driving systems",

    keywords='Simulator computer vision Advanced Driving',
    author='Tucudean Adrian-Ionut',
    author_email='Tucudean.Adrian.Ionut0@gmail.com',
    url='https://github.com/Amporu/SparkVerse',
    license='MIT',
    packages=find_packages('src','src/sparkverse/data'),
    package_dir = {'': 'src'},include_package_data=True,
    package_data={'sparkverse':['data/*.png']},
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
        'spark-verse = sparkverse:main',
    ],
},
)
