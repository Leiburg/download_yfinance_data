import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="download-yfinance-data",
    version="0.0.1",
    author="Nathan George",
    author_email="nathancgeorge@gmail.com",
    description="Downloads and saves Yahoo finance stock data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nateGeorge/download_yfinance_data",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
