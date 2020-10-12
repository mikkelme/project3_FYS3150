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


private:

};

#endif //SOLVER_H
