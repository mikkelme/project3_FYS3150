#include "force.h"
#include "constants.h"
#include <iostream>

double Force::Beta; //Initialize Beta

//Constructor
Force::Force(string force_type){
  //Link myFunc to the chosen force function
  if (force_type == "Gravity"){ ForceFunc = Gravity;}
  else if (force_type == "Inverse_Beta"){ ForceFunc = Inverse_Beta; }
  else {
    cout << "force_type: \"" << force_type << "\" not found.\n";
    terminate();
  }
}

void Force::call_force(CelestialBody &body1, CelestialBody &body2){ ForceFunc(body1, body2); }


void Force::Gravity(CelestialBody &body1, CelestialBody &body2){
  vec3 dr_vector = body1.position - body2.position;
  double dr = dr_vector.length();
  body1.force += -1*G*body1.mass*body2.mass*dr_vector/(dr*dr*dr);
  body1.pot += -G*body1.mass*body2.mass/dr;
}


void Force::set_beta(double B){
  if (B <= 0)
  {
    cout << "Beta must be positvie and different from zero." << endl;
    terminate();
  }
  else
  {
    Beta = B;
  }
}


void Force::Inverse_Beta(CelestialBody &body1, CelestialBody &body2){
  if (Beta == 0){
    cout << "Beta has not yet been initialized with legal value.\
    \nUse class member function: Force::set_beta(double B)" << endl;
    terminate();
  }
  
  vec3 dr_vector = body1.position - body2.position;
  double dr = dr_vector.length();
  body1.force += -1*G*body1.mass*body2.mass*dr_vector/(dr*pow(dr,Beta));
}
