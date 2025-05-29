/* Exercício 1 */
/* Dia de luz, festa de sol */
/* Olha está chovendo na roseira */
/* Fica comigo esta noite, E não te arrependerás, Lá fora o frio é um açoite */
let clima = prompt("Qual o clima de hoje? (Ensolarado, Chuvoso, Nublado");

if (clima != null) {
    clima = clima.toLowerCase().trim();
    if (clima == "ensolarado") {
        document.getElementById("clima").innerHTML = "Ensolarado";
        document.getElementById("mensagem").innerHTML = "Dia de luz, festa de sol.";
    }
    else if (clima == "chuvoso") {
        document.getElementById("clima").innerHTML = "Chuvoso";
        document.getElementById("mensagem").innerHTML = "Olha está chovendo na roseira.";
    }
    else if (clima == "nublado") {
        document.getElementById("clima").innerHTML = "Nublado";
        document.getElementById("mensagem").innerHTML = "Fica comigo esta noite. E não te arrependerás. Lá fora o frio é um açoite";
    } else {
        document.getElementById("clima").innerHTML = clima;
        document.getElementById("mensagem").innerHTML = "Clima não reconhecido.";
    }
}