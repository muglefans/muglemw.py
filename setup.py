import setuptools

setuptools.setup(
    name='muglemw',
    version='0.1.1',
    packages=['muglemw',],
    license='MIT',
    description = 'Python wrappers around the Mugle wallet V3 and Mugle node V2 APIs',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author = 'muglefans',
    author_email = 'muglefans@hotmail.com',
    install_requires=['requests', 'eciespy', 'coincurve', 'Crypto'],
    url = 'https://github.com/muglefans/muglemw.py',
    download_url = 'https://github.com/muglefans/muglemw.py/archive/refs/tags/v0.1.1.tar.gz',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    )
