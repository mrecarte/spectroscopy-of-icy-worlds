Hello!

Project Overview:
This repository cintain all of the files pertaining to my current research for creating a spectral analysis tool! 

This year, NASA will launch Europa Clipper. This mission will explore the surface salts and icy composition to better understand the moon's potential to support life. Europa Clipper is planned for launch in October 2024 and will arrive in 2030. NASA scientists have identified a list of salts that are present on the surface and sub-surface minerology on Europa, but not much else! So, this is where this project comes in! We would like to predict some mixtures present on Europa from the identifies salts so we can get to know a little bit more about the mechanical and chemical properties of this icy moon before it reaches in 2023 through advanced spectroscopic analysis.

Research Objectives:
This project utilizes a second-order nonlinear mixing algorithm to model and predict the visible and infrared spectroscopic signals from Europa's surface. By overcoming limitations that the traditional linear mixing models put on us, this approach allows for more accurate predictions of scattering behaviors and material properties.

a description of the files in this repo:

mineral_data - Contains raw data files for various minerals from the USGS database

ruff, salt_volumes, usgs -  Directories with categorized mineral data.

gypsum_index.txt, gypsum_spectra.txt, halite_imaginary_index.txt, etc. - Text files with specific mineral indices and spectra.

create_table.py, makescv.py, minerals_table.py: Python scripts for creating and managing data tables.

GA_LSQ_approach_for_optical_constants_mod.ipynb - Jupyter notebook detailing the genetic algorithm and least squares approach for modeling optical constants.

Hapke-Mixing.ipynb - Jupyter notebook for exploring the Hapke mixing models.

create_table.py - creates the database and table that houses the minerals' information.

populate_table.py - populates table with minerals' information. Essentially, the table is complete after running this code. Currently just have USGS data. Will add RRUFF data soon.

query_minerals.py - getting the information of the minerals you want from the database

mcr.py - an unmixing method that uses multivariate curve resolution (MCR). It is currently used within linear_mixing.py as it requires some variables in that script. Cannot stand on its own at the moment.
