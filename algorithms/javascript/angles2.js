const solution = (angles) => {
  let finalString = "";
  let tempAngles = angles;

  let stack = [];

  // Example: ><
  for (let i = 0; i < tempAngles.length; i++) {
    // console.log("i", i);

    if (tempAngles[i] === "<") {
      // console.log(1);
      finalString = finalString.concat("<");
      stack.push(">");
    } else {
      // console.log(2);

      let j = i;

      while (tempAngles[j] === ">" && j !== tempAngles.length - 1) {
        // console.log("here");
        finalString = finalString.concat("<");
        stack.push(">");

        j += 1;
        // console.log("j now", j);
      }

      // if (j === tempAngles.length - 1) {
      //   break;
      // }

      // if (finalString[finalString.length - 1] === ">") {
      //   break;
      // }
    }

    // stack.push(">");

    // if (angles[i] !== angles[j]) {
    //   finalString = finalString.concat(stack.pop());
    // }
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

console.log(solution("<")); // passing
console.log(solution(">")); // passing
console.log(solution("<<"));
console.log(solution("<<<")); // passing
console.log(solution(">>>")); // passing

// console.log(solution("><"));
console.log(solution("<>")); // passing
console.log(solution("<>>")); // passing

// console.log(solution("<>>>>")); // expected: <<<<>>>>
// console.log(solution("><<>>><")); // expected: <<><<>>><>
