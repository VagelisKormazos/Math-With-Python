import time
import mpmath as mpm # library for arbitrary precision calculations
mpm .mp.dps = 60 # define decimal precision for calculations
a, x0 , err , n , h = mpm .mpf (2) , mpm .mpf (1) , mpm .mpf (10**( -50) ), 1 , 0.0001
start = time .time ()
rec = lambda x: (x **2+h*x+2) /(2*x+h) #N-R recursive formula
x1 = rec (x0)
while mpm .fabs(x1 -x0) >= err :
# print (n, x1 , mpm . fabs(x1 -x0))
 x0 = x1
 x1 = rec (x0)
 n = n + 1
 end = time.time ()
print (" Approximation of the square root of %s using the N -R method :"%(a))
print ("root = %s, repetitions = %s"%(x1 , n))
print ("absolute error = %s"%( mpm . fabs(x1 -x0)))
print ("Time elapsed (seconds ): %s"%( end - start ))
