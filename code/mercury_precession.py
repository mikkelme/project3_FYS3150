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
    infile.close()
    return np.array(type), time, pos, vel, energy, timesteps

def read_data_big(filename = "system.data"):

    type = []                                           #Planet name
    time = []
    pos = []       #x, y, z

    with open(filename, "r") as infile:
        line = infile.readline()
        numPlanets = int(line)
        infile.readline()
        #Fill in planets name on first timestep
        pos_holder = np.zeros((numPlanets,3))
        for i in range(numPlanets):
            line = infile.readline()
            data = np.array(line.split()[2:]).astype(float)
            type.append(line.split()[1])
            pos_holder[i] = data[0:3]
        pos.append(pos_holder)
        time.append(data[-1])

        #Fill in other data for the remaing timesteps

        counter = 1
        for line in infile:
            print(f"\r timestep: {counter}", end = "")
            next(infile)
            pos_holder = np.zeros((numPlanets,3))
            for i in range(numPlanets):
                line = infile.readline()
                data = np.array(line.split()[2:]).astype(float)
                pos_holder[i] = data[0:3]
            time.append(data[-1])
            pos.append(pos_holder)
            counter += 1
            # if counter == 1000000:
            #     break
        pos = np.array(pos)
        time = np.array(time)
        print("\nDone")


        return np.array(type), pos, time



def run_simulation(folder, exe_file, dt, numTimesteps):
    print("run denied")
    exit()
    subprocess.call([folder + exe_file, str(dt), str(numTimesteps)])


def measure_precession(folder, exe_file):

    planet_focus = "Mercury"

    T = 100
<<<<<<< HEAD
    dt = 0.000001
    numTimesteps = np.rint(T/dt + 1).astype(int)

    #run_simulation(folder, exe_file, dt, numTimesteps)
    print("reading data")
    type, time, pos, vel, energy, timesteps = read_data()
    print("data read")
=======
    dt = 0.00001

    T = 10
    dt = 0.001
    numTimesteps = np.rint(T/dt + 1).astype(int)

    #run_simulation(folder, exe_file, dt, numTimesteps)
    type, pos, time = read_data_big("GR_precession.data")
>>>>>>> 8e57b985dc11cd6e6dd3b55f05307ba65ba01202
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
<<<<<<< HEAD
        # plt.plot(xp, yp, 'o', label = i)
=======
>>>>>>> 8e57b985dc11cd6e6dd3b55f05307ba65ba01202
        angle[i] = np.arctan(yp/xp)

    # plt.plot(pos[:,planet_idx,0], pos[:,planet_idx,1])
    # plt.legend()
    # plt.show()
    angle *= 360/(2*np.pi)*3600 #convertion from radians to arcseconds
    dAngle = angle[-1]
    np.save("angle", angle)


<<<<<<< HEAD

    # plt.plot(angle)
    # plt.show()
=======
    plt.plot(angle)
    plt.show()
>>>>>>> 8e57b985dc11cd6e6dd3b55f05307ba65ba01202
    effective_time = time[minema][-1]
    print(effective_time)
    # print(dAngle)
    print("Shift pr. century: ", dAngle/effective_time*100)

<<<<<<< HEAD

    # plt.plot(time, r)
    # plt.plot(time[minema], r[minema], 'o')
    # plt.show()
=======
    numOrbits = len(minema)
    print(numOrbits)
    plt.plot(time, r)
    plt.plot(time[minema], r[minema], 'o')
    plt.show()
>>>>>>> 8e57b985dc11cd6e6dd3b55f05307ba65ba01202







folder  = "../test_files/"
exe_file = "MercurySun_precession.exe"

# exe_file = "MarcurySun_precession_normalG.exe"
# exe_file = "MercurySun_precessionSunFree.exe"
<<<<<<< HEAD
print("Began program")
measure_precession(folder, exe_file)


=======
#measure_precession(folder, exe_file)
>>>>>>> 8e57b985dc11cd6e6dd3b55f05307ba65ba01202

#
angle = np.load("GR_angle.npy")
orbits = np.linspace(1,419,419)


a, b, R, p, std_a = stats.linregress(orbits,angle)
plt.title("Mercury perihelion precession during 100 years, dt = 1e-6")
plt.plot(orbits, angle, "o", label = "datapoints")
plt.plot(orbits, orbits*a + b, label = f"linreg: slope = {a:g}, std = {std_a:g}")
plt.xlabel("Orbits")
plt.ylabel("Perihelion preccesion [\"]")
plt.legend()
plt.show()
const = 419/99.90366*100
print(f"result = {a*const} +- {std_a*const}")

#
