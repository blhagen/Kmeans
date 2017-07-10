/*
 * Kmeans clustering main file
 */

#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <string>

int main(int argc, char *argv[]) {

    /*
     * DEBUG
     */
    fprintf(stdout, "%d arguments.\n", argc - 1);
    for (int i = 0; i < argc - 1; i++) {
        int ct = i + 1;
        std::cout << ct << "st argument: " << argv[ct] << std::endl;
    }

    auto x = argv[2];
    auto y = argv[3];
    auto numLines = std::stoi(argv[4]);

    /* find way to only parse x, y header columns into vectors
    std::vector<double> x;
    std::vector<double> y;
    std::ifstream inputFile(argv[1]);

    std::string line;
    
    while (std::getline(inputFile, line)) {
        std::stringstream lineStream(line);
        std::string cell;

        while (std::getline(lineStream, cell, ',')) {

        }

    }

    */



    return 0;
}