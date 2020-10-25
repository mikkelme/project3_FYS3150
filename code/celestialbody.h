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
  double kin = 0; //kinetic energy
  double pot = 0; //potential energy
  double mek = 0; //mechanical energy
  bool fixed = false; //opportunity to fix object


  CelestialBody(string name_input, vec3 pos_input, vec3 vel_input, double mass_input); //Constructor
  void Fix(bool fix);
  void Print();
  vec3 Momentum();





private:


};

#endif //CELESTIALBODY_H
