#ifndef SOLARSYSTEM_H
#define SOLARSYSTEM_H

#include "celestialbody.h"
#include "vec3.h"
#include <vector>

using namespace std;

class SolarSystem
{
public:
  //CelestrialBody &CreateBody(vec3 position, vec3 velocity, double mass);

  CelestialBody& CreateBody(vec3 pos, vec3 vel, double mass);
  vector<CelestialBody>& bodies();
  void PrintBodies();



private:
  vector<CelestialBody> my_bodies;
  vector<string> body_names;









};

#endif
