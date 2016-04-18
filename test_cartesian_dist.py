# Test script for testing the cartesian distance module between two 3D points

from math import sqrt
import cartesian_dist as cd

loc = [0,0,0,1/sqrt(3.0),1/sqrt(3.0),1/sqrt(3.0)]
d = cd.dist(loc)
print "Distance between (%.1f,%.1f,%.1f) and (%.1f,%.1f,%.1f): %.1f" %(loc[0],loc[1],loc[2],loc[3],loc[4],loc[5],d)
