#ifndef CELESTIALBODY_H
#define CELESTIALBODY_H

#include "vec3.h"

class CelestialBody
{
public:
  vec3 position;
  vec3 velocity;
  vec3 force;
  double mass;


  CelestialBody(vec3 pos_input, vec3 vel_input, double mass_input);
  void Print();
  void Change();



private:


};

#endif
