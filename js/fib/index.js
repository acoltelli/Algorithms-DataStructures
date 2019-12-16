// --- Directions
// Print out the n-th entry in the fibonacci series.
// The fibonacci series is an ordering of numbers where
// each number is the sum of the preceeding two.
// For example, the sequence
//  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
// forms the first ten entries of the fibonacci series.
// Example:
//   fib(4) === 3


// //recursive. exponential runtime.
function recurseFib(n) {
  if ( n == 0 || n == 1) {
    return n;
  } else {
    return fib(n-2) + fib(n-1);
  }
}


//iternative. linear runtime.
// function fib(n) {
//   let sol = [0, 1]
//   for (let i=2 ; i<=n; i++){
//     sol.push(sol[i-1] + sol[i-2]);
//   }
//   return sol[n];
// }



//memoization
//imporves runtime of RECURSIVE sol
function memoize(fn){
  const cache = {};
  //pass array of argments since not sure how many parameters
  //the original function takes
  return function(...args) {
    if (cache[args]) {
      return cache[args];
    }
    //use .apply() method if you want to use an array
    //instead of an argument list
    const result = fn().apply(this, args);
    cache[args] = result;

    return result;
  };
}

const fib = memoize(recurseFib);

fib(4)

var fibonacci = (function () {
  var memo = [0, 1];
  var fib = function (n) {
      var result = memo[n];
      if (typeof result !== 'number') {
        result = fib(n - 1) + fib(n - 2);
        memo[n] = result;
      }
      return result;
      };
  return fib;
}());


module.exports = fib;
