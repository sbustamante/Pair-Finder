#This script allows to build the Reduced Isolated Pairs sample using
#the data obtained by the Pair-Finder code.

import numpy as np

#Range of mass and relative distance in order to build the RIP sample
#Taken from Forero-Romero 2013
Mass_Range	=	[1e12, 4e12]
Distance_Range	=	[0.7, 0.8]

IP = np.loadtxt( "./IsoPairs.dat" )

RIP = []
for i in xrange( len(IP) ):
    if Mass_Range[0] <= IP.T[2][i] + IP.T[5][i] <= Mass_Range[1] and \
    Distance_Range[0] <= IP.T[7][i] <= Distance_Range[1]:
	RIP.append( IP[i] )
RIP = np.array(RIP)

np.savetxt( "./RedIsoPairs.dat", RIP, fmt="%d\t%d\t%1.4e\t%d\t%d\t%1.4e\t%d\t%4.3f\t\t%+4.3f\t%d\t%4.3f\t%d\t%4.3f\t%d\t%4.3f\t%d\t%4.3f\t\t%d\t%4.3f\t%d\t%4.3f\t%d\t%4.3f\t%d\t%4.3f\t\t%d\t%d\t%d"  )
