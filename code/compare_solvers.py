from read_dump import *



def error_plot(folder, exe_files):
    planet_focus = "Earth"
    N = 5
    T = 10 #[years]
    dt = np.logspace(-1,-N,N)
    color = ["tab:blue", "tab:orange", "tab:green", "xkcd:brown"]
    color_fit = ["tab:purple", "tab:red", "tab:cyan", "xkcd:beige"]

    numTimesteps = np.rint(T/dt + 1).astype(int)
    abs_pos_err = np.zeros((len(exe_files), N))
    abs_energy_err = np.zeros((len(exe_files), N))

    mode = 2*(5**0.5 - 1)/2
    fig, ax = plt.subplots(ncols=2, nrows=1, figsize=get_fig_size(390, mode))
    plt.tight_layout(pad = 3.2)
    plt.subplots_adjust(hspace = 0.4)
    for j in range(len(exe_files)):
        for i in range(N):
            print(f"Running: {exe_files[j]} for dt = {dt[i]}, numTimesteps = {numTimesteps[i]}")
            subprocess.call([folder + exe_files[j], str(dt[i]), str(numTimesteps[i])])
            type, time, pos, vel, energy, timesteps = read_data()
            planet_idx = np.argwhere(type == planet_focus)[0][0]
            abs_pos_err[j,i] = np.linalg.norm(pos[0, planet_idx] - pos[-1, planet_idx])
            abs_energy_err[j,i] = np.linalg.norm(energy[0, :, 2] - energy[-1, :, 2])

        x = np.log(dt); y = np.log(abs_pos_err[j])
        a, b, R, p, std_a = stats.linregress(x,y)

        plt.plot(dt, abs_pos_err[j], color = color[j], linestyle = "none", marker = "o", label = f"{exe_files[j]}")
        plt.plot(dt, dt**a*np.exp(b), color = color_fit[j], linestyle = "--", label = f"Linreg: slope = {a:.2f}, std = {std_a:.2f} ")
        plt.title(f"Positional error between T = 0 and T = {T} years")
        plt.xlabel("dt [yr]")
        plt.ylabel("Pos error [AU]")
        plt.xscale('log')
        plt.yscale('log')
        plt.legend(loc = 4, prop={'size': 9})

        plt.subplot(2,1,2)
        plt.plot(dt, abs_energy_err[j], color = color[j], marker = "o", label = f"{exe_files[j]}")
        plt.title(f"Mechanical energy error between T = 0 and T = {T} years")
        plt.xlabel("dt [yr]")
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





folder  = "../test_files/"


files = ["EarthSun_Euler.exe", "EarthSun_Verlet.exe"]
error_plot(folder, files)

# timing_data = "Timeused.txt"
# files = ["Euler_timing.exe" ,"Verlet_timing.exe"]
# timing(folder, files , 7, 100, 0.001)
