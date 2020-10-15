#ifndef SOLVER_H
#define SOLVER_H

#include "solarsystem.h"
#include "force.h"

class Solver
{
public:
  double my_dt;

  Solver(double dt);
  void Euler_advance(SolarSystem &system, Force &force);
  void Velocity_Verlet(SolarSystem &system, Force &force);

};

#endif //SOLVER_H
