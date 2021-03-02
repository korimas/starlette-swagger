from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='starlette_swagger',
    license='BSD',
    version='0.12',
    author='zpzhou',
    author_email='himoker@163.com',
    url='https://github.com/zpdev/starlette-swagger',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    description='swagger ui for starlette',
    packages=['starlette_swagger'],
    install_requires=['starlette', 'starlette_openapi', 'starlette_pydantic'],
    zip_safe=False,
    include_package_data=True,
)
