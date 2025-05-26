import sys
from setuptools import setup
from setuptools import find_packages

required = []
dependency_links = []
EGG_MARK = '#egg='
with open('requirements.txt') as reqs:
    for line in reqs.read().split('\n'):
        if line.startswith('-e git:') or line.startswith('-e git+') or \
                line.startswith('git:') or line.startswith('git+'):
            if EGG_MARK in line:
                package_name = line[line.find(EGG_MARK) + len(EGG_MARK):]
                required.append(package_name)
                dependency_links.append(line)
            else:
                print('Dependency to a git repository should have the format:')
                print('git+ssh://git@github.com/xxxxx/xxxxxx#egg=package_name')
                sys.exit(1)
        else:
            required.append(line)

setup(
    name='xattrfile',
    url="https://github.com/metwork-framework/xattrfile",
    packages=find_packages(),
    install_requires=required,
    include_package_data=True,
    dependency_links=dependency_links,
    entry_points={
        "console_scripts": [
            "print_tags = xattrfile.print_tags:main",
            "get_tag = xattrfile.get_tag:main",
            "set_tag = xattrfile.set_tag:main"
        ]
    }
)
