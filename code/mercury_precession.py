import numpy as np
import matplotlib.pyplot as plt
import subprocess
from scipy import stats
from scipy.signal import argrelextrema


def read_data(filename = "system.data"):
    infile = open(filename, "r")
    lines = infile.readlines()

    numPlanets = int(lines[0])
    numTimesteps = int(len(lines)/(2+numPlanets))
    numColon = len(lines[1].split())
    timesteps = np.linspace(0, numTimesteps-1, numTimesteps).astype(int)

    type = []                                           #Planet name
    time = np.zeros(numTimesteps)
    pos = np.zeros((numTimesteps, numPlanets, 3))       #x, y, z
    vel = np.zeros((numTimesteps, numPlanets, 3))       #vx, vy, vz
    energy = np.zeros((numTimesteps, numPlanets, 3))    #E_kin, E_pot, E_mek

    #Fill in planets names
    for i in range(2, numPlanets + 2):
        type.append(lines[i].split()[1])

    #Fill in other data
    for i in timesteps:
        time[i] = lines[(2+numPlanets)*i+2].split()[-1]
        for j in range(numPlanets):
            data = np.array(lines[(2+numPlanets)*i+2 + j].split()[2:]).astype(float)
            pos[i, j] = data[0:3]
            vel[i, j] = data[3:6]
            energy[i, j] = data[6:9]

    return np.array(type), time, pos, vel, energy, timesteps


def run_simulation(folder, exe_file, dt, numTimesteps):
    subprocess.call([folder + exe_file, str(dt), str(numTimesteps)])


def measure_precession(folder, exe_file):

    planet_focus = "Mercury"

    T = 100
    dt = 0.00001

    T = 10
    dt = 0.001
    # dt = 0.0000001
    numTimesteps = np.rint(T/dt + 1).astype(int)

    run_simulation(folder, exe_file, dt, numTimesteps)
    type, time, pos, vel, energy, timesteps = read_data()
    planet_idx = np.argwhere(type == planet_focus)[0][0]
    r = np.linalg.norm(pos[:,planet_idx], axis = -1)
    minema = argrelextrema(r, np.less)
    minema = minema[0][np.argwhere(r[minema] < 0.35)].T[0]


    maxima = argrelextrema(r, np.greater)
    maxima = maxima[0][np.argwhere(r[maxima] > 0.35)].T[0]


    numOrbits = len(minema)
    angle = np.zeros(numOrbits)
    for i in range(numOrbits):
        xp = pos[minema][i, planet_idx, 0]
        yp = pos[minema][i, planet_idx, 1]
        print(xp, yp)
        plt.plot(xp, yp, 'o', label = i)
        angle[i] = np.arctan(yp/xp)

    plt.plot(pos[:,planet_idx,0], pos[:,planet_idx,1])
    plt.legend()
    plt.show()
    angle *= 360/(2*np.pi)*3600 #convertion from radians to arcseconds
    dAngle = angle[-1]

    #/numOrbits
    plt.plot(angle)
    plt.show()
    effective_time = time[minema][-1]
    print(effective_time)
    # print(dAngle)
    print("Shift pr. century: ", dAngle/effective_time*100)


    plt.plot(time, r)
    plt.plot(time[minema], r[minema], 'o')
    plt.show()







folder  = "../test_files/"
exe_file = "MercurySun_precession.exe"
# exe_file = "MarcurySun_precession_normalG.exe"
# exe_file = "MercurySun_precessionSunFree.exe"
measure_precession(folder, exe_file)




#
