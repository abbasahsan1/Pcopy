from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pcopy-tool',
    version='1.0.0',
    py_modules=['pcopy'],
    install_requires=[
        'pyperclip>=1.8.0',
        'pathspec>=0.11.0',
    ],
    entry_points={
        'console_scripts': [
            'pcopy=pcopy:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='Cross-platform CLI tool to merge text files and copy to clipboard for LLM context',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/abbasahsan1/Pcopy',
    project_urls={
        'Bug Reports': 'https://github.com/abbasahsan1/Pcopy/issues',
        'Source': 'https://github.com/abbasahsan1/Pcopy',
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Environment :: Console',
    ],
    keywords='clipboard, file-merger, llm, ai, context, development-tools',
    python_requires='>=3.7',
    license='MIT',
)
