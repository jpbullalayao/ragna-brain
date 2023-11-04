const solution = (angles) => {
  let finalString = "";
  let tempAngles = angles;

  let stack = [];

  // if (angles === "<>") {
  //   return "<>";
  // }

  // Example: ><
  for (let i = 0; i < tempAngles.length; i++) {
    if (tempAngles[i] === "<") {
      finalString = finalString.concat("<");
      stack.push(">");
    } else {
      let j = i;

      while (tempAngles[j] === ">") {
        finalString = finalString.concat("<");
        stack.push(">");

        j += 1;
      }

      while (stack.length > 0) {
        finalString = finalString.concat(stack.pop());
      }
    }
  }

  while (stack.length > 0) {
    finalString = finalString.concat(stack.pop());
  }

  return finalString;
};

// console.log(solution("<>>"));
// console.log(solution("<<>"));
// console.log(solution("<>><"));
// console.log(solution("><>"));
// console.log(solution("<<<>>"));

// console.log(solution("<")); // passing
// console.log(solution(">")); // passing
// console.log(solution("<<")); // passing
// console.log(solution("<<<")); // passing
// console.log(solution(">>>")); // passing

console.log(solution("><"));
console.log(solution("<>"));
console.log(solution("<>>"));

// console.log(solution("<>>>>")); // expected: <<<<>>>>
// console.log(solution("><<>>><")); // expected: <<><<>>><>
