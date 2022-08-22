exports.convert = function(s, numRows) {
   let board = [[]];
   let y = 0;
   let x = 0;
   let i = 0;

   let goingDown = true;

   while (i < s.length) {
      if (y === 0) {
         goingDown = true;
      }

      board[x][y] = s[i];
      
      if (!goingDown) {
         y += -1;
         x += 1;
         board.push([]);
      }
      else {
         y += 1;
      }

      if (y === numRows) {
         x++;
         y--;
         goingDown = false;
         board.push([]);
      }

      i++;
   }

   i = 0;
   x = 0;
   y = 0;
   res = '';
   while (i < s.length && board[x] && board[x][y]) {
      res += board[x][y];
      x += numRows - 1;
      if (!board[x]) {
         y++;
         x = 0;
      }
   }

   return res;
}