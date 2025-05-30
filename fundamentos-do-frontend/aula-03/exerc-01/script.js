let weather = prompt("Insira clima atual (Ensolarado, Chuvoso, Nublado)");

switch (weather.toLowerCase().trim()) {
    case "ensolarado":
        alert("Dia de luz, festa de sol");
        break;
    case "chuvoso":
        alert("Olha, está chovendo na roseira");
        break;
    case "nublado":
        alert("Chove chuva, chove sem parar");
        break;
}
