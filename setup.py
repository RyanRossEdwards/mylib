from setuptools import find_packages, setup
setup(
    name='mylib',
    packages=find_packages(include=['mylib']),
    version='0.1.0',
    description='My First Library',
    author='Ryan Edwards',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: BSD 3-Clause License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    # Packages used by the library
    install_requires=[],
    # To enable pytest
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)