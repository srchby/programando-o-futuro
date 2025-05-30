let age = prompt("Insira sua idade: ");
let day = prompt("É quarta-feira (S/N)?");

const child = 10;
const adult = 20;
const senior = 12;

switch (day.toLowerCase().trim()) {
  case "s":
    if (parseInt(age) <= 12) {
      alert("O ingresso custará " + child / 2);
    } else if (parseInt(age) <= 59) {
      alert("O ingresso custará " + adult / 2);
    } else if (parseInt(age) >= 60) {
      alert("O ingresso custará " + senior / 2);
    } else {
      alert("Idade inválida");
    }
  case "n":
    if (parseInt(age) <= 12) {
      alert("O ingresso custará " + child);
    } else if (parseInt(age) <= 59) {
      alert("O ingresso custará " + adult);
    } else if (parseInt(age) >= 60) {
      alert("O ingresso custará " + senior);
    } else {
      alert("Idade inválida");
    }
  default:
    alert("Resposta inválida");
    break;
}
