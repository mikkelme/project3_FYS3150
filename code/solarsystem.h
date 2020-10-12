#ifndef SOLARSYSTEM_H
#define SOLARSYSTEM_H

#include "celestialbody.h"
#include "force.h"
#include "vec3.h"
#include <deque>
#include <fstream>

using namespace std;

class SolarSystem
{
public:
  //CelestrialBody &CreateBody(vec3 position, vec3 velocity, double mass);

  CelestialBody& CreateBody(string body_name, vec3 pos, vec3 vel, double mass);
  deque<CelestialBody>& bodies();
  void PrintBodies();
  void CalculateForce(Force &force);
  void WriteToFile(string filename);



private:
  deque <CelestialBody> my_bodies;
  deque <string> body_names;
  ofstream m_file;









};

#endif //SOLARSYSTEM_H
