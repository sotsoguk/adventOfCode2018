#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <unordered_set>

#include "reader.hpp"


using namespace std;

int main()
{
    ifstream ifs("input.txt", ifstream::in);
    auto lines = vector<string>(read_input(ifs));
    
    // Part 1 - parse input to ints and return total value
    auto freq = int64_t(0);
    auto values = vector<int64_t>();
    transform( begin(lines), end(lines), back_inserter(values),
                [&](string s) -> int64_t {int64_t val = stoi(s); freq += val; return val;});
    
    cout << "Part 1: " << freq << endl;

    // Part 2
    // compute partial sums, as each freq is increased by freq in each round, cyclic
    vector<int64_t> part_sums(0);
    std::partial_sum(values.begin(), values.end(), back_inserter(part_sums));
    std::unordered_set<int64_t> prevFreq;
    prevFreq.insert(0);
    auto seen = false;
    while(!seen)
    {
        for (auto& x:part_sums)
        {
            if (prevFreq.count(x) == 0)
            {
                prevFreq.insert(x);
            }
            else
            {
                std::cout << "Part 2: " << x std::endl;
                seen = true;
                break;
            }
            
            x += freq;
        }
    }
    
}
