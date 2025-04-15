from setuptools import setup, find_packages

setup(
    name='text-to-number',
    version='1.0',  
    packages=find_packages(), 
    install_requires=[  
        'word2number',  
    ],
    entry_points={
        'console_scripts': [
            'text_to_number = text_to_number.text_to_number_amount:main', 
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', 
)
