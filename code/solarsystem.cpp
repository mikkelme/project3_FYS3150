#include "solarsystem.h"
#include <iostream>
#include <deque>
#include <cmath>
using namespace std;


//CelestrialBody& SolarSystem::CreateBody(vec3 position, vec3 velocity, double mass){


CelestialBody& SolarSystem::CreateBody(string body_name, vec3 pos, vec3 vel, double mass){
  //Create instance of CelestrialBody
  //adds object to my_bodies and body_name to body_names
  cout << "Creating body: " << body_name << endl;
  my_bodies.push_back(CelestialBody(body_name, pos, vel, mass));
  body_names.push_back(body_name);


  return my_bodies.back();
}

deque<CelestialBody>& SolarSystem::bodies(){
  return my_bodies;
}

void SolarSystem::PrintBodies(){
    for (int i = 0; i < my_bodies.size(); i++){
    cout << body_names[i] <<"; Position: " << my_bodies[i].position;
    cout << " Velocity: " << my_bodies[i].velocity;
    cout << " Mass: " << my_bodies[i].mass << endl;
  }
}


void SolarSystem::CalculateForce(Force &force){

  for (CelestialBody &body : my_bodies){
    //Set forces to zero for alle bodies
    body.force = vec3{0,0,0};
  }
  double pi = acos(-1.0);
  double G = 4*pi*pi;
  int N = my_bodies.size();
  for (int i = 0; i < N; i++){
    CelestialBody &body1 = my_bodies[i];
    for (int j = i+1; j < N; j++){
        CelestialBody &body2 = my_bodies[j];
        force.call_force(body1, body2);
        force.call_force(body2, body1);
    }
  }
}

void SolarSystem::CalculateEnergy(){
  //Calculate: kinetic, potential energy and total mechanical energy
}

void SolarSystem::WriteToFile(string filename){
  if (!m_file.good()){
    m_file.open(filename.c_str(), ofstream::out);
    if (!m_file.good()){
      cout << "Error opening file" << filename << ". Aborting!" << endl;
      terminate();
    }
  }

  m_file << my_bodies.size() << endl;
  m_file << "id type x y z vx vy vz" << endl;
  for (int i=0; i < my_bodies.size(); i++){
    CelestialBody &body = my_bodies[i];
    m_file << i << " ";
    m_file << body.name << " ";
    m_file << body.position.x() << " ";
    m_file << body.position.y() << " ";
    m_file << body.position.z() << " ";
    m_file << body.velocity.x() << " ";
    m_file << body.velocity.y() << " ";
    m_file << body.velocity.z() << endl;
  }
}






//
