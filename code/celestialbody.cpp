#include "celestialbody.h"

#include <iostream>
using namespace std;


//CelestrialBody& SolarSystem::CreateBody(vec3 position, vec3 velocity, double mass){

CelestialBody::CelestialBody(vec3 pos_input, vec3 vel_input, double mass_input){
  cout << "Creating body" << endl;

  position = pos_input;
  velocity = vel_input;
  mass = mass_input;
}

void CelestialBody::Print(){
  cout << "Position: " << position;
  cout << " Velocity: " << velocity;
  cout << " Mass: " << mass << endl;
}

void CelestialBody::Change(){
    mass = 0;

}
