from setuptools import setup, find_packages

setup(
    name='theatre-cli',
    version='1.0.0',
    description='A command-line interface to play movies',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/theatre-cli',
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
