// --- Directions
// Implement a Queue datastructure using two stacks.
// *Do not* create an array inside of the 'Queue' class.
// Queue should implement the methods 'add', 'remove', and 'peek'.
// For a reminder on what each method does, look back
// at the Queue exercise.
// --- Examples
//     const q = new Queue();
//     q.add(1);
//     q.add(2);
//     q.peek();  // returns 1
//     q.remove(); // returns 1
//     q.remove(); // returns 2

const Stack = require('./stack'); //write reverse function for stack

class Queue {
  constructor(){
    this.stack1 = new Stack();
    this.stack2 = new Stack();
  }

  add(elm){

  }

  remove(elm){

  }

  peek(elm){

  }

}

module.exports = Queue;
