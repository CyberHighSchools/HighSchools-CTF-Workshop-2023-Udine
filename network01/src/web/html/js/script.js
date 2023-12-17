var messaggio = "=03ZulmclVmbpdmbl9VZzJXZ2Vmcf9GdhRnblZXak9VZf9GdzVWdxt3ZhxmZ";

function decodifica(msg) {
  msg = msg.split("").reverse().join("");
  msg = atob(msg);
  console.log(msg);
}

decodifica(messaggio);
