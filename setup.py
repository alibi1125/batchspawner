from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="batchspawner",
    entry_points={
        "console_scripts": ["batchspawner-singleuser=batchspawner.singleuser:main"],
    },
    packages=["batchspawner"],
    version="1.3.2.dev1",
    description="""Batchspawner: A spawner for Jupyterhub to spawn notebooks using batch resource managers. Forked to include a move_certs implementation fitting our specific deployment.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Alexander Birk, Michael Milligan, Andrea Zonca, Mike Gilbert",
    author_email="alexander.birk@ki.uni-stuttgart.de",
    url="http://jupyter.org",
    license="BSD",
    platforms="Linux, Mac OS X",
    keywords=["Interactive", "Interpreter", "Shell", "Web", "Jupyter"],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    project_urls={
        "Bug Reports": "https://github.com/alibi1125/batchspawner/issues",
        "Source": "https://github.com/alibi1125/batchspawner/",
        "About Jupyterhub": "http://jupyterhub.readthedocs.io/en/latest/",
        "Jupyter Project": "http://jupyter.org",
    },
    python_requires=">=3.9",
    install_require={
        "jinja2",
        "jupyterhub>=1.5.1",
    },
    extras_require={
        "test": [
            "pytest",
            "pytest-asyncio",
            "pytest-cov",
            "notebook",
        ],
    },
)
