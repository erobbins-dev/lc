var maxArea = function (height) {
   let l = 0, r = height.length - 1;
   let maxVol = 0;

   const getVolume = (l, r) => {
      return Math.min(height[l], height[r]) * (r - l);
   }

   while (l < r) {
      maxVol = Math.max(maxVol, getVolume(l, r))
      if (height[l] < height[r]) {
         l++;
      } else {
         r--;
      }
   }

   return maxVol;
};

let height = [1,1,3,4,2,1,0]
console.log(maxArea(height));