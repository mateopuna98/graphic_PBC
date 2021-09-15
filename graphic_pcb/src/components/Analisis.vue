<template>
  <div class="analisis">
    <img
      src="https://kbaile03.github.io/projects/fibo_dijk/images/graph_icon.png"
      alt="graph icon"
    />
    <h1 id="titulo">
      Colas prioritarias con Fibonacci Heap y FIFO - Una visualización
    </h1>
    <h2 class="nombre">Mateo Puña</h2>
    <h2 class="nombre">Javier Soruco</h2>
    <h2 class="Introduccion">Introducción</h2>
    <p class="parrafo">{{ introduccion }}</p>
    <p class="parrafo">{{ introduccion2 }}</p>

    <h2 class="Introduccion">Qué es un PCB?</h2>
    <p class="parrafo">{{ pcb }}</p>

    <h2 class="Introduccion">Descripción del gráfico</h2>
    <p class="parrafo">{{ grafico }}</p>
    <p class="parrafo">{{ grafico2 }}</p>

    <ul id="listapartes" class="parrafo">
      <li class="elemLista">Representación PCB</li>
      <li class="elemLista">Visualización de la cola</li>
      <li class="elemLista">Estadísticas</li>
    </ul>
    <h3>Representación PCB</h3>
    <p class="parrafo">{{ grafico2 }}</p>
    <h3>Visualización de la cola</h3>
    <p class="parrafo">{{ grafico3 }}</p>
    <h3>Estadísticas</h3>
    <p class="parrafo">{{ grafico4 }}</p>

    <h2 class="Introduccion">Explicación de estadísticas</h2>
    <h3>Procesos terminados</h3>

    <p class="parrafo">{{ estadisticas1 }}</p>
    <h3>Tamaño actual cola</h3>

    <p class="parrafo">{{ estadisticas2 }}</p>
    <h3>Prioridad promedio</h3>

    <p class="parrafo">{{ estadisticas3 }}</p>
    <h3>Tamaño de cola promedio</h3>

    <p class="parrafo">{{ estadisticas4 }}</p>
    <h3>Tiempo de espera promedio</h3>

    <p class="parrafo">{{ estadisticas5 }}</p>
        <h3>Valor ponderado de pérdida</h3>

    <p class="parrafo">{{ estadisticas6 }}</p>
        <h2  id="visualize" class="Introduccion">Visualización</h2>

  </div>
</template>

<script>
export default {
  name: "Analisis",
  data() {
    return {
      introduccion:
        "Para un sistema operativo, el metodo de gestionamiento de procesos es de suprema importancia, dado que de ser mal  gestionado puede llevar a problemas como retrasos extendidos y el excesivo uso de memoria. " +
        "Esto se realiza mediante un sistema de colas prioritarias, que son estructuras de datos en las cuales los elementos con mayor prioridad son insertados en los primeros lugares, y por lo tanto son los primeros en ser ejecutados. ",
      introduccion2:
        "La estructura más básica de colas es llamada cola FIFO (First In First Out), en la cual los procesos se colocan por orden de llegada, es decir el primero que llegue en la cola ser[a el primero en salir. " +
        "En este proyecto, compararemos la eficiencia de ésa estructura de datos con un Montículo de Fibonacci o 'Fibonacci Heap', la cual es una estructura compleja que utiliza una combinación de listas enlazadas y árboles" +
        "para obtener el elemento de mayor prioridad y que éste sea ejecutado en primer lugar. Toda la información relacionada a éste proceso es luego enviada al PCB mientras se realiza su ejecución",
      pcb: "Un Bloque de Control de Procesos o Process Control Block (PCB) se refiere a un registro especial donde el sistema operativo agrupa toda la información que necesita conocer respecto a algún proceso en particular. Por tanto, cada vez que un proceso se crea, el sistema operativo crea el PCB, que va a servir como descripción en tiempo de ejecución del proceso durante toda la vida del mismo.",
      grafico:
        " La visualización consiste en dos secciones: una dedicada a la cola Fibonacci y otra dedicada a la cola FIFO. A su vez, cada seccion está subdividida en tres subsecciones:",
      grafico2:
        "La columna de la izquierda representa al PCB, con la animación de un monstruo 'consumiendo' el proceso. Abajo del mismo se encuentra información sobre el proceso como su Process ID (PID), su prioridad, y su progreso actual.",
      grafico3:
        "En la columna del medio se encuentra la visualización gráfica de la estructura de datos utilizada como cola. La cola Fibonacci nos muestra la cabeza, que es el elemento más a la izquiera, con su información correspondiente, el árbol que contiene a los descendientes de la cabeza, y el montículo principal, que son los nodos que se conectan en línea recta hacia la derecha de la cabeza," +
        " los cuales representan a los procesos recientemente añadidos. En la cola FIFO el proceso en primer lugar se muestra más a la izquiera, y los siguientes procesos se encuentran conectados hacia la derecha.",
      grafico4:
        "En la columna de la derecha se encuentran las estadísticas de uso de cada estructura de datos, las cuales permitirán analizar la efectividad de cada tipo de cola.",
      estadisticas1: "Cantidad total de procesos ejecutados",
      estadisticas2: "Cantidad de procesos esperando a ser ejecutados",
      estadisticas3:
        "Media de la prioridad de los procesos ejecutados. Mientras menor el valor mejor el resultado.",
      estadisticas4:
        "Media de la cantidad de procesos en espera. Mientras menor el valor mejor el resultado.",
      estadisticas5:
        "Segundos promedio que un proceso espera para ser ejecutado. Mientras menor el valor mejor el resultado.",
      estadisticas6:
        "Valor acumulativo que califica si los procesos con mayor prioridad están siendo ejecutados primero. Mientras menor el valor mejor el resultado.",
    };
  },
};
</script>

<style scoped>
#titulo {
  text-align: center;
  color: #7f696c;
  font-size: 4em;
  font-weight: 100;
}

.analisis {
  padding: 50px;
  width: 65%;
  justify-content: center;
  margin: auto;
}

html body * {
  text-align: center;
}
.nombre {
  color: #d0c277;
  font-size: 1.5em;
}

.Introduccion {
  color: #b26e63;
  font-size: 2.5em;
}
.parrafo {
  font-size: 20px;
  justify-content: center;
  width: 60%;
  text-align: justify;
  margin: auto;
  padding: 0.4em;
}
.elemLista {
  font-size: 20px;
  justify-content: center;
  width: 60%;
  text-align: justify;
  margin: auto;
  padding: 0.25em;
}

img {
  display: block;
  margin: 0 auto;
  width: 200px;
  padding-top: 23px;
  -webkit-transition: width 2s, padding-top 2s;
  transition: width 2s, padding-top 2s;
  height: auto;
}

h3 {
  font-size: 1.4em;
  color: #7f696c;
}

#visualize {
    padding-top: 1em;
}
</style>

