#include "reader.hpp"
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <fstream>

int main()
{
    std::ifstream ifs("input.txt", std::ifstream::in);
    auto input = std::vector<std::string>(read_input(ifs));

    //Part 1, count 2 and threes of any letter
    auto twos = 0;
    auto threes = 0;
    for (auto l: input)
    {
        auto twoFound = false;
        auto threeFound = false;
        auto uniqueLetters = std::set<char>(begin(l), end(l));
        for (auto c: uniqueLetters)
        {
            if (count(begin(l), end(l),c) == 2) twoFound = true;
            if (count(begin(l), end(l),c) == 3) threeFound = true;
        }
        twoFound && twos++;
        threeFound && threes++;
    }
    std::cout<<"Part 1: Checksum: " << twos * threes << std::endl;
}

