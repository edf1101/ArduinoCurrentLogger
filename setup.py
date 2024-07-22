import setuptools

with open("README.md", "r") as fh:
    readme = fh.read()

setuptools.setup(
    name='arduino_current_logger',
    version='1.0',
    author="edf1101",
    author_email="blank@blank.com",
    description="Current Logging with an Arduino and an INA219, graphed in python",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/edf1101/ArduinoCurrentLogger",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=["matplotlib", "numpy", "appdirs", "tkscrollableframe"]
)
