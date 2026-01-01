/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 2;
    int* returnedArray = malloc(sizeof(int) * (*returnSize));

    for (int i = 0; i < numsSize; i++) {
        int expectedValue = target - nums[i];
        for (int j = i + 1; j < numsSize; j++) {
            if (expectedValue == nums[j]) {
                returnedArray[0] = i;
                returnedArray[1] = j;
                return returnedArray;
            }
        }
    }
    *returnSize = 0; 
    return NULL;
}

int main(){
    int nums[] = {2,7,11,15};
    int numsSize = 4;
    int target = 9;
    int returnSize;

    int* result = twoSum(nums, numsSize, target, &returnSize);
    if(result != NULL){
        printf("indices %d %d\n", result[0], result[1]);
    }

    free(result);
    return 0;
}