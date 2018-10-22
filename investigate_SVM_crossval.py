# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:18:46 2018

@author: Greta
"""

import pickle 
import os
import scipy.io as sio

##### Load files from SVM LOSO crossvalidation model (gamma corrected) ####

os.chdir('C:/Users/Greta/Desktop/github-mindreading-backup/SVM_savemodel/')
with open("dualcoef.pckl", 'rb') as pickleFile:
    dualcoef_full = pickle.load(pickleFile)

with open("SVM_model.pckl", 'rb') as pickleFile2:
    SVM_model = pickle.load(pickleFile2)
    
with open("support_vectors.pckl", 'rb') as pickleFile3:
    support_vectors = pickle.load(pickleFile3)
