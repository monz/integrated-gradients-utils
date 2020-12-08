from setuptools import find_packages, setup

setup(
    name='integrated_gradients_utils',
    packages=find_packages(),
    version='0.1.0',
    url='http://github.com/monz/integrated-gradients-utils',
    description='Util package XAI method Integrated Gradients',
    author='Markus Monz',
    install_requires=[
        'matplotlib >= 3.3.3',
        'numpy >= 1.19.4',
        'Pillow >= 8.0.1',
        'scipy >= 1.5.4',
    ],
    extras_require={
        "tf": ["tensorflow >= 2.3.1"],
        "tf_gpu": ["tensorflow-gpu>=2.3.1"],
    },
    license='MIT',
)
