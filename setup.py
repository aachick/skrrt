import os
import setuptools


with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='skrrt',
    version='1.0.0a1',
    author='aachick',
    description='skrrt is a package designed to play audio files during the execution of other routines',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aachick/skrrt',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3',
    data_files=[
        (
            'audio',
            [
                os.path.join('audio', 'failure.wav'),
                os.path.join('audio', 'mario.wav')
            ]
        )
    ]
)
