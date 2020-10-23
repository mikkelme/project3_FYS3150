#include "solver.h"
using namespace std;


Solver::Solver(double dt){
  my_dt = dt;
}


void Solver::Euler_advance(SolarSystem &system, Force &force, double time){
  system.CalculateForceEnergy(force);
  system.WriteToFile("system.data", time);

  for (CelestialBody &body : system.bodies()){
    body.position += body.velocity * my_dt;
    body.velocity += body.force / body.mass * my_dt;
  }
}

void Solver::Velocity_Verlet(SolarSystem &system, Force &force, double time){
	system.CalculateForceEnergy(force);
  system.WriteToFile("system.data", time);

	for (CelestialBody &body : system.bodies()){
		vec3 old_a = body.force / body.mass;
		body.position += body.velocity*my_dt + body.force / body.mass *(my_dt*my_dt*0.5);
		system.CalculateForceEnergy(force); // new acceleration
		body.velocity += (old_a + body.force / body.mass)*(my_dt*0.5);
	}
}
