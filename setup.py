import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="analizer-yosoyfr",  # Replace with your own username
    version="0.0.1",
    author="Francisco Suarez",
    author_email="francisco16lopez@hotmail.com",
    description="A small sql interpreter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yosoyfr/analizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)