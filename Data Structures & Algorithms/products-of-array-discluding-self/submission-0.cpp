class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int p = 1;
        bool containtZ = false;
        int numZ = 0;
        vector<int> result;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                containtZ = true;
                numZ += 1;
            } else {
                p = p * nums[i];
            }
        }
        for (int i = 0; i < nums.size(); i++) {
            if (numZ > 1) {
                result.push_back(0);
                continue;
            }
            if (containtZ) {
                if (nums[i] == 0) {
                    result.push_back(p);
                } else {
                    result.push_back(0);
                }
            } else {
                result.push_back(p / nums[i]);
            }
        }

        return result;
    }
};
