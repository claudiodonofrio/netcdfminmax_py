## netcdfminmax

A python script to read a netcdf file and extract minimum and maximum values for all variables. The script contains a "class" which can be instantiated or the script can be executed directly.
""" pythyon
python cdfminmax.py -h
usage: cdfminmax.py [-h] [-v] [-d DIRECTORY]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         show process progess
  -d DIRECTORY, --directory DIRECTORY
                        set root directory to traverse
"""

- If -d DIRECTORY is not provided or invalid, the current directory is used as "root directory"
- all files and folders within the "root directory" are considered
- for a valid netcdf file an output file is written with filename.json
- already existing outputfiles are overwritten


#### Example output:

python cdfminmax.py -v -d "./netcdf_testfiles"
rootdir = ./netcdf_testfiles
./netcdf_testfiles\edgar.nc
timed in (s): 9.2700533
overwrite ./netcdf_testfiles\edgar.nc.json ...OK
{
   "filename": "edgar.nc",
   "lon": {
      "min": "-179.75",
      "max": "179.75"
   },
   "lon_bnds": {
      "min": "-180.0",
      "max": "180.0"
   },
   "lat": {
      "min": "-89.75",
      "max": "89.75"
   },
   "lat_bnds": {
      "min": "-90.0",
      "max": "90.0"
   },
   "time": {
      "min": "1416.0",
      "max": "2159.0"
   },
   "emission": {
      "min": "0.0",
      "max": "134.85986"
   },
   "cell_area": {
      "min": "13487115.0",
      "max": "3091058400.0"
   }
}
./netcdf_testfiles\edgar.nc.json not a netCDF file
./netcdf_testfiles\ingos222.nc
timed in (s): 0.7397349000000002
overwrite ./netcdf_testfiles\ingos222.nc.json ...OK
{
   "filename": "ingos222.nc",
   "lon": {
      "min": "-11.958333",
      "max": "29.958334"
   },
   "lat": {
      "min": "30.041666",
      "max": "71.958336"
   },
   "time": {
      "min": "0.0",
      "max": "2526.0"
   },
   "rn_flux": {
      "min": "0.0",
      "max": "170.73242"
   }
}
./netcdf_testfiles\ingos222.nc.json not a netCDF file

(netcdf) C:\Users\Claudio\Documents\GitHub\netcdfminmax_py_dev>