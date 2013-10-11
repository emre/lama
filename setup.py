from setuptools import setup

setup(
    name='imgui',
    version='0.4',
    packages=['imgui'],
    url='http://github.com/emre/imgui',
    license='MIT',
    author='Emre Yilmaz',
    author_email='mail@emreyilmaz.me',
    description='a tool to take screenshots and upload to imgur from command line.',
    install_requires=["requests", ],
    entry_points={
        'console_scripts': ['imgur_client = imgur_client.upload:main',]
    }
)