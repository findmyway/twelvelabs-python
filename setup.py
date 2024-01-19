from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="twelvelabs",
    version="0.0.0",
    packages=find_packages(),
    install_requires=required,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "twelvelabs=cli.main:cli",
        ],
    },
    author="Twelve Labs",
    description="SDK for Twelve Labs API",
)
