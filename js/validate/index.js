// --- Directions
// Given a node, validate the binary search tree,
// ensuring that every node's left hand child is
// less than the parent node's value, and that
// every node's right hand child is greater than
// the parent

function validate(node, min = null, max = null) {
  // first two if statements set validate() call to false
  //for use of last two if statements, two recusive calls
  if (max !== null && node.data > max) {
    return false;
  }
  if (min !== null && node.data < min) {
    return false;
  }

  // left/right children must exist and validate must be false
  //to return false
  if (node.left && !validate(node.left, min, node.data)){
    return false;
  }
  if (node.right && !validate(node.right, node.data, max)){
    return false;
  }
   return true;
}

module.exports = validate;
