let age = prompt("Insira sua idade: ");
let day = prompt("É quarta-feira (S/N): ");

const child = 10;
const adult = 20;
const senior = 12;

if (age != null && day != null) {
    if (day.toLowerCase().trim() === "s") {
        if (age < 12) {
            document.getElementById("ticket").innerHTML = "Você é criança. O valor do ingresso é R$" + child / 2 + ".";
        } else if (age >= 12 && age < 60) {
            document.getElementById("ticket").innerHTML = "Você é adulto. O valor do ingresso é R$" + adult / 2 + ".";
        } else {
            document.getElementById("ticket").innerHTML = "Você é idoso. O valor do ingresso é R$" + senior / 2 + ".";
        }
    }
    else if (day.toLowerCase().trim() === "n") {
        if (age < 12) {
            document.getElementById("ticket").innerHTML = "Você é criança. O valor do ingresso é R$" + child + ".";
        } else if (age >= 12 && age < 60) {
            document.getElementById("ticket").innerHTML = "Você é adulto. O valor do ingresso é R$" + adult + ".";
        } else {
            document.getElementById("ticket").innerHTML = "Você é idoso. O valor do ingresso é R$" + senior + ".";
        }
    }
}