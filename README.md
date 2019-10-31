## netcdfminmax

A python script to read a netcdf file and extract minimum and maximum values for all variables. The script contains a "class" which can be instantiated or the script can be executed directly.
``` pythyon
python cdfminmax.py -h
usage: cdfminmax.py [-h] [-v] [-d DIRECTORY]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         show process progess
  -d DIRECTORY, --directory DIRECTORY
                        set root directory to traverse
```

- If -d DIRECTORY is not provided or invalid, the current directory is used as "root directory"
- all files and folders within the "root directory" are considered
- for a valid netcdf file an output file is written with filename.json
- already existing outputfiles are overwritten


#### Example output:

``` python
python cdfminmax.py -v -d "./netcdf_testfiles"
```
rootdir = ./netcdf_testfiles<br>
./netcdf_testfiles\edgar.nc<br>
timed in (s): 9.2700533<br>
overwrite ./netcdf_testfiles\edgar.nc.json ...OK<br>
{<br>
   "filename": "edgar.nc",<br>
   "lon": {<br>
      "min": "-179.75",<br>
      "max": "179.75"<br>
   },<br>
   "lon_bnds": {<br>
      "min": "-180.0",<br>
      "max": "180.0"<br>
   },<br>
   "lat": {<br>
      "min": "-89.75",<br>
      "max": "89.75"<br>
   },<br>
   "lat_bnds": {<br>
      "min": "-90.0",<br>
      "max": "90.0"<br>
   },<br>
   "time": {<br>
      "min": "1416.0",<br>
      "max": "2159.0"<br>
   },<br>
   "emission": {<br>
      "min": "0.0",<br>
      "max": "134.85986"<br>
   },<br>
   "cell_area": {<br>
      "min": "13487115.0",<br>
      "max": "3091058400.0"<br>
   }<br>
}<br>
./netcdf_testfiles\edgar.nc.json not a netCDF file<br>
