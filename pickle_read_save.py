#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 15:54:03 2021

@author: gui
"""
try:
   import cPickle as pickle
except:
   import pickle
   
class ReadSaveDate:
    def __init__(self):
        pass
    
    def readPickle(filename):
        with open(filename, 'rb') as fd:
            new_pickle = pickle.load(fd)
        return new_pickle

    def savePickle(filename, object_pickle):       
        with open(filename, 'wb') as fd:
            pickle.dump(object_pickle, fd)     
        
 