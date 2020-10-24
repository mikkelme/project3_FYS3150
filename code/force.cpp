#include "force.h"
#include "constants.h"
#include <iostream>
#include <iomanip>

double Force::Beta; //Initialize Beta

//Constructor
Force::Force(string force_type){
  //Link myFunc to the chosen force function
  if (force_type == "Gravity"){ForceFunc = Gravity;}
  else if (force_type == "Inverse_Beta"){ForceFunc = Inverse_Beta;}
  else if (force_type == "Relativistic"){ForceFunc = Relativistic_Gravity;}
  else {
    cout << "force_type: \"" << force_type << "\" not found.\n";
    terminate();
  }
}

void Force::call_force(CelestialBody &body1, CelestialBody &body2){ ForceFunc(body1, body2); }


void Force::Gravity(CelestialBody &body1, CelestialBody &body2){
  vec3 dr_vector = body1.position - body2.position;
  double dr = dr_vector.length();
  body1.force += -G*body1.mass*body2.mass*dr_vector/(dr*dr*dr);

  double speed = body1.velocity.length();
  body1.kin = 0.5*body1.mass*speed*speed;
  body1.pot += -G*body1.mass*body2.mass/dr;
  body1.mek = body1.kin + body1.pot;
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

  double speed = body1.velocity.length();
  body1.kin = 0.5*body1.mass*speed*speed;
  body1.pot += -G*body1.mass*body2.mass/((Beta-1) * pow(dr,Beta-1));
  body1.mek = body1.kin + body1.pot;
}

void Force::Relativistic_Gravity(CelestialBody &body1, CelestialBody &body2){
  vec3 dr_vector = body1.position - body2.position;
  double dr = dr_vector.length();
  double l = (dr_vector.cross(body1.velocity)).length();

  body1.force += -G*body1.mass*body2.mass*dr_vector/(dr*dr*dr)*(1 + 3*l*l/(dr*dr*c*c));

  double speed = body1.velocity.length();
  body1.kin = 0.5*body1.mass*speed*speed;
  body1.pot += -G*body1.mass*body2.mass/dr; //unsure of this ...have to recalculate for new force
  body1.mek = body1.kin + body1.pot;
  // double correction = 1 + 3*l*l/(dr*dr*c*c);
  // cout << std::setprecision(10) << correction << endl;
}







//
