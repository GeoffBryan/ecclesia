#!/usr/bin/env python
"""
mk_hdf5.py
"""
 
import h5py
import numpy as np

# ===================
# Main Python section
# ===================
#
if __name__ == '__main__':
 
    f = h5py.File("mytestfile.hdf5", "w")
    
    dset = f.create_dataset("mydataset", (100,), dtype='i')
    
    dset[...] = np.arange(100)
 
    print("dset.shape = ",dset.shape)
    print( "dset.dtype = ",dset.dtype)
    print("dset.name = ",dset.name)
    print( "f.name = ",f.name)
   
    grp = f.create_group("subgroup");
    dset2 = grp.create_dataset("another_dataset", (50,), dtype='f');
    print("dset2.name = ",dset2.name)
    
    dset3 = f.create_dataset('subgroup2/dataset_three', (10,), dtype='i')
    print("dset3.name = ",dset3.name)
   
  # end if
