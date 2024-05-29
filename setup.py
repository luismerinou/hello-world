from setuptools import setup, find_packages

setup(
    name='Github-Hello-world',
    version='1.0',
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'main.py',
        ],
    },
    author='Luis Merino Ulizarna',
    author_email='lmerinoulizarna@gmail.com',
    description='Proyecto para aprender a usar GitHub y sus características clave, como Pull Requests y ciclos de '
                'CI/CD.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/luismerinou/hello-world/',  # Reemplaza con la URL de tu repositorio
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Versión mínima de Python requerida
)
