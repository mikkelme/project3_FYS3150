#ifndef CELESTIALBODY_H
#define CELESTIALBODY_H

#include "vec3.h"
using namespace std;


class CelestialBody
{
public:
  string name;
  vec3 position;
  vec3 velocity;
  vec3 force;
  double mass;


  CelestialBody(string name_input, vec3 pos_input, vec3 vel_input, double mass_input); //Constructor
  void Print();
  void Change();




private:


};

#endif //CELESTIALBODY_H
