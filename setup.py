import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="COVID19_smart_alarm_matthewcheng222",
    version="0.0.1",
    author="Matthew Cheng",
    author_email="mc879@exeter.ac.uk",
    description="Package for ECM1400CA3 - COVID-19 Smart Alarm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matthewcheng222/COVID19_Smart_Alarm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)