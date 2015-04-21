import os
from setuptools import setup
 
README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
 
# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
 
setup(
    name = 'athentoimaging',
    version = '0.1',
    packages = ['athentoimaging'],
    install_requires =  [
        'argparse',
        'numpy'
    ],
    include_package_data = True,
    license = 'Athento Shared Source License',
    description = 'Image cleaning and OCR improvement package in Python using OpenCV.',
    long_description = README,
    url = 'http://www.athento.com/',
    author = 'Daniel Ramirez Torres, Jose Luis de la Rosa',
    author_email = 'dramireztorres@gmail.com, jlr@athento.com',
    classifiers =[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
    ]
)
