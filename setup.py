from setuptools import setup


requirements = []

if __name__ == "__main__":
    setup(
        name='myprofiler',  # other name like deepprofile
        version='0.1.0',
        author='Edouard GEZE',
        author_email='edouard.geze@gmail.com',
        license='LICENSE.txt',
        description='interactive profiler for deep learning',
        long_description=open('README.md').read(),
        install_requires=requirements,
    )