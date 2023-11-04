const solution = (angles) => {
  let finalString = "";
  let numToClose = 0;
  let tempAngles = angles;

  // angles: "<>>>>"
  // 1st iteration: finalString = "<", i = 1
  // 2nd: finalString = "<<", i = 2
  // 3rd: finalString = "<<<", i = 3
  // 4th: finalString = "<<<<", i = 4
  for (let i = 0; i < tempAngles.length; i++) {
    let j = i + 1;

    // while 0 = 1, 0 = 2
    while (tempAngles[i] == tempAngles[j]) {
      if (tempAngles[i] === "<") {
        finalString = finalString.concat(tempAngles[i]);
        console.log("concat here", finalString);
        i += 1;
        numToClose += 1;
      } else {
        console.log("there");
        // angles[i] == '>'
        finalString = finalString.concat("<");
        console.log("final string", finalString);
      }
      j += 1;
      //   console.log("finalString", finalString);
    }

    finalString = finalString.concat(tempAngles[i]);
    console.log("concat here 2", finalString);

    if (tempAngles[i] === ">") {
      numToClose -= 1;
    }

    while (numToClose > 0) {
      finalString = finalString.concat(">");
      console.log("concat here 3", finalString);
      numToClose -= 1;
    }
  }

  if (finalString[0] === ">") {
    finalString = "<".concat(finalString);
    console.log("concat here 4", finalString);
  }

  if (finalString[finalString.length - 1] === "<") {
    finalString = finalString.concat(">", finalString);
  }

  return finalString;
};

console.log(solution("<>>"));
// console.log(solution("<<>"));
// console.log(solution("<>><"));
// console.log(solution("><>"));
// console.log(solution("<<<>>"));

// console.log(solution("<<<"));
// console.log(solution(">>>")); // expected: <<<
// console.log(solution("<>>>>")); // expected: <<<<>>>>
// console.log(solution("><<>>><")); // expected: <<><<>>><>
