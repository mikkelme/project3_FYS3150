import numpy as np
import matplotlib.pyplot as plt
import subprocess
from scipy import stats
from scipy.signal import argrelextrema


def read_data_big(filename = "system.data"):

    type =  []
    time =  []
    pos =   []

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
    dt = 0.000001
    numTimesteps = np.rint(T/dt + 1).astype(int)
    #run_simulation(folder, exe_file, dt, numTimesteps)

    type, pos, time = read_data_big("newton_precession.data")
    planet_idx = np.argwhere(type == planet_focus)[0][0]


    r = np.linalg.norm(pos[:,planet_idx], axis = -1)
    minema = argrelextrema(r, np.less)
    minema = minema[0][np.argwhere(r[minema] < 0.35)].T[0]
    #new_minema = argrelextrema(r[minema], np.less)
    #correction
    tol = 1000
    keepers = []
    for i in range(0, len(minema)):
        if i < 1:
            if minema[i] > tol:
                keepers.append(minema[i])
        else:
            if minema[i] > tol:
                diff =  abs(minema[i] - minema[i-1])
                if diff > tol:
                    keepers.append(minema[i])

    minema = np.array(keepers)



    # maxima = argrelextrema(r, np.greater)
    # maxima = maxima[0][np.argwhere(r[maxima] > 0.35)].T[0]


    numOrbits = len(minema)
    angle = np.zeros(numOrbits)
    for i in range(numOrbits):
        xp = pos[minema][i, planet_idx, 0]
        yp = pos[minema][i, planet_idx, 1]
        angle[i] = np.arctan(yp/xp)

    # plt.plot(pos[:,planet_idx,0], pos[:,planet_idx,1])
    # plt.legend()
    # plt.show()

    angle *= 360/(2*np.pi)*3600 #convertion from radians to arcseconds
    dAngle = angle[-1]
    #np.save("Newton_angle.npy", angle)
    plt.plot(angle)
    plt.show()
    effective_time = time[minema][-1]
    numOrbits = len(minema)
    print(f"effective time = {effective_time}, number of orbits = {numOrbits}")
    plt.plot(time, r)
    plt.plot(time[minema], r[minema], 'o')
    plt.show()







folder  = "../test_files/"
exe_file = "MercurySun_precession.exe"

# exe_file = "MarcurySun_precession_normalG.exe"
# exe_file = "MercurySun_precessionSunFree.exe"
print("Began program")
measure_precession(folder, exe_file)






angle = np.load("Newton_angle.npy")
orbits = np.linspace(1,len(angle),len(angle))


a, b, R, p, std_a = stats.linregress(orbits,angle)
plt.title("Mercury perihelion precession during 100 years\nNewtonian force, dt = 1e-6")
plt.plot(orbits, angle, "o", label = "datapoints")
plt.plot(orbits, orbits*a + b, label = f"linreg: slope = {a:g}, std = {std_a:g}")
plt.xlabel("Orbits")
plt.ylabel("Perihelion preccesion [\"]")
plt.legend()
plt.show()
const = 419/99.90366*100
print(f"result = {a*const} +- {std_a*const}")
