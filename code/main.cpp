#include <iostream>
#include <cmath>
#include <cstdlib>
#include "constants.h"
#include "solarsystem.h"
#include "celestialbody.h"
#include "solver.h"
#include "force.h"
#include "vec3.h"


//#include <vector>
using namespace std;

int main (int numArguments, char ** arguments){
  int numTimesteps = 1000;
  double dt = 0.001;
  if (numArguments >= 2) dt = atof(arguments[1]);
  if (numArguments >= 3) numTimesteps = atoi(arguments[2]);

  //Initialize instance of SolarSystem
  SolarSystem my_system;

  /*
  CelestialBody &Sun = my_system.CreateBody("Sun", vec3(0, 0, 0), vec3(0, 0, 0), 1.0);
  CelestialBody &Earth = my_system.CreateBody("Earth" ,vec3(1, 0, 0), vec3(0, 2*pi, 0), M_Earth/M_Sun);
<<<<<<< HEAD
  // Sun.Fix(true);
=======
  Sun.Fix(true);
  */

  // Data accessed from ssd.jpl.nasa.gov, Time: 2020-Oct-23 00:00:00.0000 TBD
  CelestialBody &Sun = my_system.CreateBody("Sun", vec3(-6.158e-3, 6.384e-3, 9.046e-5), vec3(-7.234e-6, -5.148e-6, 2.176e-7)*yr, 1.0);
  CelestialBody &Earth = my_system.CreateBody("Earth" ,vec3(8.575e-1, 5.002e-1, 6.633e-5), vec3(8.833e-3, 1.486e-2, 1.132e-7)*yr, M_Earth/M_Sun);
  CelestialBody &Jupiter = my_system.CreateBody("Jupiter", vec3(2.601, -4.399, -3.995e-2), vec3(6.402e-3, 4.198e-3, -1.606e-4)*yr, M_Jupiter/M_Sun);
  Sun.Fix(false);
>>>>>>> ca1e39d7f75482dcf69a59eeba47c1768ea64b62


  //Solver
  Solver my_solver(dt);
  Force my_force("Gravity");

  // Force my_force("Inverse_Beta");
  // double B = 3.0;
  // my_force.set_beta(B);

  double time = 0;
  for (int timestep = 1; timestep < numTimesteps; timestep++){
    time = dt*timestep;
<<<<<<< HEAD
    // my_solver.Euler_advance(my_system, my_force, time);
    my_solver.Velocity_Verlet(my_system, my_force, time);
  }
  my_system.WriteToFile("system.data", time);
=======
    //my_solver.Euler_advance(my_system, my_force);
    my_solver.Velocity_Verlet(my_system, my_force);
    my_system.WriteToFile("system.data", time);
}

>>>>>>> ca1e39d7f75482dcf69a59eeba47c1768ea64b62



  return 0;
}
