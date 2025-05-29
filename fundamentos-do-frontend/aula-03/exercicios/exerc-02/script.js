document.getElementById("portal").innerHTML = "Fora do portal";

let portal = prompt("Escolha um portal para entrar: (1, 2, 3):");

switch (portal) {
    case "":
        document.getElementById("portal").innerHTML = "Fim!";
        break;

    case "1":
        document.getElementById("portal").innerHTML = "Você entrou no portal 1!";
        break;
    case "2":
        document.getElementById("portal").innerHTML = "Você entrou no portal 2!";
        break;
    case "3":
        document.getElementById("portal").innerHTML = "Você entrou no portal 3!";
        break;

    default:
        document.getElementById("portal").innerHTML = "Portal inválido";
        break;
}