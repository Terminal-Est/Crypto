function addTwo(int1, int2) {
  return int1 + int2;
}

function outputText() {
  let text = document.getElementById("txta1").value;
  let len = text.length;
  let codeOut = text.charAt(1);
  document.getElementById("p3").innerHTML = codeOut;
}
