#include "solarsystem.h"


#include <iostream>
#include <vector>
using namespace std;


//CelestrialBody& SolarSystem::CreateBody(vec3 position, vec3 velocity, double mass){


CelestialBody& SolarSystem::CreateBody(vec3 pos, vec3 vel, double mass){
  //Create instance of CelestrialBody and add to my_bodies

  my_bodies.push_back(CelestialBody(pos, vel, mass));

  string name = "Planet_Name";

  //body_names.push_back(name);
  //cout << body_names.size() << endl;
  //cout << body_names[-1] << endl;


  //vector<CelestialBody> &bodies = SolarSystem::bodies();
  //return bodies[my_bodies.size() - 1];
  //return my_bodies[my_bodies.size() - 1];
  return my_bodies.back();
}

vector<CelestialBody>& SolarSystem::bodies(){
  return my_bodies;
}

void SolarSystem::PrintBodies(){

    for (int i = 0; i < my_bodies.size(); i++){
    cout <<": Position: " << my_bodies[i].position << " Velocity: " << my_bodies[i].velocity << " Mass: " << my_bodies[i].mass <<endl;
  }

  //vector<CelestialBody> &bodies = SolarSystem::bodies();
  //for (int i = 0; i < bodies.size(); i++){
  //  CelestialBody &body = bodies[i];
  //  cout << "Position: " << body.position << " Velocity: " << body.velocity << " Mass: " << body.mass <<endl;
  //}
}
