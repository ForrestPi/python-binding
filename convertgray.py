# -*- coding: utf-8 -*-
import os
def convertgray(imagename,resultname):
    """ process an image and save the results in a file"""
    path = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))
    path1 = path+"/Test/convertgray"
    path2= path+"/Test/"+imagename
    path3= path+"/Test/"+resultname
    if imagename[-3:] == 'jpg':
    	cmmd = str(path1+" "+path2+" "+path2)
    	os.system(cmmd)
    	print 'processed', imagename
    elif imagename[-3:] == 'bmp':
    	cmmd = str(path1+" "+path2+" "+path3)
    	os.system(cmmd)
    	print 'processed', imagename
    elif imagename[-3:] == 'png':
    	cmmd = str(path1+" "+path2+" "+path3)
    	os.system(cmmd)
    	print 'processed', imagename

    else: 
    	print 'Cannot processed', imagename

#imagename="xihua.bmp"
#path = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))
#print path
#resultname="gray.bmp"
#convertgray(imagename,resultname)
