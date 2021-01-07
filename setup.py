from setuptools import setup
from setuptools import find_packages

def read_requirements():
    with open('requirements.txt', "r") as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements

setup(
    name='eze',
    version='0.1',
    author='Ezequiel Vega<Zetta>', 
    author_email='vegaezequiel51@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points="""
        [console_scripts]
        eze=eze.cli:cli
    """,
    python_requires='>=3.6'
)
