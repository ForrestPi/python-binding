import sys
reload(sys)
sys.setdefaultencoding('gb18030')
#great_module.pyx
cdef public great_function(a,index):
    return a[index]