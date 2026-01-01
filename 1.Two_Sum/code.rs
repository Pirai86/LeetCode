struct Solution;
use std::collections::HashMap;

impl Solution {
    // My Solution -> Runtime 19ms
    pub fn two_sum(nums: &[i32], target: i32) -> Vec<i32> {
        let mut output = vec![];
        
        for i in 0..nums.len(){
            for j in i+1..nums.len(){
                if target == nums[i] + nums[j]{
                    output.extend([i as i32,j as i32]);
                    return output;
                }
            }
        }
        return vec![]
    }
    
    // AI Solution -> Runtime 0ms
    pub fn two_sum2(nums: &[i32], target: i32) -> Vec<i32> {
        let mut seen = HashMap::new();
    
        for (i, num) in nums.iter().enumerate() {
            let complement = target - num;
            if let Some(&j) = seen.get(&complement) {
                return vec![j as i32, i as i32];
            }
            seen.insert(num, i);
        }
        vec![]
    }
}

fn main(){
    let target: i32 = 9;
    let nums = vec![2,11,7,15];
    let returned_out = Solution::two_sum(&nums,target);
    let returned_out_2 = Solution::two_sum2(&nums,target);
    
    println!("{:?}", returned_out);
    println!("{:?}", returned_out_2);
}

