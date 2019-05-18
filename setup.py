import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iindustry-comms-python-utils",
    version="0.0.1",
    author="Ricardo Correia",
    author_email="ricardocorreiap@gmail.com",
    description="iIndustry Communication Utils for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iindustryrocks/I2CServer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)