"""Setup file for quantum applications template."""

import setuptools

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name="nus_quantum_optimization",
    description="Repository for NUS quantum optimization tutorial",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    python_requires=">=3.10",
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
)
