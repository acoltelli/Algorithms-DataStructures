
//type coercion
// ==

//object with all elements in str and their count
let str = 'teststring'
  const obj = {}
  for (var i of str) {
    i in obj ? obj[i] ++ : obj[i] = 1
  }

//The entries() method returns a new Array Iterator object that contains the key/value pairs for each index in the array.
const array1 = ['a', 'b', 'c'];
const iterator1 = array1.entries();
for (var i of iterator1) {
  // console.log(i)
}


// fill with 0 from position 2 until position 4
array1.fill(0, 2, 4);
// expected output: [1, 2, 0, 0]


//.every() when you want derive a single boolean value from multiple elements in an array.
var sampleArray = [ 1, 2, 3, 4, 5 ];
var sampleArray2 = [ 0, -1, -30, 5];
function tester(number){
  return number > 0;
}
sampleArray.every(tester); // returns true
sampleArray2.every(tester); // returns false
sampleArray.every( number => number > 0 ); // returns true. ES6

// .apply()
// takes array, apply method to each array entry
var person = {
  fullName: function(city, country) {
    return this.firstName + " " + this.lastName + "," + city + "," + country;
  }
}
var person1 = {
  firstName:"John",
  lastName: "Doe"
}
person.fullName.apply(person1, ["Oslo", "Norway"]);

//.reduce()
var numbers = [0, 1, 1, 2];
function getSum(total, num) {
  return total + num;
}
console.log(numbers.reduce(getSum, 0))
