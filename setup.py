import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="keras-resnext", # Replace with your own username
    version="0.1",
    author="Somshubra Majumdar",
    author_email="titu1994@gmail.com",
    description="Implementation of ResNeXt models for Keras 2.0+",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/titu1994/Keras-ResNeXt",
    project_urls={
        "Bug Tracker": "https://github.com/titu1994/Keras-ResNeXt/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
