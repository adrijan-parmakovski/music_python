from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
    f.close()
with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read()
    f.close()

setup(
    name = 'PyMusiC#',
    version = '0.1.0',
    py_modules = ['pymusic'],
    packages = find_packages(exclude=['tests']),
    install_requires = [
        'click'
    ],
    entry_points = """
        [console_scripts]
        pymusic=pymusic:cli
    """
)
