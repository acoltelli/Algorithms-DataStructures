// --- Directions
// Check to see if two provided strings are anagrams of eachother.
// One string is an anagram of another if it uses the same characters
// in the same quantity. Only consider characters, not spaces
// or punctuation.  Consider capital letters to be the same as lower case
// --- Examples
//   anagrams('rail safety', 'fairy tales') --> True
//   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
//   anagrams('Hi there', 'Bye there') --> False

// function buildObject(str) {
//   const counter = {};
//   for (let i of str){
//     (i in counter ? counter[i]++:counter[i]=1)
//   }
//   return counter;
// }
//
//
// function anagrams(stringA, stringB) {
//   a = stringA.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g,"").toLowerCase()
//   b = stringB.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g,"").toLowerCase()
//   if (a.length !== b.length) {
//     return false;
//   }
//   a= buildObject(a)
//   b= buildObject(b)
//
//   // if (Object.keys(a).length !== Object.keys(b).length) {
//   //   return false;
//   // }
//
//   for (let i in a){
//     if (a[i] !== b[i]) {
//       return false
//     }
//     return true
//   }
// }

function helper(str){
  return str.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g,"").toLowerCase().split("").sort().join();
}

function anagrams(stringA, stringB) {
  if (helper(stringA) !== helper(stringB)){
    return false;
  }
    return true;
}









anagrams('rail safety', 'fairy tales')
// anagrams('One One', 'Two two two')
// anagrams('A tree, a life, a bench', 'A tree, a fence, a yard')





module.exports = anagrams;
