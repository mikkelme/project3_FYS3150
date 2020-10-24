#include "constants.h"
#include "solarsystem.h"
#include "celestialbody.h"
#include "solver.h"
#include "force.h"
#include "vec3.h"
#include "time.h"


using namespace std;

int main (int numArguments, char ** arguments){
  int numTimesteps = 1000;
  double dt = 0.001;
  double B = 2.0;
  double v_escape = 1;
  if (numArguments >= 2) dt = atof(arguments[1]);
  if (numArguments >= 3) numTimesteps = atoi(arguments[2]);
  // if (numArguments >= 4) B = atof(arguments[3]);
  if (numArguments >= 4) v_escape = atof(arguments[3]);


  //Initialize instance of SolarSystem
  SolarSystem my_system;
  bool Circle_Sun_Earth = false;
  bool All_planets = true;
  bool Escape_velocity = false;

  if (Circle_Sun_Earth){
    CelestialBody &Sun = my_system.CreateBody("Sun", vec3(0, 0, 0), vec3(0, 0, 0), 1.0);
    CelestialBody &Earth = my_system.CreateBody("Earth" ,vec3(1, 0, 0), vec3(0, 2*pi, 0), M_Earth/M_Sun);
    Sun.Fix(true);
  }

  if (All_planets){
    // Data accessed from ssd.jpl.nasa.gov/horizons.cgi, Time: 2020-Oct-23 00:00:00.0000 TBD
    CelestialBody &Sun = my_system.CreateBody("Sun", vec3(-6.158e-3, 6.384e-3, 9.046e-5), vec3(-7.234e-6, -5.148e-6, 2.176e-7)*yr, 1.0);
    CelestialBody &Mercury = my_system.CreateBody("Mercury", vec3(3.143e-1, 1.065e-1, -2.112e-2), vec3(-1.385e-2, 2.810e-2, 3.567e-3)*yr, M_Mercury/M_Sun);
    CelestialBody &Venus = my_system.CreateBody("Venus", vec3(-3.514e-1, 6.358e-1, 2.865e-2), vec3(-1.780e-2, -9.846e-3, 8.924e-4)*yr, M_Venus/M_Sun);
    CelestialBody &Earth = my_system.CreateBody("Earth" ,vec3(8.575e-1, 5.002e-1, 6.633e-5), vec3(-8.833e-3, 1.486e-2, 1.132e-7)*yr, M_Earth/M_Sun);
    CelestialBody &Mars = my_system.CreateBody("Mars", vec3(1.272, 6.357e-1, -1.808e-2), vec3(-5.652e-3, 1.374e-2, 4.268e-4)*yr, M_Mars/M_Sun);
    CelestialBody &Jupiter = my_system.CreateBody("Jupiter", vec3(2.601, -4.399, -3.995e-2), vec3(6.402e-3, 4.198e-3, -1.606e-4)*yr, M_Jupiter/M_Sun);
    CelestialBody &Saturn = my_system.CreateBody("Saturn", vec3(5.175, -8.540, -5.748e-2), vec3(4.461e-3, 2.875e-3, -2.273e-4)*yr, M_Saturn/M_Sun);
    CelestialBody &Uranus = my_system.CreateBody("Uranus", vec3(1.551e1, 1.226e1, -1.554e-1), vec3(-2.467e-3, 2.902e-3, 4.277e-5)*yr, M_Uranus/M_Sun);
    CelestialBody &Neptune = my_system.CreateBody("Neptune", vec3(2.941e1, -5.443, -5.658e-1), vec3(5.501e-4, 3.105e-3, -7.622e-5)*yr, M_Neptune/M_Sun);
    CelestialBody &Pluto = my_system.CreateBody("Pluto", vec3(1.384e1, -3.119e1, -6.676e-1), vec3(2.952e-3, 6.077e-4, -9.227e-4)*yr, M_Pluto/M_Sun);
    Sun.Fix(false);
  }

  if (Escape_velocity){
    CelestialBody &Sun = my_system.CreateBody("Sun", vec3(0, 0, 0), vec3(0, 0, 0), 1.0);
    CelestialBody &Earth = my_system.CreateBody("Earth" ,vec3(1, 0, 0), vec3(v_escape, 0, 0), M_Earth/M_Sun);
    Sun.Fix(true);
  }


  //Solver
  Solver my_solver(dt);
  Force my_force("Gravity");

  // Force my_force("Inverse_Beta");
  // my_force.set_beta(B);



  // clock_t start, finish; //For timing
  // start = clock(); //Start timer

  double time = 0;
  for (int timestep = 1; timestep < numTimesteps; timestep++){
    time = dt*timestep;
    //my_solver.Euler_advance(my_system, my_force, time);
    my_solver.Velocity_Verlet(my_system, my_force, time);
  }
  my_system.WriteToFile("system.data", time);

  // finish = clock();
  // double timeused = (double) (finish - start)/(CLOCKS_PER_SEC );
  // my_solver.WriteTime(timeused);

}
