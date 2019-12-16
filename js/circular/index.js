// --- Directions
// Given a linked list, return true if the list
// is circular, false if it is not.
// --- Examples
//   const l = new List();
//   const a = new Node('a');
//   const b = new Node('b');
//   const c = new Node('c');
//   l.head = a;
//   a.next = b;
//   b.next = c;
//   c.next = b;
//   circular(l) // true

function circular(list) {
  let slow = list.head;
  let fast = list.head;

  while (fast.next && fast.next.next) {
    //move slow forward by one, move fast forward by two
    slow = slow.next;
    fast = fast.next.next;
    // if slow equals fast then the list is a circular linked list
    if ( slow === fast ){
      return true;
    }
  }
  return false;
}



module.exports = circular;
