/**
 * @param {number[][]} trips
 * @param {number} capacity
 * @return {boolean}
 */

exports.carPooling = function (trips, capacity) {
   trips.sort((a, b) => a[1] - b[1]);
   console.log(trips);
   let capLeft = capacity;
   let pos = trips[0][1];
   let dropMap = new Map();
   let i = 0;
   while (i < trips.length) {
      let [passengers, start, end] = trips[i];
      while (pos <= start) {
         if (dropMap.has(pos)) {
            capLeft += dropMap.get(pos);
            console.log(`dropping off ${dropMap.get(pos)} at point ${pos}, cap left: ${capLeft}`)
         }
         pos++;
      }

      while (i < trips.length && trips[i][1] === start) {
         passengers = trips[i][0];
         end = trips[i][2];
         capLeft -= passengers;
         console.log(`picking up ${passengers} at point ${start}, cap left: ${capLeft}`)
         if (capLeft < 0) {
            return false;
         }
         if (dropMap.has(end)) {
            passengers += dropMap.get(end);
         }
         dropMap.set(end, passengers);
         
         i++;
      }
   }

   return true;
};