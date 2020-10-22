#include "celestialbody.h"
#include <iostream>
using namespace std;



//Constructor
CelestialBody::CelestialBody(string name_input, vec3 pos_input, vec3 vel_input, double mass_input){
  name = name_input;
  position = pos_input;
  velocity = vel_input;
  mass = mass_input;
}

void CelestialBody::Fix(bool fix){
  fixed = fix;
}

void CelestialBody::Print(){
  cout << name;
  cout << "; Position: " << position;
  cout << " Velocity: " << velocity;
  cout << " Mass: " << mass << endl;
}
