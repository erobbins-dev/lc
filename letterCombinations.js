var letterCombinations = function (digits) {
   let keymaps = {
      2: 'abc',
      3: 'def',
      4: 'ghi',
      5: 'jkl',
      6: 'mno',
      7: 'pqrs',
      8: 'tuv',
      9: 'wxyz'
   }

   let combos = []

   const recurse = (str) => {
      let ndx = str.length;
      if (ndx === digits.length) {
         if (str) {
            combos.push(str)
         }
      }
      else {
         for (ltr of keymaps[digits[ndx]]) {
            recurse(str + ltr)
         }
      }
   }

   recurse('');
   return combos;
};

const testdigits = "2"
console.log(letterCombinations(testdigits))