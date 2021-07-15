/*
Given a signed 32-bit integer x,
return x with its digits reversed.
If reversing x causes the value to go outside
the signed 32-bit integer range [-231, 231 - 1],
then return 0.
*/

#include <iostream>
#include <limits.h>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        
        int ret = 0;
        while (x != 0) {
            if (2147483647 / 10 < ret ||
            -2147483648 / 10 > ret)
                return 0;
            ret = (ret * 10) + (x % 10);
            x /= 10;
        }
        return ret;
    }
};


int main() {
    Solution sol;
    cout << "Test case 1: " << sol.reverse(2147483647) << endl;
    cout << "Test case 2: " << sol.reverse(0) << endl;
    cout << "Test case 3: " << sol.reverse(1) << endl;
    cout << "Test case 4: " << sol.reverse(-1) << endl;
    cout << "Test case 5: " << sol.reverse(123) << endl;
    cout << "Test case 6: " << sol.reverse(68745) << endl;
    cout << "Test case 7: " << sol.reverse(+156) << endl;
    cout << "Test case 8: " << sol.reverse(-100) << endl;
    cout << "Test case 9: " << sol.reverse(-2147483648) << endl;
    cout << "Test case 10: " << sol.reverse(746384741) << endl;
    cout << "Test case 11: " << sol.reverse(-1463847412) << endl;
    return 0;
}