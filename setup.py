from distutils.core import setup


setup(
    name= 'jupyter-gradelabel',
    version='0.0.1',
    description='Label for nbgrader cells',
    author='Dmitry Gerasimenko',
    author_email='kiddima@gmail.com',
    license='BSD',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Framework :: Jupyter',
    ],
    install_requires=[
        'jupyter',
        'notebook>=4.2.0',
    ],
    packages=['gradelabel'],
)