import numpy as np
import matplotlib.pyplot as plt
import subprocess
from scipy import stats


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


def get_fig_size(fig_widt_pt, mode):
        """ Get appropriate fig sizes for latex
            depending on textwidth in property  """
        ratio = {"golden": (5**0.5 - 1)/2, "square": 1, "3/4": 0.75}
        in_per_pt = 1/72.27
        fig_width_in = fig_widt_pt*in_per_pt

        if isinstance(mode,str):
            fig_height_in = fig_width_in*ratio[mode]
        else:
            fig_height_in = fig_width_in*mode

        fig_dim = (fig_width_in, fig_height_in)

        return fig_dim

def set_margins(mode):
    if mode == "golden":
        plt.subplots_adjust(left = 0.14, bottom = 0.15, right = 0.93, top = 0.86)
    if mode == "square":
        plt.subplots_adjust(left = 0.15, bottom = 0.10, right = 0.88, top = 0.90)
    if mode == "3/4":
        plt.subplots_adjust(left = 0.15, bottom = 0.13, right = 0.94, top = 0.87)



def get_color(idx):
    color_list = ["tab:red", "tab:blue", "tab:orange"]
    return color_list[idx]

def plot_pos(pos, timesteps, planets, axis, solver):
    mode = "square"
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=get_fig_size(390, mode))
    plt.tight_layout(pad = 3.2)
    #set_margins(mode)

    coord = ["x [AU]", "y [AU]", "z [AU]"]
    for i in planets:
        print(i)
        pos_x = pos[timesteps, i, axis[0]]
        pos_y = pos[timesteps, i, axis[1]]
        if np.all(pos_x == pos_x[0]) and np.all(pos_y == pos_y[0]):
            plt.plot(pos_x, pos_y, color = get_color(i), linestyle = "none", marker = 'o', label = type[i])
        else:
            plt.plot(pos_x, pos_y, color = get_color(i), label = type[i])
    plt.legend()
    plt.title(f"2D Position of celestial objects. Simulation time = {time[-1]:.2f} yr\
    \nSolver = {solver:s},  dt = {time[1]-time[0]}")
    plt.xlabel(coord[0])
    plt.ylabel(coord[1])
    plt.axis("equal")
    plt.show()

def run_cpp(exe_file, dt, numTimesteps):
    """ Run program """
    subprocess.call([exe_file, str(dt), str(numTimesteps)])


def error_plot(files):
    folder = "../test_files/"
    planet_focus = "Earth"
    N = 5
    T = 10 #[years]
    dt = np.logspace(-1,-N,N)
    color = ["tab:blue", "tab:orange"]
    color_fit = ["tab:purple", "tab:red"]

    numTimesteps = np.rint(T/dt + 1).astype(int)
    abs_pos_err = np.zeros((len(files), N))
    abs_energy_err = np.zeros((len(files), N))

    mode = 2*(5**0.5 - 1)/2
    fig, ax = plt.subplots(ncols=2, nrows=1, figsize=get_fig_size(390, mode))
    plt.tight_layout(pad = 3.2)
    plt.subplots_adjust(hspace = 0.4)
    for j in range(len(files)):
        for i in range(N):
            print(f"Running: {files[j]} for dt = {dt[i]}, numTimesteps = {numTimesteps[i]}")
            run_cpp(folder + files[j], dt[i], numTimesteps[i])
            type, time, pos, vel, energy, timesteps = read_data()
            planet_idx = np.argwhere(type == planet_focus)[0][0]
            abs_pos_err[j,i] = np.linalg.norm(pos[0, planet_idx] - pos[-1, planet_idx])
            abs_energy_err[j,i] = np.linalg.norm(energy[0, :, 2] - energy[-1, :, 2])

        plt.subplot(2,1,1)

        x = np.log(dt); y = np.log(abs_pos_err[j])
        a, b, R, p, std_a = stats.linregress(x,y)

        plt.plot(dt, abs_pos_err[j], color = color[j], linestyle = "none", marker = "o", label = f"{files[j]}")
        plt.plot(dt, dt**a*np.exp(b), color = color_fit[j], linestyle = "--", label = f"Linreg: slope = {a:.2f}, std = {std_a:.2f} ")
        plt.title(f"Positional error between T = 0 and T = {T} years")
        plt.xlabel("dt [1/yr]")
        plt.ylabel("Pos error [AU]")
        plt.xscale('log')
        plt.yscale('log')
        plt.legend(loc = 4, prop={'size': 9})

        plt.subplot(2,1,2)
        plt.plot(dt, abs_energy_err[j], color = color[j], marker = "o", label = f"{files[j]}")
        plt.title(f"Mechanical energy error between T = 0 and T = {T} years")
        plt.xlabel("dt [1/yr]")
        plt.ylabel(f"Energy error [AU^5/yr^4]")
        plt.xscale('log')
        plt.yscale('log')
        plt.legend()
    plt.show()


def timing(folder, exe_files, exp_max, exp_num, dt):
    color = ["tab:blue", "tab:orange"]
    color_fit = ["tab:purple", "tab:red"]
    exponent = np.linspace(1, exp_max, exp_num)
    data = np.zeros((len(exe_files), exp_num))

    mode = "3/4"
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=get_fig_size(390, mode))
    plt.tight_layout(pad = 3.2)

    for i in range(len(exe_files)):
        timing_data = "Timeused.txt"
        with open(timing_data, "w") as infile:
            infile.write("")

        print(f"Running: \"{exe_files[i]} {dt} N\"  for N: [10:10^{exp_max:d}]\nn: ", end = "")
        for n in exponent: #Run Jacobi_solver for different dimensions n
            subprocess.call([folder + exe_files[i], str(dt), str(int(10**n))])
            print(f"\r n: 10^{n:.2f}/{exp_max}", end = "")
        print("\nDone")

        with open(timing_data, "r") as infile:
            j = 0
            for line in infile:
                data[i,j] = float(line)
                j+= 1


        x = np.log(10**exponent); y = np.log(data[i])
        a, b, R, p, std_a = stats.linregress(x,y)

        plt.plot(10**exponent, data[i], color = color[i], linestyle = "none", marker = "o", label = exe_files[i])
        plt.plot(10**exponent, 10**exponent**a*np.exp(b), color = color_fit[i], linestyle = "-", label = f"Linreg: slope = {a:.2f}, std = {std_a:.3f} ")
    plt.title("Timing of algorithms (without writing to data)")
    plt.xlabel("Number of timesteps")
    plt.ylabel("Time used [s]")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    plt.show()




# folder  = "../test_files/"
# files = ["Euler_timing.exe" ,"Verlet_timing.exe"]
# timing(folder, files , 7, 100, 0.001)
# timing_data = "Timeused.txt"



# # run_cpp("../test_files/EarthSun_Euler.exe", 0.001, 10000)
# # type, time, pos, vel, energy, timesteps = read_data()
# #
# # solver = "Velocity Verlet"
# # solver = "Euler"
# plot_pos(pos, timesteps, [0,1], [0,1], solver)




files = ["EarthSun_Euler.exe", "EarthSun_Verlet.exe"]#, "EarthSun_Verlet_SunFree.exe"]
error_plot(files)
