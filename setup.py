from setuptools import setup

setup(name='pytest-selenium',
      version='1.0',
      description='pytest plugin for Selenium',
      long_description=open('README.rst').read(),
      author='Dave Hunt',
      author_email='dhunt@mozilla.com',
      url='https://github.com/davehunt/pytest-selenium',
      packages=['pytest_selenium', 'pytest_selenium.cloud'],
      install_requires=[
          'pytest>=2.2.4',
          'selenium>=2.26.0',
          'requests==2.6.0'],
      entry_points={'pytest11': [
          'selenium = pytest_selenium.pytest_selenium',
          'selenium_safety = pytest_selenium.safety']},
      license='Mozilla Public License 2.0 (MPL 2.0)',
      keywords='py.test pytest selenium saucelabs browserstack mozwebqa webqa '
               'qa mozilla',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7'])
