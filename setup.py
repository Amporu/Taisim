from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
#README = open(os.path.join(here, 'README-pypi.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '1.0.3'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
    'requests'	
]


setup(name='sparkverse',
    version=version,
    description="Simple python3 simulator for advance driving systems",
    long_description= NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='wrapper api spacex',
    author='Tucudean Adrian-Ionut',
    author_email='phadnisvinay30@gmail.com',
    url='https://github.com/phadnisvinay30/SpaceX-Python',
    license='MIT',
    packages=find_packages('src','data'),
    package_dir = {'': 'src'},include_package_data=True,
    package_data={'sparkverse':['data/*.png',"salut.txt"]},
    zip_safe=False,
    install_requires=install_requires,
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
