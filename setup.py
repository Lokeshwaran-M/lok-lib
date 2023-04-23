from setuptools import setup, find_packages

setup(
    name='loklib',
    version='0.1',
    description='A library to power an AI voice-controlled digital assistant',
    author='Lokeshwaran M',
    author_email='lokeshwaran.m23072003@gmail.com',
    url="https://github.com/Lokeshwaran-M/lok-lib",
    license="MIT",
    packages=find_packages(),
    install_requires=open('requirements.txt').readlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='loklib library',
)
