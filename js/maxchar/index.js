// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
// maxChar("abcccccccd") === "c"
// maxChar("apple 1231111") === "1"

// function maxChar(str) {
//   var counter = {}
//   for (var i=0; i < str.length; i++){
//     (str[i] in counter ?   counter[str[i]] ++ : counter[str[i]] = 1)
//   }
//   console.log(Object.values(counter))
// }

function maxChar(str) {
  var counter = {}
  for (let i of str){ //create object with each char count in str
    (i in counter ? counter[i] ++ : counter[i] = 1)
  }
  let max = 0
  let maxChar = ''
  for (let i in counter){ //i are the object keys
    if (counter[i] > max) {
      max = counter[i]
      maxChar= i
    }
  }
  return maxChar
}


module.exports = maxChar;
