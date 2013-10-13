from setuptools import setup

setup(
    name='lama',
    version='0.1',
    packages=['lama'],
    url='http://github.com/emre/lama',
    license='MIT',
    author='Emre Yilmaz',
    author_email='mail@emreyilmaz.me',
    description='a tool to take screenshots and upload to imgur from command line.',
    install_requires=["requests", ],
    entry_points={
        'console_scripts': ['lama = lama.upload:main', ]
    }
)
