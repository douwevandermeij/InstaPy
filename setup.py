from setuptools import setup, find_packages

__version__ = '0.0.1'
__author__ = 'Tim Grossmann'

REQUIREMENTS = (
    'selenium==2.53.6',
    'clarifai==2.0.32',
    'pyvirtualdisplay',
    'emoji'
)

DESCRIPTION = 'Instagram Like, Comment and Follow Automation Script'

setup(
    name='instagram_py',
    version=__version__,
    author=__author__,
    author_email='contact.timgrossmann@gmail.com',
    url='https://github.com/timgrossmann/InstaPy',
    py_modules='instapy',
    packages=['instapy'],
    include_package_data=True,
    description=DESCRIPTION,
    install_requires=REQUIREMENTS,
)
