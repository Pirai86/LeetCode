var nums = [2, 7, 11, 15];
var target = 9;

// My Solution -> Runtime 32ms
function twoSum(nums, target) {
    for (var i = 0; i < nums.length; i++) {
        for (var j = i + 1; j < nums.length; j++) {
            if (target == nums[i] + nums[j]) {
                return [i, j];
            }
        }
    }
};

// AI Solution -> Runtime 3ms
function twoSum2(nums, target) {
  const seen = new Map();

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];

    if (seen.has(complement)) {
      return [seen.get(complement), i];
    }

    seen.set(nums[i], i);
  }

  return [];
}

console.log(twoSum(nums, target));
console.log(twoSum2(nums, target));
