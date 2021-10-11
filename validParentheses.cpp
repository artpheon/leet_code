#include <string>
#include <stack>

using std::string;

class Solution {
public:
    bool is_open(char c) {
        return c == '[' || c == '(' || c == '{';
    }
    
    bool is_close(char c) {
        return c == '}' || c == ')' || c == ']';
    }
    
    bool is_same_type(char o, char c) {
        if (o == '[')
            return c == ']';
        else if (o == '(')
            return c == ')';
        else if (o == '{')
            return c == '}';
    }
    
    bool isValid(string s) {
        if (this->is_close(s.at(0)))
            return false;
        string brackets = "";
        for (int i = 0; i < s.size(); i++) {
            if (this->is_open(s.at(i)))
                brackets.push_back(s.at(i));
            else if (this->is_close(s.at(i))) {
                if (!this->is_same_type(brackets.back(), s.at(i)))
                    return false;
                brackets.pop_back();
            }
            else
                return false;
        }
        return brackets.empty();
    }
    bool isValid_2(string s) {
        std::stack<char> stack;
        
        if (s[0] != '[' && s[0] != '(' && s[0] != '{')
            return false;
        for (char& c: s) {
            if (c == '{' || c == '(' || c == '[')
                stack.push(c);
            else if (!stack.empty()) {
                if (stack.top() == '(' && c != ')')
                    return false;
                else if (stack.top() == '[' && c != ']')
                    return false;
                else if (stack.top() == '{' && c != '}')
                    return false;
                stack.pop();
            }
            else
                return false;
        }
        return stack.empty();
    }
};