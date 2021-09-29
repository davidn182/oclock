# -*- coding: utf-8 -*-
import os
import re
import sys
from setuptools import setup

if not sys.version_info[:2] >= (3, 6):
    sys.exit(f"oclock is only meant for Python 3.6 and up.\n"
             f"Current version: {sys.version_info[0]}.{sys.version_info[1]}.")

setup(
    name="oclock",
    version="0.0.1",
    description="Open-source OBS clock error correction program",
    author="Naranjo, D., Parisi, L., Jousset, P., Weemstra, C., and Jónsson, S",
    author_email="davidn182@hotmail.com",
    packages=find_packages(include=['oclock', 'oclock.*']),
    install_requires=[
        'pandas>=0.23.3',
        'numpy>=1.15',
        'matplotlib>=3.2.0,
        'obspy',
        'seaborn']
    python_requires=">=3.7",
    license="Apache-2.0",
    setup_requires=["setuptools_scm"],
)
