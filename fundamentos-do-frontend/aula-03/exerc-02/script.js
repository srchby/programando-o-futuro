let portal = prompt("Escolha um portal (1, 2, 3)");

switch (portal.toLowerCase().trim()) {
  case "1":
    alert("Você entrou no universo de Admirável Mundo Novo");
    break;
  case "2":
    alert("Você entrou no universo de Fahrenheit 451");
    break;
  case "3":
    alert("Você entrou no universo de 1984");
    break;

  default:
    alert("Portal inválido");
    break;
}
