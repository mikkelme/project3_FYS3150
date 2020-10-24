#ifndef FORCE_H
#define FORCE_H

#include "vec3.h"
#include "celestialbody.h"
#include <functional>
using namespace std;



class Force
{
public:
  Force(string force_type);
  static void Gravity(CelestialBody &body1, CelestialBody &body2);
  static void Inverse_Beta(CelestialBody &body1, CelestialBody &body2);
  static void Relativistic_Gravity(CelestialBody &body1, CelestialBody &body2);
  void call_force(CelestialBody &body1, CelestialBody &body2);
  void set_beta(double B);

  static double Beta;


private:
  function<void(CelestialBody &body1, CelestialBody &body2)> ForceFunc; //link to force function


};

#endif //FORCE_H
