
//type coercion


//The entries() method returns a new Array Iterator object that contains the key/value pairs for each index in the array.
const array1 = ['a', 'b', 'c'];
const iterator1 = array1.entries();
for(var i of iterator1){
  console.log(i)
}




//.every() when you want derive a single boolean value from multiple elements in an array.
var sampleArray = [ 1, 2, 3, 4, 5 ];
var sampleArray2 = [ 0, -1, -30, 5];
function tester(number){
  return number > 0;
}
sampleArray.every(tester); // returns true
sampleArray2.every(tester); // returns false
sampleArray.every( number => number > 0 ); // returns true. ES6
