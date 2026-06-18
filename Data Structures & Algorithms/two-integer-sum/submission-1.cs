public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var set = new Dictionary<int, int>();
        var result = new int[] {0, 0};
        
        for (int i = 0; i < nums.Length; i++)
        {
            // if existed in dict
            if (set.TryGetValue(target - nums[i], out var value))
            {
                result[0] = value;
                result[1] = i;
                break;
            }
            else
            {
                if (!set.ContainsKey(nums[i]))
                {
                    set.Add(nums[i], i);
                }
            }
        }

        return result;
    }
}
