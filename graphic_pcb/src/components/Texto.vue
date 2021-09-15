<template>
    <div class="data">
        <h1 class="titulo">Análisis de los algoritmos</h1>
        <p class="texto">{{introduccionAnalisis}}</p>
        <h3 class="subtitulo titulo">Análisis amortizado cola Fibonacci</h3>
        <p class="texto">{{intrudccionAmortiado}}</p>
        <div class="formula">  
          <img :src="imagenEcuacionPotencial" alt="Ecuacion Potencial">
        </div>
        <p class="texto">{{explicacionFormula}}</p>
        <h3 class="subtitulo titulo">Análisis amortizado: Inserción</h3>
        <p class="texto">{{introduccionInsercion}}</p>
        <div  class="formula">
            <img :src="imagenInsercion" alt="Costo amortizado Insercion">
        </div>
        <p class="texto">{{conclucionInsercion}}</p>
        <h3 class="subtitulo titulo">Análisis amortizado: Reducción de llave</h3>
        <p class="texto">{{introduccionReduccion}}</p>
        <h3 class="caso titulo">Caso 1: No se violan las reglas de fibonacci heap</h3>
        <p class="texto">{{introduccionReduccion1}}</p>
        <h3 class="caso titulo">Caso 2: Se violan las reglas de fibonacci heap</h3>
        <p class="texto">{{introduccionReduccion2}}</p>
        <div  class="formula">
            <img :src="imagencaso2Reduccion" alt="Costo amortizado Reduccion de llave">
        </div>
        <p class="texto">{{introduccionReduccion21}}</p>
        <div  class="formula">
            <img :src="imagenEcuacionCadena" alt="Costo amortizado Reduccion de llave en cadena">
        </div>
        <p class="texto">{{ conclusionReduccion }}</p>
        <h3 class="subtitulo titulo">Análisis amortizado: Eliminar minimo</h3>
        <p class="texto">¨{{introduccionEliminar}}</p>
        <h3 class="caso titulo">Caso 1: La raiz minima eliminada tiene un hijo que herede su posicion: </h3>
        <div  class="formula">
            <img :src="imagenEliminarHeredero" alt="Costo amortizado de eliminacion con un heredero">
        </div>
        <h3 class="caso titulo">Caso 2: La raiz minima eliminada NO tiene un hijo que herede su posicion: </h3>
        <div  class="formula">
            <img :src="imagenEliminarSolo" alt="Costo amortizado de eliminacion sin un heredero">
        </div>
        <p class="texto">{{introduccionConsolidacion}}</p>
        <div  class="formula">
            <img :src="imagenCostoConsolidacion" alt="Costo amortizado de una sola consolidacion">
        </div>
        <p class="texto">{{puenteConsolidacion}}</p>
        <div  class="formula">
            <img :src="imagenCostoTotalEliminacion" alt="Costo amortizado de una eliminacion mas consolidaciones">
        </div>
        <p class="texto">{{conclusionEliminar}}</p>
        

    </div>
</template>

<script>
import imagenEcuacionPotencial from "../assets/ecuaciones/ecuacionPotencial.png"
import imagenInsercion from "../assets/ecuaciones/ecuacionInsercion.png"
import imagencaso2Reduccion from "../assets/ecuaciones/ecuacioncaso2recuccion.png"
import imagenEcuacionCadena from "../assets/ecuaciones/ecuacionCadena.png"
import imagenEliminarHeredero from "../assets/ecuaciones/eliminarHeredero.png"
import imagenEliminarSolo from "../assets/ecuaciones/eliminarSolo.png"
import imagenCostoConsolidacion from "../assets/ecuaciones/costoConsolidacion.png"
import imagenCostoTotalEliminacion from "../assets/ecuaciones/totalDelete.png"

export default {
    name: 'Texto',
    data() {
        return {
        imagenEcuacionPotencial : imagenEcuacionPotencial,
        imagenInsercion: imagenInsercion,
        imagencaso2Reduccion: imagencaso2Reduccion,
        imagenEcuacionCadena: imagenEcuacionCadena,
        imagenEliminarHeredero: imagenEliminarHeredero,
        imagenEliminarSolo: imagenEliminarSolo,
        imagenCostoConsolidacion: imagenCostoConsolidacion,
        imagenCostoTotalEliminacion : imagenCostoTotalEliminacion,
        introduccionAnalisis: "El algoritmo de cola prioritaria utilizado 'Monticulo Fibonacci'," + 
        " es un algoritmo conocido por reducir la complejidad de otros algorimtos como Dijkstra o Prim, reduciendo su complejidad convirtiendolos en algoritmos mas factibles para su uso comercial," + 
        " esto debido a que el costo amortizado de sus operaciones mas importenta es relativamente bajo.",
        intrudccionAmortiado: "En un montículo de Fibonacci con N elementos se define la función potencial como:",
        explicacionFormula: "Donde las raices son los nodos en el montículo principal y los ‘loosers’ son los nodos que han perdido un hijo por la operacion decrease key. ",
        introduccionInsercion: "Dado C el número de raíces del montículo y L el numero de loosers, y con s el costo por operación, una inserción genera el siguiente costo amortizado:",
        conclucionInsercion: "Por lo tanto, el costo amortizado por inserción es O(1).",
        introduccionReduccion: "Contemplamos 2 casos, cuando la nueva llave es mayor que la del nodo padre y por tanto no se violan las reglas de fibonacci heap y cuando la nueva llave es menor y estas reglas son violadas:",
        introduccionReduccion1: "Cuando no existe violación a las reglas, la estructura no se ve afetada, por ende, la diferencia de potenciales es 0 y el costo amortizado es s = O(1).", 
        introduccionReduccion2: "Se violan las reglas del árbol, por ende, el nodo se inserta en la raíz generando la siguiente diferencia de potencial: ",
        introduccionReduccion21: "Tambien se puede asumir el caso que todo el conjunto de nodos padres sean 'lossers' y desencadenen una reaccion insertando L nodos en la raiz: ",
        conclusionReduccion: "En cualquiera de los casos, la complejidad es O(1)",
        introduccionEliminar: "Sin tomar en cuenta la cosolidación o merge, un delete puede tener 2 casos: ",
        introduccionConsolidacion: "Ahora consideremos que esta operación de eliminación tiene esta hecha sobre un montículo de N nodos entonces se tendría que realizar log(N), con esto en mente calculemos el costo amortizado de una consolidación:",
        puenteConsolidacion: "con esto sabemos que el costo amortizado de un delete con log(N) consolidaciones es: ",
        conclusionEliminar: "En cualquiera de los casos, la complejidad es O(log(N))"
        }
    }
}

</script>

<style scoped>

    .titulo{
     text-align: center;
     color: #b26e63;
     font-size: 2.5em;
     font-weight: 100;
    }
    .subtitulo{
        font-size: 1.5em;
    }
    .caso{
        font-size: 1em;
    }
    .text{
        font-size: 20px;
        justify-content: center;
        width: 60%;
        text-align: justify;
        margin: auto;
        padding: 0.5em;
    }
    .formula{
        align-self: center;
        text-align: center;
    }
    .data {
        padding: 50px;
        width: 45%;
        align-items: center;
        justify-content: center;
        margin: auto;
        text-align: justify;
    }
</style>
