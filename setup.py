from setuptools import setup, find_packages

setup(
    name='pyapply',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click==8.1.7',
        'openai==1.3.6',
        'pyperclip==1.8.2',
        'python-dotenv==1.0.0',
        'reportlab==4.0.7',
    ],
)