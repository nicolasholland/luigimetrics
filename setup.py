from setuptools import find_packages, setup

setup(
    name='luigimetrics',
    author='Nicolas Holland',
    version='1.0.0',
    description='scrape task infos from a luigid server to be used with prometheus',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'selenium',
        'flask',
        'pyyaml'
    ]
)


