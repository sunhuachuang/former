from setuptools import setup

setup(
    name="former",
    version="0.0.1",
    keywords=("form", "former", "validate", "auto-bind"),
    description="A package for auto build form, validate form, bind data to object",

    url="https://github.com/sunhuachuang/former",
    author="sunhuachuang",
    author_email="huachuang20@gmail.com",
    packages=['former'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'schematics',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
