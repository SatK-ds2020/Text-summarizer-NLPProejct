import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.1.0"

REPO_NAME="Text-Summarizer-NLPProject"
AUTHOR_USER_NAME = "Satindra Kathania"
SRC_REPO="Text-Summarizer"
AUTHOR_EMAIL="kathania.s2020@gmail.com",

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A text summarization tool using NLP techniques",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SatK-ds2020/Text-summarizer-NLPProejct",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
        
   )
    