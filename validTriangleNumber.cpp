#include <iostream>
using namespace std;
#include <vector>
class Solution {
public:
    static int triangleNumber(vector<int>& nums) {
        int combinations = 0;
        if (nums.size() < 3)
            return 0;
        int first = 0, second = 1, third = 2;
        for (; first != nums.size(); first++) {
            for(; second != nums.size(); second++) {
                for(; third != nums.size(); third++) {
                    if (nums[first] != nums[second] &&
                       nums[second] != nums[third])
                        ++combinations;
                }
            }
        }
        return combinations;
    }
};

void    testCase(vector<int> tmp) {
    cout << "For ";
    for (int i = 0; i < tmp.size(); i++) {
        cout << tmp[i] << " - ";
    }
    cout << "nums, the valid combinations = " << Solution::triangleNumber(tmp) << endl;
}

int main() {
    vector<int> vect = { 10, 20, 30 };
    testCase(vect);
    vector<int> vect1 = { 4, 2, 3, 4 };
    testCase(vect1);
    vector<int> vect2 = { 2, 2, 3, 4 };
    testCase(vect2);
    vector<int> vect3 = { 1, 6, 3, 9, 7 };
    testCase(vect3);
    vector<int> vect4 = { 1, 3, 3 };
    testCase(vect4);
    return 0;
}