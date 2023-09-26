from setuptools import setup, find_packages


with open("README.rst", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name='theatre-cli',
    version='0.1.4',
    description='A command-line interface to play movies',
    long_description=long_description,
    author='SNG Viraj Reddy',
    author_email='vir200319@gmail.com',
    url='https://github.com/virajsazzala/theatre-cli',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    scripts=['scripts/theatre-cli'],  # Add this line
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
    ],
)
