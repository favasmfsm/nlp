from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open('deploy/requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='fsmnlp',
    version='0.1',
    description='A library for plug-and-play NLP tasks',
    author='Favas M',
    author_email='favasmfsm@gmail.com',
    url='https://github.com/favasmfsm/nlp',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Topic :: Text Processing',
    ],
)
