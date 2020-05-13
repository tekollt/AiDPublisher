import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AiDPublisher",
    version="0.0.1",
    author="Glimte",
    author_email="post@glimte.com",
    description="EasyPeasy downloader to download \"Aksjemarked i dag\" from DNB.",
    long_description=long_description,
    packages=setuptools.find_packages(),
)