# -*- coding: utf-8 -*-

"""
    extract the range for all variables
    in netCDF files and store them as json
    files with the same base file name
    
    starting from the base directory, all 
    files are considered and checked
    
    https://www.unidata.ucar.edu/software/netcdf/docs/faq.html
    
    How can I tell which format a netCDF file uses?
    The short answer is that under most circumstances, you should not care,
    if you use version 4.0 or later of the netCDF library to access data
    in the file. But the difference is indicated in the first four bytes of
    the file, which are 'C', 'D', 'F', '\001' for the classic netCDF CDF-1
    format; 'C', 'D', 'F', '\002' for the 64-bit offset CDF-2 format;
    'C', 'D', 'F', '\005' for the 64-bit data CDF-5 format;
    or '\211', 'H', 'D', 'F' for an HDF5 file,
    which could be either a netCDF-4 file or a netCDF-4 classic model file.
    (HDF5 files may also begin with a user-block of 512, 1024, 2048, ... bytes
    before what is actually an 8-byte signature beginning with the 4 bytes above.)
"""

import os
from netCDF4 import Dataset
import json
import argparse
import time


class cdfMinMax:
    
    #def "__init__(self, dobj):            
    def __init__(self):            
        self.rootdir = '.'
        self.headers = ['cdf','hdf']
        self.verbose = False

# ----------------------------------------------------------------------
    def set_verbose(self, v):
        self.verbose = v        

# ----------------------------------------------------------------------
    def set_directory(self, directory):
        if (os.path.isdir(directory)):
            self.rootdir = directory
            self.consoleOtput('rootdir = ' + str(self.rootdir))
        else:
            self.consoleOtput('dir '+ directory +' not valid.')
            self.consoleOtput('Rootdirectory set to ' + self.rootdir)

# ----------------------------------------------------------------------
    def filecheck(self, filename): 
        # minimal sanity check
        # check the first 8 bytes for existence
        # of "cdf" or "hdf"
        # TODO: check possible offset for netCDF superblock at 512 1024 ...
        headers = ['cdf', 'hdf']
        with open(filename, 'rb') as ncf:  
            signature = str(ncf.read(8).lower())
            # self.consoleOtput(signature)
        
        for header in headers:
            if header in signature:
                return True
    
        return False
    
    # ----------------------------------------------------------------------   
    def run(self):
        
        for path, names, files in os.walk(self.rootdir):
            for file_name in files:
                
                # ---- for benchmark
                if(self.verbose):
                    t1_start = time.perf_counter()
                # ---- 
                
                f = os.path.join(path, file_name)
                if not self.filecheck(f):
                    self.consoleOtput(f + ' not a netCDF file')
                    continue
                
                self.consoleOtput(f)
                # now we should have a valid netcdf file  
                # but a textfile can have the header string in the first lien
                # hence we add another try..
                try: 
                    ncf = Dataset(f)            
                except: 
                    self.consoleOtput(f + ' not a netCDF file')
                    continue
                
                out = {}
                fout = f + '.json'
                
                out['filename'] = file_name
                for k in ncf.variables.keys():
                    var = ncf.variables[k]
                    out[var.name] = {'min':str(var[:].min()),
                       'max': str(var[:].max())}                

                # ---- for benchmark
                if(self.verbose):
                    performance = time.perf_counter() - t1_start
                    print('timed in (s): '+ str(performance))
                # ---- 
                
                if os.path.isfile(fout):
                    self.consoleOtput('overwrite ' + fout + ' ...OK')
                else:
                    self.consoleOtput(fout + ' ...OK')
                

                with open(fout, 'w') as fo:  
                    json.dump(out, fo)
                    self.consoleOtput(json.dumps(out, indent=3))
    
    def consoleOtput(self, msg):
        if self.verbose:
            print(msg)
    # ----------------------------------------------------------------------

if __name__ == "__main__":
    helptxt = """
        We expect only up to two (2) arguments
        cfdminmax
            @input: no arguments:
                    processing the current directory and subdirectories
                    no console output by default
            
            @input: -v, --verbose:
                    processing the current directory and subdirectories
                    filenames and processing status is sent to console
                    
            @input: -d --directory:
                    rootdirectory is set to --directory
                    if --directory is not "valid", reset to default     
    
            """
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-v',
                        '--verbose', 
                        help='show process progess',
                        action="store_true")    
    parser.add_argument('-d',
                        '--directory',
                        help='set root directory to traverse',
                        type=str)    
    
    args = parser.parse_args()    
    
    cdf = cdfMinMax()
    
    if args.verbose is not None:
        cdf.set_verbose(args.verbose)
    if args.directory is not None:
        cdf.set_directory(args.directory)
       
    cdf.run()




















