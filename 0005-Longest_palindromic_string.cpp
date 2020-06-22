// Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

// Example 1:

// Input: "babad"
// Output: "bab"
// Note: "aba" is also a valid answer.
// Example 2:

// Input: "cbbd"
// Output: "bb"

class Solution {
public:
  string longestPalindrome(string s) {
    string res;
    for (int i = 0; i < s.size(); i++) {
      string s1 = palindrome(s, i, i);
      string s2 = palindrome(s, i, i+1);
      //res = longest(res, s1, s2)
      res = res.size() > s1.size() ? res : s1;
      res = res.size() > s2.size() ? res : s2;
    }
    return res;
  }

  string palindrome(string& s, int l, int r){
    while (l >= 0 && r < s.size() && s[l] == s[r]){
      l--;
      r++;
    }
    return s.substr(l+1, r-l-1);
  }
};
