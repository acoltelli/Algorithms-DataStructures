// --- Description
// Create a queue data structure.  The queue
// should be a class with methods 'add' and 'remove'.
// Adding to the queue should store an element until
// it is removed
// --- Examples
//     const q = new Queue();
//     q.add(1);
//     q.remove(); // returns 1;


// FIFO. One end inserts data, other end removes data.


class Queue {
  constructor(){
    this.data = [];
  }

  //adds elm to beginning of queue
  add(elm) {
    //unshift adds one or more elements to the beginning of an array
    //and returns the new length of the new array
    this.data.unshift(elm);
  }

  //removes elm from end of queue
  remove(elm) {
    return this.data.pop(elm);
  }
}

module.exports = Queue;
