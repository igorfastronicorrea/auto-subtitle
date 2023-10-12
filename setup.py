from setuptools import setup, find_packages

setup(
    version="1.0",
    name="auto_subtitle_igor",
    packages=find_packages(),
    py_modules=["auto_subtitle_igor"],
    author="Miguel Piedrafita",
    install_requires=[
        'openai-whisper',
    ],
    description="Automatically generate and embed subtitles into your videos",
    entry_points={
        'console_scripts': ['auto_subtitle_igor=auto_subtitle_igor.cli:main'],
    },
    include_package_data=True,
)
