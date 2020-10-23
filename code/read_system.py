# Super simple, can be generalized...

import numpy as np
import matplotlib.pyplot as plt

file = open('system.data')
lines = file.readlines()
num_planets = 3
n = int(len(lines)/(2+num_planets))


sun_pos = np.zeros((n,3))
sun_vel = np.zeros((n,3))
earth_pos = np.zeros((n,3))
earth_vel = np.zeros((n,3))
jupiter_pos = np.zeros((n,3))
jupiter_vel = np.zeros((n,3))

for i in range(n):
	sun_pos[i,0] = float(lines[(2+num_planets)*i+2].split()[2])
	sun_pos[i,1] = float(lines[(2+num_planets)*i+2].split()[3])
	sun_pos[i,2] = float(lines[(2+num_planets)*i+2].split()[4])
	sun_vel[i,0] = float(lines[(2+num_planets)*i+2].split()[5])
	sun_vel[i,1] = float(lines[(2+num_planets)*i+2].split()[6])
	sun_vel[i,2] = float(lines[(2+num_planets)*i+2].split()[7])

	earth_pos[i,0] = float(lines[(2+num_planets)*i+3].split()[2])
	earth_pos[i,1] = float(lines[(2+num_planets)*i+3].split()[3])
	earth_pos[i,2] = float(lines[(2+num_planets)*i+3].split()[4])
	earth_vel[i,0] = float(lines[(2+num_planets)*i+3].split()[5])
	earth_vel[i,1] = float(lines[(2+num_planets)*i+3].split()[6])
	earth_vel[i,2] = float(lines[(2+num_planets)*i+3].split()[7])

	jupiter_pos[i,0] = float(lines[(2+num_planets)*i+4].split()[2])
	jupiter_pos[i,1] = float(lines[(2+num_planets)*i+4].split()[3])
	jupiter_pos[i,2] = float(lines[(2+num_planets)*i+4].split()[4])
	jupiter_vel[i,0] = float(lines[(2+num_planets)*i+4].split()[5])
	jupiter_vel[i,1] = float(lines[(2+num_planets)*i+4].split()[6])
	jupiter_vel[i,2] = float(lines[(2+num_planets)*i+4].split()[7])

plt.plot(sun_pos[:,0],sun_pos[:,1],label='Sun')
plt.plot(earth_pos[:,0],earth_pos[:,1],label='Earth')
plt.plot(jupiter_pos[:,0],jupiter_pos[:,1],label='Jupiter')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.legend()
plt.show()
