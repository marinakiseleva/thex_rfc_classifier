# Transient Classifier

Classifier that identifies transient type based on information about the host galaxy.

## Getting Started

Run model.py from command line with one simple call: python model.py

Pass in appropriate arguments. An example call is below:

$ python model.py 
	-file_name '../../data/THEx-catalog.v0_0_3.fits' 
	-col_list "AllWISE" 
	-min_rs 0 
	-max_rs .1 
	-subsample 'Ia' 
	-oneall 'Ia'


### Prerequisites

Python 3 and the following packages:
 - numpy
 - pandas
 - sklearn
 - argparse 
 - sys

You also need the .FITS data file to run analysis on. Currently using Yujing's version 3 database, THEx-catalog.v0_0_3.fits. 

### How it works
You call model.py which runs the main(). It first initializes a Pandas DataFrame of data using data_init.collect_data. Then, it calls the function run_analysis in model.py which is the workhorse of this program. Here, it uses data_prep.prep_data which filters down the data based on values passed in for: redshift, subsampling, and one versus all divsion. 


## Versioning

This is Version 1.

## Authors

Yuantian Liu, Marina Kiseleva


## Acknowledgments

THEx team members.
