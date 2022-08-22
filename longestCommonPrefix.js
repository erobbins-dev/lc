exports.longestCommonPrefix = (strs) => {
   let baseWord = strs[0];
   let currMax = strs[0].length;

   for (let str of strs) {
      let i = 0;
      while (str[i] && baseWord[i] && str[i] === baseWord[i]) {
         i++;
      }
      currMax = Math.min(i, currMax);
   }

   return baseWord.slice(0, currMax);
};

