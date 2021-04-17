import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
def _load_requirements(path_dir=_PATH_ROOT, comment_char='#'):
    with open(os.path.join(path_dir, 'requirements.txt'), 'r') as file:
        lines = [ln.strip() for ln in file.readlines()]
    reqs = [ln[:ln.index(comment_char)] if comment_char in ln else ln for ln in lines]
    reqs = [ln for ln in reqs if ln and not any(s in ln for s in ['http://', 'https://'])]
    return reqs

setuptools.setup(
    name="resnext-keras",
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
    setup_requires=[],
    install_requires=setuptools.parse_requirements('requirements.txt')
)
