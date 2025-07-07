struct Solution;

impl Solution {
    // Solution 1 -> Runtime 19ms
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut output: Vec<i32> = vec![];
        
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
}

fn main(){
    let target: i32 = 9;
    let nums: Vec<i32> = vec![2,11,7,15];
    let returned_out = Solution::two_sum(nums,target);
    
    // println!("{}", returned_out);
    println!("{:?}", returned_out);
}

