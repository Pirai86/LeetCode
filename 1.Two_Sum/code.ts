const nums: number[] = [2, 7, 11, 15];
const target: number = 9;

// My Solution -> Runtime 31ms
function twoSum_sa(nums: number[], target: number): number[] {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (target == nums[i] + nums[j]) {
        return [i, j];
      }
    }
  }
  return []
};

function twoSum2_sa(nums: number[], target: number): number[] {
  const map = new Map<number, number>(); // value → index

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];

    if (map.has(complement)) {
      return [map.get(complement)!, i]; // ! tells TS it's non-null
    }

    map.set(nums[i], i);
  }

  // Since problem guarantees exactly one solution, no fallback needed
  throw new Error("No valid solution found");
}


console.log(twoSum_sa(nums, target))
console.log(twoSum2_sa(nums, target));