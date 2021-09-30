Usage
=====

.. _installation:

Installation
------------

To use oclock, first install it using pip:

You need to download the folder.
It is necessary to install Obspy, Jupyter notebooks, and Basemap.
It is recommendable doing this via Anaconda and in a new environment as follows:
```bash
$ conda config --add channels conda-forge
$ conda create -n clock_errors python=3.7
$ conda activate clock_errors
(clock_errors) $ conda install obspy basemap
(clock_errors) $ conda install -c conda-forge jupyterlab notebook
```
Additionally you will need to have gfortran and SAC installed in your computer to run the fortran executable.
### Getting started
You can take a look at the jupyter-notebook at the **Tutorial** section for basic usage of the program. You will neet to have access to the data so send an e-mail to d.f.naranjohernandez@tudelft.nl
