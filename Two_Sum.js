let nums = [2,7,11,15], target = 9
for (let j=0;j<nums.length;j++){
    for (let i = 1;i<nums.length;i++){
        if ((nums[j]+nums[i]===target)&&(j!==i))
        {
            return [j,i];
        }

    }
}