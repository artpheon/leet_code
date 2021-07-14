#include <vector>
#include <iostream>

using namespace std;

void printVector(vector<int>& vect) {
    std::cout << "v = { ";
    for (int n : vect) {
        std::cout << n << ", ";
    }
    std::cout << "}; \n";
}

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int>::iterator it = nums.begin(), ite = nums.end();
        int first = 0, last = 0;
        for (;it != ite; it++) {
            last = getInd(nums, target - nums[first]);
            if (last != -1 && last != first)
                break ;
            ++first;
        }
        vector<int> result = {first, last};
        return result;
    }

    int getInd(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            if (nums.at(i) == target)
                return i;
        }
        return -1;
    }
};


int main() {
    Solution solution;
    vector<int> vectTest1 = {2, 7, 11, 15};
    vector<int> vectTest2 = {3, 2, 4};
    vector<int> vectTest3 = {0, 2, 4, 9, 5, 13};
    vector<int> res1 = solution.twoSum(vectTest1, 9);
    vector<int> res2 = solution.twoSum(vectTest2, 6);
    vector<int> res3 = solution.twoSum(vectTest3, 14);
    cout << "Indexes are: " << res1[0] << " and " << res1[1] << endl;
    cout << "Indexes are: " << res2[0] << " and " << res2[1] << endl;
    cout << "Indexes are: " << res3[0] << " and " << res3[1] << endl;
}