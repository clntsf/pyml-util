import setuptools

with open("README.md", "r") as reader:
    long_description = reader.read()

REQ_PKGS = []

setuptools.setup(
    name="pyml-util",
    version="0.0.1",
    author="Colin Simon-Fellowes",
    author_email="colin.tsf@gmail.com",
    description="Python ML utils for training, profiling and visualizing data and models",

    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/clntsf/pyml_util",
    project_urls={
        "Repo":"https://github.com/clntsf/pyml_util"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[REQ_PKGS],
    python_requires=">=3.12.2",
)