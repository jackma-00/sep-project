"""Package setup"""
from setuptools import setup, find_packages

setup(
    name="unzip-v1",
    version="0.1.0",
    author="Jacopo Maragna and Abdelrahman Saleh",
    description="Swedish Event Planning Business Project",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.100.0",
        "uvicorn==0.22.0",
        "python-multipart==0.0.6",
    ],
    extras_require={
        "dev": [
            "black==23.1.0",
            "pylint==2.17.0",
            "pytest==7.3.1",
            "httpx==0.23.3",
            "uvicorn==0.22.0",
        ]
    },
)
