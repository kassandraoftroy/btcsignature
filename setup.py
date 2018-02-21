from setuptools import setup

setup(name='btcsignature',
      version='0.11',
      description='secure offline bitcoin transaction signing tool',
      url='http://github.com/',
      author='sendbtcsimply',
      author_email='sendbtcsimply@protonmail.com',
      license='MIT',
      packages=['btcsignature'],
      entry_points = {'console_scripts': ['sign-offline=btcsignature.command_line:main'],},
      install_requires=['bitcoin','blockchain', 'enum', 'ecdsa'],
      zip_safe=False)