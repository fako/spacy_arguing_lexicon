import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spacy_arguing_lexicon",
    version="0.0.1",
    author="Fako Berkers",
    author_email="email@fakoberkers.nl",
    description="A spaCy extension wrapping around the arguing lexicon by MPQA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fako/spacy_arguing_lexicon",
    packages=setuptools.find_packages(),
    install_requires=[
        "spacy>=2"
    ],
    python_requires="~=3.4",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: GPL 3",
        "Operating System :: OS Independent",
        "SpaCy :: 2"
    ),
)