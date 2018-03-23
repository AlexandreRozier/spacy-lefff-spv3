
#!/usr/bin/env python
# coding: utf8

from pathlib import Path
from setuptools import setup, find_packages

def setup_package():
    package_name = 'spacy_lefff'
    root = Path(__file__).parent.resolve()

    # Get readme
    readme_path = root / 'README.md'
    with readme_path.open('r', encoding='utf8') as f:
        readme = f.read()

    setup(
        name='spacy-lefff',
        description=' Custom French lemmatizer based on Leff for spacy',
        long_description=readme,
        author='sami moustachir',
        author_email='moustachir.sami@gmail.com',
        url='https://github.com/sammous/spacy-lefff',
        version='0.1.3',
        license='MIT',
        packages=find_packages(exclude=['tests']),
        package_data={'spacy_lefff': ['data/*']},
        tests_require=['pytest', 'pytest-cov'],
        install_requires=[
            'spacy>=2.0.0,<3.0.0'],
        zip_safe=False,
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
            'Development Status :: 3 - Alpha',
            'Natural Language :: English',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'Topic :: Scientific/Engineering',
            'License :: OSI Approved :: MIT License',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )


if __name__ == '__main__':
    setup_package()
