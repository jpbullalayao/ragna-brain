const solution = (angles) => {
  let finalString = "";
  let tempAngles = angles;

  let stack = [];

  // Example: ><
  for (let i = 0; i < tempAngles.length; i++) {
    let j = i;
    let counter = 0;

    if (tempAngles[j] === "<") {
      while (tempAngles[j] === "<") {
        stack.unshift("<");
        j += 1;
        counter += 1;
      }

      while (counter > 0) {
        stack.unshift(">");
        counter -= 1;
      }
    } else {
      while (tempAngles[j] === ">") {
        stack.unshift("<");
        j += 1;
        counter += 1;
      }

      while (counter > 0) {
        stack.unshift(">");
        counter -= 1;
      }
    }

    if (j === tempAngles.length) {
      break;
    }
  }

  let item;
  while ((item = stack.pop())) {
    finalString = finalString.concat(item);
  }

  return finalString;
};

console.log(solution("<>>"));
// console.log(solution("<<>"));
// console.log(solution("<>><"));
// console.log(solution("><>"));
// console.log(solution("<<<>>"));

// console.log(solution("<")); // passing
// console.log(solution(">")); // passing
// console.log(solution("<<")); // passing
// console.log(solution("<<<")); // passing
// console.log(solution(">>"));
// console.log(solution(">>>")); // passing
// console.log(solution("<<<>")); // passing

console.log(solution("><"));
// console.log(solution("<>"));
// console.log(solution("<>>"));

// console.log(solution("<>>>>")); // expected: <<<<>>>>
// console.log(solution("><<>>><")); // expected: <<><<>>><>
