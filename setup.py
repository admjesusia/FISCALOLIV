#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# Requisitos básicos de instalação
requirements = [
    'streamlit>=1.30.0',
    'pandas>=2.0.3',
    'numpy>=1.24.3',
    'matplotlib>=3.7.2',
    'seaborn>=0.12.2',
    'pytesseract>=0.3.10',
    'pdf2image>=1.16.3',
    'Pillow>=10.0.0',
    'python-dateutil>=2.8.2',
    'tqdm>=4.65.0',
]

# Requisitos extras para diferentes funcionalidades
extras_require = {
    'reports': [
        'reportlab>=4.0.4',
        'jinja2>=3.1.2',
        'openpyxl>=3.1.2',
    ],
    'dev': [
        'pytest>=7.3.1',
        'mypy>=1.3.0',
        'pylint>=2.17.4',
        'black>=23.3.0',
    ],
    'full': [
        'reportlab>=4.0.4',
        'jinja2>=3.1.2',
        'openpyxl>=3.1.2',
        'plotly>=5.18.0',
        'pydantic>=2.4.2',
        'tabulate>=0.9.0',
        'pyyaml>=6.0',
    ],
}

# Metadados do pacote
setup(
    name='pdv_analyzer',
    version='1.0.0',
    description='Sistema de importação de notas fiscais PDF para formato BK',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='PDV Analysis Team',
    author_email='pdv.analysis@example.com',
    url='https://github.com/pdv-analysis/pdv-analyzer',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    entry_points={
        'console_scripts': [
            'pdv-analyzer=pdv_analyzer.cli:main',
            'pdf-to-bk=pdv_analyzer.pdf_to_bk_processor:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Office/Business :: Financial',
        'Topic :: Scientific/Engineering :: Image Recognition',
    ],
    python_requires='>=3.7',
    keywords='pdv, invoice, ocr, backup, bk-file, retail',
)
