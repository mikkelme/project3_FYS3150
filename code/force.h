#ifndef FORCE_H
#define FORCE_H

#include "vec3.h"
#include "celestialbody.h"
using namespace std;



class Force
{
public:
  Force(string force_type);
  static void Gravity(CelestialBody &body1, CelestialBody &body2);
  void call_force(CelestialBody &body1, CelestialBody &body2);


//private:
  //function<void(CelestialBody &body1, CelestialBody &body2)> myFunc; //link to force function

};

#endif //FORCE_H
