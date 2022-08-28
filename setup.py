import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spacy_arguing_lexicon",
    version="0.1.0",
    author="Fako Berkers",
    author_email="email@fakoberkers.nl",
    description="A spaCy extension wrapping around the arguing lexicon by MPQA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fako/spacy_arguing_lexicon",
    packages=setuptools.find_packages(),
    install_requires=[
        "spacy>=3.0.0"
    ],
    python_requires=">=3.7.0",
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ),
)
