// --- Directions
// Write a function that returns the number of vowels
// used in a string.  Vowels are the characters 'a', 'e'
// 'i', 'o', and 'u'.
// --- Examples
//   vowels('Hi There!') --> 3
//   vowels('Why do you ask?') --> 4
//   vowels('Why?') --> 0

// function vowels(str) {
//   const strL = str.toLowerCase()
//   const obj = {}
//   var count= 0
//   for (var i of strL) {
//     (i in obj ? obj[i] ++ : obj[i] = 1)
//   }
//   for (var i in obj) {
//     if (i == "a" || i =='e' || i=='i'|| i=='o' || i=='u') {
//       count  += obj[i]
//     }
//   }
//    return count
// }







// function vowels(str) {
//   let count = 0;
// or can use .includes on an array ['a', 'e', 'i', 'o', 'u']
//   const vowel = "aeiou";
//   for (var i of str.toLowerCase()) {
//       if (vowel.includes(i)) {
//         count  ++
//     }
//   }
//   return count
//   }


function vowels(str) {
  //will either be an array or null
  const vowel = str.match(/[aeiou]/gi);
  return vowel ? vowel.length : 0

}

vowels("aeiouiiiiiiiiiii")







module.exports = vowels;
