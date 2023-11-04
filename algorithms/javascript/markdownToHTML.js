const h1 = (content) => `<h1>${content.substring(2)}</h1>`;

const h2 = (content) => `<h2>${content.substring(3)}</h2>`;

const paragraph = (content) => `<p>${content.replace("\n", "<br>")}</p>`;

const strong = (content) => {
  const lastIndexOfStrong = content.lastIndexOf("**");
  return `<strong>${content.substring(2, lastIndexOfStrong)}</strong>`;
};

const list = (content) => {
  const lines = content.split("\n");
  const lineItems = lines.reduce((acc, line) => {
    return `${acc}\n<li>${line.trim().substring(2)}</li>`;
  }, "");

  return `<ul>${lineItems}\n</ul>`;
};

const MARKDOWN_TO_HTML_MAP = {
  "##": h2,
  "#": h1,
  "**": strong,
  "- ": list,
};

const convertToHTML = (input) => {
  for (let [k, v] of Object.entries(MARKDOWN_TO_HTML_MAP)) {
    if (input.startsWith(k)) {
      return v(input);
    }
  }

  return paragraph(input);
};

console.log(convertToHTML("# this is heading 1"));
console.log(convertToHTML("## this is heading 2"));
console.log(convertToHTML("**this is bold text**"));
console.log(convertToHTML("This is a paragraph"));
console.log(
  convertToHTML(`- First item
  - Second item
  - Third item
  - Fourth item`)
);
console.log(
  convertToHTML(`This is a paragraph
  This is the second line.`)
);
