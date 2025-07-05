"""
Setup script for Visualio - Data Visualization Assistant
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="visualio",
    version="1.0.0",
    author="Visualio Team",
    author_email="",
    description="A data visualization assistant that creates charts from natural language commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Haix02/Visualio",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Data Analysts",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
        ],
    },
    entry_points={
        "console_scripts": [
            "visualio=app:main",
        ],
    },
    keywords="data visualization, streamlit, plotly, natural language, charts, analytics",
    project_urls={
        "Bug Reports": "https://github.com/Haix02/Visualio/issues",
        "Source": "https://github.com/Haix02/Visualio",
        "Documentation": "https://github.com/Haix02/Visualio#readme",
    },
)