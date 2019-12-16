// --- Directions
// Implement classes Node and Linked Lists
// See 'directions' document

class Node {
  constructor (data, next = null) {
    this.data = data;
    this.next = next;
  }
}


class LinkedList {
  constructor() {
    this.head = null;
  }

  insertFirst(data) {
    // creat new node, assign it to list head.
    const node = new Node(data, this.head);
    this.head = node;
  }

  size(){
    let count = 0;
    let curr = this.head;
    while (curr != null) {
      count++;
      curr = curr.next;
    }
    return count;
  }

  getFirst() {
    return this.head;
  }

  getLast() {
    if (!this.head) {
      return null;
    }

    let curr = this.head;
    while (curr) {
      if (!curr.next) {
        return curr;
      }
      curr = curr.next;
    }
  }

  clear() {
    this.head = null;
  }

  removeFirst() {
    if (!this.head) {
      return;
    }
    this.head = this.head.next;
  }

  // removeLast() {
  //   if (!this.head || !this.head.next){
  //     this.head = null;
  //     return
  //   }
  //   let curr = this.head;
  //   while (curr) {
  //     if (!curr.next.next) {
  //       curr.next=null;
  //       return
  //     }
  //     curr = curr.next;
  //   }
  // }

  removeLast() {
    //case of length 0
    if (!this.head){
      return;
    }
    //case of length 1
    if (!this.head.next) {
      this.head = null;
      return;
    }

    let prev = this.head;
    let curr = this.head.next;
    while (curr.next) {
        prev = curr;
        curr = curr.next;
      }
      prev.next = null;
    }

    // insertLast(data) {
    //   const last = this.getLast();
    //   last.next = new Node(data);
    // }

    insertLast(data) {
      const last = this.getLast();
      if (last) {
        last.next = new Node(data);
      }
      else {
        this.head = new Node(data);
      }
    }

    getAt(int) {
      let count = 0;
      let current = this.head;
      while (current) {
        if (count === int) {
          return current;
        }
        count++;
        current = current.next;
      }
      //case where current is null, but count has never equalled int.
      //this would occur when int is larger than the length of the linked list.
      return null;
    }

    removeAt(int) {
      if (!this.head){
        return;
      }

      if (int === 0) {
        this.head = this.head.next;
        return;
      }

      const prev = this.getAt(int-1);
      // .getAt() returns null if int is out of bounds
      if (!prev || !prev.next) {
        return;
      }
      prev.next = prev.next.next;
    }

    insertAt(data, int) {
      if (!this.head) {
        this.head = new Node(data);
        return;
      }

      if (int === 0) {
        this.head = new Node(data, this.head);
        return;
      }

      let previous = this.getAt(int-1) || this.getLast();
      previous.next = new Node(data, previous.next);
    }


    /////////

// list.forEach(node => {node.data += 10;});
    forEach(fn) {
      if (!this.head) {
        return null;
      }

      let node = this.head;
      while (node) {
        fn(node);
        node = node.next;
      }
    }

// for (let node of list) { node.data += 10;}
    *[Symbol.iterator]() {
      let node = this.head;
      while (node) {
        yield node;
        node = node.next;
      }
    }


}




const list = new LinkedList();
list.insertFirst('a');
list.insertFirst('b');
list.insertFirst('c');

console.log(list)
console.log(" ")

list.insertAt('z', 1)
console.log(list)











module.exports = { Node, LinkedList };
