from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name="statistical_distributions",
      version="0.2",
      description="Bionomial and Gaussion destributions",
      long_description= readme,
      long_description_content_type='text/markdown',
      url='https://github.com/huwwp/cryptocli',
      license=license,
      keywords='Gaussian or Binomial distributions',
      packages=["statistical_distributions"],
      author="Usman Naeem",
      author_email= "usmaanbinnaeem@gmail.com",
      zip_safe=False
      )
