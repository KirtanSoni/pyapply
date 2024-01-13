from setuptools import setup, find_packages
import subprocess
import os

pyapply_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)
if "-" in pyapply_version:
    # when not on tag, git describe outputs: "1.3.3-22-gdf81228"
    # pip has gotten strict with version numbers
    # so change it to: "1.3.3+22.git.gdf81228"
    # See: https://peps.python.org/pep-0440/#local-version-segments
    v,i,s = pyapply_version.split("-")
    pyapply_version = v + "+" + i + ".git." + s

assert "-" not in pyapply_version
assert "." in pyapply_version

assert os.path.isfile("pyapply/version.py")
with open("pyapply/VERSION", "w", encoding="utf-8") as fh:
    fh.write("%s\n" % pyapply_version)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pyapply',
    version=pyapply_version,
    author="Kirtan Soni",
    author_email="1kirtansoni@gmail.com",
    description="Tool to automate coverletter generation (and much more)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kirtansoni/pyapply",
    packages=find_packages(),
    package_data={"pyapply": ["VERSION"]},  # include VERSION file
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=[
        'docx==0.2.4',
        'click==8.1.7',
        'openai==1.3.6',
        'pyperclip==1.8.2',
        'python-dotenv==1.0.0',
        'reportlab==4.0.7',
        'click_help_colors==0.9.4',
    ],
    entry_points={
        'console_scripts': [
            'pyapply = pyapply.__main__:cli' #TODO: might not work
        ]
    }
)
