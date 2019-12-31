import setuptools


with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='skrrt',
    version='0.0.1',
    author='aachick',
    description='skrrt is a package designed to play audio files during the execution of other routines',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aachick/skrrt',
    package_data=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.5'
)
