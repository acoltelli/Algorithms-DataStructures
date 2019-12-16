// --- Directions
// Given a string, return a new string with the reversed
// order of characters
// --- Examples
//   reverse('apple') === 'leppa'
//   reverse('hello') === 'olleh'
//   reverse('Greetings!') === '!sgniteerG'

function reverse(str) {
  // debugger;
  newStr = str.split(''); // or newStr = [...str];
  newStr.reverse()
  newStr = newStr.join('')
  return newStr //or just return: str.split('').reverse().join()
}

// function reverse(str) {
//   let reverse = ''
//   for (let i of str){
//     // iteratiely add characters to new str from first to last i in str
//     reverse = i + reverse;
//   }
//   return reverse
// }

module.exports = reverse;
