import numpy as np

filename = "system.data"
infile = open(filename, "r")
lines = infile.readlines()
numPlanets = int(lines[0])
numTimesteps = int(len(lines)/(2+N))
#to be continued 
