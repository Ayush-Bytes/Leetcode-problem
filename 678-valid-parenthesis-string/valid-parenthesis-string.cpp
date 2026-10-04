#include <string>
#include <stack>

class Solution {
public:
    bool checkValidString(std::string s) {
        std::stack<int> leftStack;
        std::stack<int> starStack;

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                leftStack.push(i);
            } else if (s[i] == '*') {
                starStack.push(i);
            } else { // s[i] == ')'
                if (!leftStack.empty()) {
                    leftStack.pop();
                } else if (!starStack.empty()) {
                    starStack.pop();
                } else {
                    return false;
                }
            }
        }

        // Remaining '(' ko matching '*' ke saath pair karo jo unke baad aate hain
        while (!leftStack.empty() && !starStack.empty()) {
            if (leftStack.top() < starStack.top()) {
                leftStack.pop();
                starStack.pop();
            } else {
                break;
            }
        }

        return leftStack.empty();
    }
};