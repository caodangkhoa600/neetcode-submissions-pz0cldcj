class Solution {
public:
   
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        unordered_map<string, vector<string>> m;

        for (int i = 0; i < strs.size(); i++)
        {
            string sorted = strs[i];
            sort(sorted.begin(), sorted.end());
            m[sorted].push_back(strs[i]);
        }

        for (auto &p : m)
        {
            result.push_back(p.second);
        }

        return result;
    }
};
