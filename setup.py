#!/usr/bin/env python

from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

#reqs = [line.strip() for line in open('requirements.txt') if not line.startswith('#')]

setup(name              = "cdsapi_wrappy",
      version           = "1.0",
      description       = "A package created by Dalton Sasaki and Danilo Silva, to download ERA5 dataset using the CDS API.",
      long_description  = readme(),
      license           = '',
      author            = 'Dalton Sasaki and Danilo Silva',
      author_email      = 'dalton.sasaki@gmail.com; nilodna@gmail.com',
      packages          = find_packages(),
      #install_requires  = reqs,
      python_requires='>=3.6',
      include_package_data=True,
     )
