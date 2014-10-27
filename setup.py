from setuptools import setup

'''
# local install
python setup.py install

# local developer install 
python setup.py develop 

#registering on PyPI 
python setup.py register 

#create a source distribution 
python setup.py sdist

# upload the source distribution tp PyPI 
python setup.py sdist upload
'''


setup(name='simulator',
      version='0.1',
      description='healthcare agent-based simulator',
      url='http://github.com/ttrikalin/simulator',
      author='TA Trikalinos',
      author_email='thomas_trikalinos@brown.edu',
      license='MIT',
      packages=['simulator'],
      install_requires=[
          'pint', 
          'numpy'
      ],
      zip_safe=False)


