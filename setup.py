import os
import platform
import urllib.request
from setuptools import setup, find_packages
from setuptools.command.install import install


class PostInstallCommand(install):
    def run(self):
        install.run(self)

        arch = platform.architecture()[0]
        if arch == "64bit" and platform.machine() == "x86_64":
            url = "https://github.com/Y2Z/monolith/releases/download/v2.7.0/monolith-gnu-linux-x86_64"
        elif arch == "64bit" and platform.machine() == "aarch64":
            url = "https://github.com/Y2Z/monolith/releases/download/v2.7.0/monolith-gnu-linux-aarch64"
        else:
            print("Unsupported architecture : {} {}".format(
                platform.architecture(), platform.machine()))
            print("Uninstalling monolith-py...")
            os.system("pip uninstall -y monolith-py")
            return

        os.makedirs(os.path.join(self.install_lib, "monolithpy/bin"), exist_ok=True)
        bin_file = os.path.join(self.install_lib, "monolithpy/bin/monolith")

        print("Downloading monolith binary for {} {}...".format(
            arch, platform.machine()))
        urllib.request.urlretrieve(url, bin_file)

        os.chmod(bin_file, 0o755)

        print("monolith-py installed successfully !")


setup(
    name="monolith-py",
    version="2.0.0",
    author="krishna2206",
    author_email="fitiavana.krishna@gmail.com",
    description="A simple python wrapper to https://github.com/Y2Z/monolith.",
    long_description="file: README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/krishna2206/monolith-py",
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    cmdclass={
        "install": PostInstallCommand,
    },
)
