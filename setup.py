import re

from setuptools import setup, find_packages


_deps = [
    "dataclasses",
    "tqdm>=4.27",
    "pytest",
    "parameterized",
    "click",
    "black",
    "wheel",
    "twine",
]

constraints = {
    name: constraints for constraints, name in (
        re.findall(r"^(([^!=<>~ ]+)(?:[!=<>~ ].*)?$)", x)[0] for x in _deps)
}

def identify_deps(*names) -> list[str]:
    return [constraints[name] for name in names]


extras = {}
extras["base"] = identify_deps("dataclasses", "tqdm")
extras["dev"] = identify_deps("pytest", "parameterized", "click", "black", "wheel", "twine")
extras["testing"] = (
    extras["base"]
    + extras["dev"]
)


_keywords = (
    "ai", "toolkit",
)

setup(
    name="teenytiny",
    version="0.1.1",
    author="MrHenryD",
    author_email="hi@example.com",
    description="The teeny tiny ML toolkit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords=" ".join(_keywords),
    license="Apache 2.0 License",
    url="https://github.com/MrHenryD/teenytiny",
    # package_dir={"": "teenytiny"}, # Used for alternative folder
    packages=find_packages(),
    extras_require=extras,
    python_requires=">=3.9.0",
    install_requires=[
        constraints["dataclasses"],
        constraints["tqdm"],
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)