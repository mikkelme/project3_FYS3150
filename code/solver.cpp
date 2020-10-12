#include "solver.h"
using namespace std;


Solver::Solver(double dt){
  my_dt = dt;
}


void Solver::Euler_advance(SolarSystem &system, Force &force){
  system.CalculateForce(force);
  
  for (CelestialBody &body : system.bodies()){
    body.velocity += body.force / body.mass * my_dt;
    body.position += body.velocity * my_dt;
  }
}
