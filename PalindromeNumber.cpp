class Solution {
public:
    bool isPalindrome(int x) {
        if (0 > x || (x % 10 == 0 && x != 0))
            return false;
        int res = 0;
        while (res < x) {
            res = (res * 10) + x % 10;
            x = x / 10;
        }
        return x == res || x == res / 10;
    }
};