from read_dump import *

def Inverse_Beta(folder, filename, beta_start, beta_end, numBeta):

    #Run conditions
    Beta = np.linspace(beta_start, beta_end, numBeta)
    dt  = 0.0001
    T = 1
    numTimesteps = np.rint(T/dt + 1).astype(int)
    planet_focus = "Earth"

    #Arrays
    abs_energy_err = np.zeros(numBeta)
    energy_cont = np.zeros((numBeta, numTimesteps))
    position = np.zeros((numBeta, numTimesteps, 2))
    radial = np.zeros((numBeta, numTimesteps))
    L = np.zeros((numBeta, numTimesteps))

    #Run file and fetch data
    for i in range(numBeta):
        print(f"Running: {filename} {dt} {numTimesteps} {Beta[i]}")
        subprocess.call([folder + filename, str(dt), str(numTimesteps), str(Beta[i])])
        type, time, pos, vel, energy, timesteps = read_data()
        planet_idx = np.argwhere(type == planet_focus)[0][0]

        abs_energy_err[i] = np.linalg.norm(energy[0, :, 2] - energy[-1, :, 2])
        energy_cont[i] = energy[:,1,2]
        position[i] = pos[:,1, 0:2]
        radial[i] = np.linalg.norm(position[i], axis = -1)
        L[i] = np.shape(np.linalg.norm(np.cross(pos[:,1], vel[:,1], axis = -1), axis = -1))


    #What to plot
    plot_pos            = False
    plot_energy         = False
    plot_energy_time    = False
    plot_radial         = False
    plot_L              = True

    if plot_pos:
        if numBeta != 16:
            print("must use 16 points here")
            exit()
        mode = "square"
        fig, ax = plt.subplots(ncols=4, nrows=4, figsize=get_fig_size(390, mode))
        plt.suptitle(f"Stability of orbit for inverse beta force\nT = {T} years, dt = {dt}")
        plt.subplots_adjust(left = 0.07, bottom = 0.05, right = 0.95, top = 0.85, hspace = 0.78)

        for i in range(numBeta):
            plt.subplot(4,4,i+1)
            plt.title(f"Beta = {Beta[i]:.2f}")
            plt.plot(position[i,:,0], position[i,:,1])
        plt.show()

    if plot_energy:
        mode = "golden"
        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=get_fig_size(390, mode))
        plt.tight_layout(pad = 3.2)

        plt.plot(Beta, abs_energy_err, label = f"{filename}")
        plt.title(f"Mechanical energy error between T = 0 and T = {T} years\ndt = {dt} yr")
        plt.xlabel("Beta")
        plt.ylabel(f"Energy error [AU^5/yr^4]")
        #plt.xscale('log')
        plt.yscale('log')
        plt.show()

    if plot_energy_time:
        mode = "3/4"
        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=get_fig_size(390, mode))
        plt.tight_layout(pad = 3.2)
        for i in range(numBeta):
            plt.plot(time, energy_cont[i], label = f"Beta = {Beta[i]:.3f}")
            plt.title(f"Total mechanical energy, dt = {dt} yr")
            plt.xlabel("T [yr]")
            plt.ylabel("E [AU^5/yr^4]")
        plt.legend()
        plt.show()


    if plot_radial:
        mode = "3/4"
        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=get_fig_size(390, mode))
        plt.tight_layout(pad = 3.2)
        for i in range(numBeta):
            plt.plot(time, radial[i], label = f"Beta = {Beta[i]:.3f}")
            plt.title(f"Radial distance to Sun with inverse beta force, dt = {dt} yr")
            plt.xlabel("T [yr]")
            plt.ylabel("Radial distance [AU]")
        plt.legend()
        plt.show()

    if plot_L:
        mode = "golden"
        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=get_fig_size(390, mode))
        plt.tight_layout(pad = 3.2)

        for i in range(numBeta):
            plt.plot(time, L[i], label = f"Beta = {Beta[i]:.3f}")
            plt.title(f"Angular momentum, dt = {dt} yr")
            plt.xlabel("T [yr]")
            plt.ylabel("L [M_sun AU^2 / yr]")
        plt.legend()
        plt.show()




folder  = "../test_files/"
filename = "EarthSun_InverseBeta_ellipse.exe"
Inverse_Beta(folder, filename, 2, 3, 8)
