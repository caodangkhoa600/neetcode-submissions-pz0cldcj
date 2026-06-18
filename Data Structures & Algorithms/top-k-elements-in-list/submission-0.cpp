class Solution {
    static bool cmp(pair<int, int>& a, pair<int, int>& b) {
        return a.second > b.second;
    }

    static vector<pair<int, int>> sortmap(map<int, int>& M) {
        vector<pair<int, int>> A;

        for (auto& it : M) {
            A.push_back(it);
        }

        sort(A.begin(), A.end(), cmp);
        return A;
    }
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> result;
        map<int, int> m;
        for (int i = 0; i < nums.size(); i++) {
            if (m.count(nums[i])) {
                m[nums[i]]++;
            } else {
                m[nums[i]] = 0;
            }
        }

        vector<pair<int, int>> a = sortmap(m);

        for (auto const& x : a) {
            if (k == 0) {
                return result;
            }
            result.push_back(x.first);
            k--;
        }

        return result;
    }
};
