class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> mp;

        for(char c : s){
            if(mp[c]){
                mp[c]++;
            }
            else{
                mp[c] = 1;
            }
        }

        for(char c : t){
            if(mp[c] > 0){
                mp[c]--;
            }
            else{
                return false;
            }
        }

        for(char c : s){
            if(mp[c]!=0){
                return false;
            }
        }
        return true;
    }
};
