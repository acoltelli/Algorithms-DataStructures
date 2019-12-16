// --- Directions
// Given a linked list, return the element n spaces
// from the last node in the list.  Do not call the 'size'
// method of the linked list.  Assume that n will always
// be less than the length of the list.
// --- Examples
//    const list = new List();
//    list.insertLast('a');
//    list.insertLast('b');
//    list.insertLast('c');
//    list.insertLast('d');
//    fromLast(list, 2).data // 'b'

function fromLast(list, n) {
  let start = list.head;
  let end = list.head;
  //create gap between the two pointers that is equal to n
  while (n > 0) {
    start = start.next;
    n--;
  }
  // when start pointer reaches the end of the list, end pointer will be n nodes behind
  while (start.next) {
    start = start.next;
    end = end.next;
  }
  return end
}

module.exports = fromLast;
