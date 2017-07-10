CXX = g++
CXXFLAGS = -g -std=c++11

#OBJS = 
SRCS = main.cpp
#HEADERS = 

all: main

main: $(SRCS)
		$(CXX) $(CXXFLAGS) $(SRCS) -o kmeansclustering

#testSuite.o: testSuite.cpp
#		$(CXX) $(CXXFLAGS) testSuite.cpp
	   
#Point.o: Point.cpp
#		$(CXX) $(CXXFLAGS) Point.cpp

#Cluster.o: Cluster.cpp
#		$(CXX) $(CXXFLAGS) Cluster.cpp
	  
#Kmeans.o: Kmeans.cpp
#		$(CXX) $(CXXFLAGS) Kmeans.cpp
        
main.o: main.cpp
		$(CXX) $(CXXFLAGS) main.cpp
		
clean:
		rm *o kmeansclustering