class Solution {
public:
    vector<int> intersection(vector<vector<int>>& nums) {
        unordered_map<int, int> freq;
        vector<int> res;
        int size = nums.size();

        for (const vector<int>& arr : nums) {
            for (int n : arr) {
                freq[n]++;
            }
        }

        for (const auto& [num, count] : freq) {
            if (count == size) {
                res.push_back(num);
            }
        }

        sort(res.begin(), res.end());
        return res;
    }
};