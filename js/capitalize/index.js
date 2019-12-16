// --- Directions
// Write a function that accepts a string.  The function should
// capitalize the first letter of each word in the string then
// return the capitalized string.
// --- Examples
//   capitalize('a short sentence') --> 'A Short Sentence'
//   capitalize('a lazy fox') --> 'A Lazy Fox'
//   capitalize('look, it is working!') --> 'Look, It Is Working!'

// function capitalize(str) {
//   var sen = '';
//   for (let i of str.split(' ')) {
//     sen += i[0].toUpperCase() + i.slice(1) + ' '
//   }
//   return sen.slice(0, sen.length - 1)
// }

// function capitalize(str) {
//   var sen = '';
//   var test = str
//   test = test[0].toUpperCase() + test.slice(1, str.length + 1)
//   for (let i = 0 ; i < str.length; i++) {
//     if (test[i] == " ") {
//       test = test.slice(0,i+1) + test[i+1].toUpperCase() + test.slice(i+2, str.length + 1)
//     }
//   }
//   return test
// }

function capitalize(str) {
  var sen = '';
  sen += str[0].toUpperCase()
  for (let i = 1 ; i < str.length; i++) {
    if (str[i-1] == " ") {
      sen += str[i].toUpperCase()
      continue
    }
    sen += str[i]
  }
  return sen
}

capitalize('a short sentence')




module.exports = capitalize;
