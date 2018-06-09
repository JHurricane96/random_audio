import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirement_list = [r.strip() for r in open('requirements.txt', 'r').readlines() if r]

setuptools.setup(
    name="random_audio",
    install_requires=requirement_list,
    version="1.0.1",
    author="Arun Ramachandran",
    author_email="ramachandran.arun@outlook.com",
    description="CLI tool to generate a mash-up of audio clips",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jhurricane96/random_audio",
    packages=setuptools.find_packages(),
    license="MIT",
    entry_points={
        "console_scripts": ["random_audio=random_audio:main"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities"
    ],
)