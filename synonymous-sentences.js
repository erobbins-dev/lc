/**
 * @param {string[][]} synonyms
 * @param {string} text
 * @return {string[]}
 */
exports.generateSentences = function (synonyms, text) {
   if (!text || text.length === 0) return [];
   if (!synonyms || synonyms.length === 0) return [text];

   const currParents = {};
   
   for (let synPair of synonyms) {
      for (let word of synPair) {
         if (!currParents.hasOwnProperty(word)) {
            currParents[word] = { parent: word, groupSize: 1 };
         }
      }
   }

   unify(synonyms, currParents);
   let result = generatePermutations(currParents, text);
   return result;
};

var unify = (synonyms, currParents) => {
   for (let synPair of synonyms) {
      let v1 = currParents[synPair[0]];
      let v2 = currParents[synPair[1]];
      let v1GroupSize = currParents[v1.parent].groupSize;
      let v2GroupSize = currParents[v2.parent].groupSize;
      let sharedParent = v1GroupSize >= v2GroupSize ? v1.parent : v2.parent;
      v1.parent = sharedParent;
      v2.parent = sharedParent;

      currParents[sharedParent].groupSize = currParents[sharedParent].groupSize + 1;
   }
}

var generatePermutations = (currParents, text) => {
   let parentDirectory = {};
   let groups = [];
   let maxGroupNdx = 0;
   for (word in currParents) {
      let parent = currParents[word].parent;
      while (currParents[parent].parent !== parent) {
         parent = currParents[parent].parent;
      }
      let groupNdx = maxGroupNdx;
      if (!parentDirectory.hasOwnProperty(parent)) {
         parentDirectory[parent] = groupNdx;
         groups.push([])
         maxGroupNdx++;
      }
      else {
         groupNdx = parentDirectory[parent];
      }
      groups[groupNdx].push(word);
   }

   for (group of groups) {
      group.sort();
   }

   const permutations = []
   const textWords = text.split(" ");

   function recurse(str, textNdx, groupCursor, p) {
      if (textNdx === textWords.length) {
         p.push(str.slice(0, str.length - 1));
         return;
      };

      let localStr = str;
      let currWord = textWords[textNdx];

      // word is in synonyms list
      if (currParents[currWord]) {
         let groupNdx = parentDirectory[currParents[currWord].parent];
         // build str for each word in group
         if (groupCursor < 0) {
            let groupCursor = 0;
            while (groupCursor < groups[groupNdx].length) {
               let cString = localStr + groups[groupNdx][groupCursor] + " ";
               recurse(cString, textNdx + 1, -1, p);
               groupCursor++;
            }
         }
      } else {
         localStr += currWord + " ";
         recurse(localStr, textNdx + 1, -1, p);
      }
   }

   recurse("", 0, -1, permutations);
   return permutations;
}

// runner
// const synsen = require('./synonymous-sentences');
// const synonyms = [["a","b"],["b","c"],["d","e"],["c","d"]];
// const text = 'a b'

// var result = synsen.generateSentences(synonyms, text);
// console.log(result);