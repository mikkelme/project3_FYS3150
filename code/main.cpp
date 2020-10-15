#include <iostream>
#include <cmath>
#include <cstdlib>
#include "solarsystem.h"
#include "celestialbody.h"
#include "solver.h"
#include "force.h"
#include "vec3.h"


//#include <vector>
using namespace std;

int main (int numArguments, char ** arguments){
  int numTimesteps = 1000;
  if (numArguments >= 2) numTimesteps = atoi(arguments[1]);


  SolarSystem my_system; //Initialize instance of SolarSystem

  double pi = acos(-1.0);
  double M_Sun = 1.989e30;
  double M_Earth = 5.972e24;

  //Create Celestial Bodies
  CelestialBody &Sun = my_system.CreateBody("Sun", vec3(0, 0, 0), vec3(0, 0, 0), 1.0);
  CelestialBody &Earth = my_system.CreateBody("Earth" ,vec3(1, 0, 0), vec3(0, 2*pi, 0), M_Earth/M_Sun);
  //my_system.PrintBodies();


  // Must be smaller if Forward Euler is used
  double dt = 0.01;
  Solver my_solver(dt);
  Force my_force("Gravity");



   for (int timestep = 0; timestep < numTimesteps; timestep++){
       //my_solver.Euler_advance(my_system, my_force);
       my_solver.Velocity_Verlet(my_system,my_force);
       my_system.WriteToFile("system.data");
  }










  return 0;
}
