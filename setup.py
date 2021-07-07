from setuptools import setup

# Testing webhook 24. 

def readme():
    with open('README.rst') as f:
        return f.read()

setup(  name='soundmixture',
        version='0.1',
        description='generating mixture of noise and non-noise sound files',
        url='https://github.com/aakazemaa',
        author='Kazem Ardekanian',
        author_email='kazem.ardekanian@gmail.com',
        license='MIT',
        packages=['soundmixture'],
        install_requires=[
          'pydub',
          'scipy',
          
      ],
        zip_safe=False)


