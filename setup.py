from setuptools import setup
import django_typograf


setup(
    name='django-typograf',
    version=django_typograf.__version__,
    description=django_typograf.__doc__,
    url='https://github.com/Samael500/django-typograf',
    author='Maksim Skorokhod',
    author_email='Samael500@gmail.com',
    license='MIT',
    packages=('django_typograf', ),
    install_requires=('typograf>=0.1', ),
    zip_safe=False
)
