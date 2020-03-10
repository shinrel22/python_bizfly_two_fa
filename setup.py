import setuptools
import os


def get_version(version_tuple):
    """Return the version tuple as a string, e.g. for (0, 10, 7),
    return '0.10.7'.
    """
    return ".".join(map(str, version_tuple))


try:
    with open("README.rst") as fin:
        LONG_DESCRIPTION = fin.read()
except Exception:
    LONG_DESCRIPTION = None

DESCRIPTION = "Python SDK for Bizfly2FA"

CLASSIFIERS = [
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

init = os.path.join(os.path.dirname(__file__), "bizfly_two_fa", "__init__.py")
version_line = list(filter(lambda l: l.startswith("VERSION"), open(init)))[0]

VERSION = get_version(eval(version_line.split("=")[-1]))

setuptools.setup(
    name="bizfly_two_fa",
    version=VERSION,
    author="Tri Nguyen",
    author_email="tringuyen5835@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/shinrel22/python_bizfly_two_fa",
    packages=setuptools.find_packages(),
    classifiers=CLASSIFIERS,
    python_requires='>=2.7',
    license="MIT",
)
