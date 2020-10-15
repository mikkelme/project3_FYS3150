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

void Solver::Velocity_Verlet(SolarSystem &system, Force &force){
	system.CalculateForce(force);

	for (CelestialBody &body : system.bodies()){
		vec3 old_a = body.force / body.mass;
		body.position += body.velocity*my_dt + body.force / body.mass *(my_dt*my_dt*0.5);
		system.CalculateForce(force); // new acceleration
		body.velocity += (old_a + body.force / body.mass)*(my_dt*0.5);
	}
}
