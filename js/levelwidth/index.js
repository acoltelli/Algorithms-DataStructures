

// --- Directions
// Given the root node of a tree, return
// an array where each element is the width
// of the tree at each level.
// --- Example
// Given:
//     0
//   / |  \
// 1   2   3
// |       |
// 4       5
// Answer: [1, 3, 2]

class Node {
  constructor(data) {
    this.data = data;
    this.children = [];
  }

  add(data) {
    this.children.push(new Node(data));
  }
};

function levelWidth(root) {
  const count = [0];
  // 's' is a placeholder to mark the end of a 'row'
  const array = [root, 's'];
  // implement similar to breadth first search w placeholder
  while ( array.length > 1) {
    const node = array.shift();
    if ( node === 's') {
      array.push('s');
      count.push(0);
    } else {
      array.push(...node.children);
      count[count.length - 1]++;
    }
  }
  return count;
}



const root = new Node(0);
root.add(1);
root.add(2);
root.add(3);
root.children[0].add(4);
root.children[2].add(5);
console.log(root)
console.log(levelWidth(root))












module.exports = levelWidth;
