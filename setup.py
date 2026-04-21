"""
Setup configuration for Database Table Profiler package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="database-table-profiler",
    version="1.0.0",
    author="DataForge Development Team",
    description="A robust, modular Python application for profiling database tables and generating comprehensive Excel reports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/database-table-profiler",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Database",
        "Topic :: Office/Business",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "table-profiler=main:main",
        ],
    },
    include_package_data=True,
    keywords="database profiling sql excel report analysis",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/database-table-profiler/issues",
        "Source": "https://github.com/yourusername/database-table-profiler",
        "Documentation": "https://github.com/yourusername/database-table-profiler/blob/main/README.md",
    },
)
