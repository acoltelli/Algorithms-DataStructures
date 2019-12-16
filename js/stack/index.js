// --- Directions
// Create a stack data structure.  The stack
// should be a class with methods 'push', 'pop', and
// 'peek'.  Adding an element to the stack should
// store it until it is removed.
// --- Examples
//   const s = new Stack();
//   s.push(1);
//   s.push(2);
//   s.pop(); // returns 2
//   s.pop(); // returns 1


//FILO. first in, last out.
//Add to top(first elm) of stack, remove from top(first elm) of stack.

class Stack {
  constructor(){
    this.data = [];
  }

  push(elm){
    //unshift adds elements to beginning of array
    this.data.unshift(elm);
  }

  pop(elm){
    //shift returns and deletes first element in array
    return this.data.shift(elm);
  }

  peek(elm){
    //rreturns first elm in stack but doesnt remove it
    return this.data[0];
  }
}

module.exports = Stack;
