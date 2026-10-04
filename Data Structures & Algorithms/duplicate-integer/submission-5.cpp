class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // Map for seen nums
        map<int, int> seen;
        // Loop through input
        for (int num : nums) {
            // Check if num has been seen
            if (seen[num] == 0) {
                seen[num] += 1;
            } else if (seen[num] == 1) {
                return true;
            }
        }
        return false;
    }
};