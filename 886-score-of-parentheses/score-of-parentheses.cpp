class Solution {
public:
    int scoreOfParentheses(string s) {
        stack<int> st;
        st.push(0); // Base score for the current level

        for (char c : s) {
            if (c == '(') {
                st.push(0);
            } else {
                int v = st.top();
                st.pop();
                int outer = st.top();
                st.pop();
                
                // If v == 0, it means it was a "()", so score is 1.
                // Otherwise, it was "(A)", so score is 2 * v.
                int addedScore = (v == 0) ? 1 : 2 * v;
                st.push(outer + addedScore);
            }
        }

        return st.top();
    }
};