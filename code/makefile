CPPflags = c++ -std=c++11 #c++ -O3 
LIB =  #-larmadillo -llapack -lblas
PROG = main

${PROG}: 						${PROG}.o vec3.o solarsystem.o celestialbody.o
										${CPPflags} ${PROG}.o vec3.o solarsystem.o celestialbody.o ${LIB} -o ${PROG}.exe

${PROG}.o: 					${PROG}.cpp
										${CPPflags} -c ${PROG}.cpp


vec3.o: 						vec3.cpp vec3.h
										${CPPflags} -c vec3.cpp


solarsystem.o: 			solarsystem.cpp solarsystem.h
										${CPPflags} -c solarsystem.cpp


celestialbody.o: 		celestialbody.cpp celestialbody.h
										${CPPflags} -c celestialbody.cpp
