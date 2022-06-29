from setuptools import setup

setup(
    name="ccob_nb",
    author="Johan Bregeon",
    author_email="bregeon@in2p3.fr",
    url = "https://github.com/bregeon/ccob-nb",
    packages=["ccobnb"],
    description="Analysis of Rubin telescope CCOB NB system",
    setup_requires=['setuptools_scm'],
    long_description=open("README.md").read(),
    package_data={"": ["README.md", "LICENSE"]},
    use_scm_version={"write_to":"ccobnb/_version.py"},
    include_package_data=True,
    classifiers=[
        "Development Status :: 1 - Beta",
        "License :: OSI Approved :: GPL License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
    install_requires=["matplotlib",
                      "numpy",
                      "scipy",
                      "lmfit",
                      "setuptools_scm"]
)
