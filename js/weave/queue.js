// --- Directions
// Implement a 'peek' method in this Queue class.
// Peek should return the last element (the next
// one to be returned) from the queue *without*
// removing it.

class Queue {
  constructor() {
    this.data = [];
  }

  //adds elm to beginning of queue
  add(record) {
    this.data.unshift(record);
  }

 //removes elm from end of queue
  remove() {
    return this.data.pop(); //pop returns and removes last elm
  }

 //returns last elm in queue
  peek() {
    return this.data[this.data.length-1];
  }
}

let q = new Queue;
q.add(1)
q.add(2)
console.log(q.peek())
console.log(q.data)

module.exports = Queue;
