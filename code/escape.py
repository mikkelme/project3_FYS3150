from read_dump import *


def find_escape_velocity(folder, filename, T):
    dt  = 0.01
    numTimesteps = np.rint(T/dt + 1).astype(int)

    v_analytical = np.sqrt(2*4*np.pi**2)
    v_escape = 8.878
    v_increase = 0.0001

    escape = False
    while escape != True:
        print(f"\rTesting escape velocity: {v_escape}, expected = {v_analytical}", end = "")
        subprocess.call([folder + filename, str(dt), str(numTimesteps), str(v_escape)])
        type, time, pos, vel, energy, timesteps = read_data()
        escape = np.all(vel[:,1,0] > 0)
        v_escape += v_increase

        rel_err = abs(v_escape-v_analytical)/v_analytical

    print(f"\nEscape accomplished at: {v_escape}\nExpected: {v_analytical}\nRelativ error: {rel_err}")



folder  = "../test_files/"
filename = "EarthSun_escape.exe"
find_escape_velocity(folder, filename, 1000)
