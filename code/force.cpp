#include "force.h"
#include <iostream>


//Constructor
Force::Force(string force_type){
  if (force_type == "Gravity"){
    myFunc = Gravity;
  }
  else {
    cout << "force_type: \"" << force_type << "\" not found.\n";
    terminate();
  }

  // vector<function<void()>> actionCommand = {[](){}
  //   [this](){this->}
}

void Force::call_force(CelestialBody &body1, CelestialBody &body2){ //CelestialBody &body1, CelestialBody &body2
  myFunc(body1, body2);
}


void Force::Gravity(CelestialBody &body1, CelestialBody &body2){
  double pi = acos(-1.0);
  int G = 4*pi*pi;
  vec3 dr_vector = body1.position - body2.position;
  double dr = dr_vector.length();
  body1.force += -1*G*body1.mass*body2.mass*dr_vector/(dr*dr);
}
