from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA mypackage',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Nkamogeleng/mypackage',
    author='Immaculate Nkamogeleng',
    author_email='kamo21.km@gmail.com'
)
