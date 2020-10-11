#include <iostream>
#include <cmath>
#include <cstdlib>
#include "solarsystem.h"
#include "celestialbody.h"
#include "vec3.h"
using namespace std;

int main (int numArguments, char ** arguments){
  int numTimesteps = 1000;
  if (numArguments >= 2) numTimesteps = atoi(arguments[1]);
  //cout << numTimesteps << endl;

  SolarSystem my_system; //Name of class
  //my_system.test();

  CelestialBody &Earth = my_system.CreateBody(vec3(1, 2, 3), vec3(4, 5, 6), 7);
  CelestialBody &Sun = my_system.CreateBody(vec3(11, 12, 13), vec3(14, 15, 16), 17 );
  CelestialBody &Planet = my_system.CreateBody(vec3(21, 22, 23), vec3(24, 25, 26), 27 );
  //references stop working after adding more...
  //but the reference from bodies work just fine:

  Earth.Print();
  Sun.Print();
  Planet.Print();
  cout << endl;

  /*
  vector<CelestialBody> &bodies = my_system.bodies();
  cout << bodies.size() << endl;
  for (int i = 0; i < bodies.size(); i++){
    CelestialBody &body = bodies[i];
    cout << "Position: " << body.position << " Velocity: " << body.velocity << " Mass: " << body.mass <<endl;
  }
  */
  my_system.PrintBodies();







  return 0;
}
