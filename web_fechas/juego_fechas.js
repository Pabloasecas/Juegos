const preguntas = require('./juego_fechas/preguntas_fechas');
const readline = require('readline');

function jugar() {
  const pregunta = preguntas[Math.floor(Math.random() * preguntas.length)];
  const respuesta_correcta = pregunta.respuesta;

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  rl.question(pregunta.pregunta + "\n", respuesta_usuario => {
    if (respuesta_correcta === respuesta_usuario) {
      console.log("¡Has acertado!");
    } else {
      console.log("Has fallado, es " + respuesta_correcta);
    }
    
    rl.close();
    continuar();
  });
}

function continuar() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  rl.question("¿Quieres seguir jugando? (s/n) ", continuacion => {
    continuacion = continuacion.toLowerCase();

    while (continuacion !== "s" && continuacion !== "n") {
      console.log("Entrada no válida. Introduce 's' o 'n'.");
      continuar();
    }

    if (continuacion === "s") {
      rl.close();
      jugar();
    } else {
      console.log("¡Hasta luego!");
      rl.close();
      process.exit();
    }
  });
}

console.log("Hola, ¡vamos a aprender fechas!");
jugar();
