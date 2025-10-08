import setuptools
setuptools.setup(
    name="parrot",
    version="1.0",
    author="prithiviraj damodaran",
    author_email="",
    description="Parrot paraphraser",
    long_description="Parrot paraphraser",
    url="https://github.com/RupeshSangoju/Parrot_Paraphraser",
    packages=setuptools.find_packages(),
    install_requires=[
        'transformers==4.30.2',
        'sentencepiece==0.2.0',
        'python-Levenshtein==0.25.1',
        'sentence-transformers==2.2.2',
        'fuzzywuzzy==0.18.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
)