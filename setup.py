from setuptools import find_packages, setup

# packages: python packages
# find_package(): auto find package
# include_package_data: if it has other file (static/templates ...)
# If you need to include other data, then create a MANIFEST.in file

# run "pip install -e ." to install packages
# check with pip list

setup(
	name='flaskr',
	version='1.0.0',
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'flask',
	],
)
