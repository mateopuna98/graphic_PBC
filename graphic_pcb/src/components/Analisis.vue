<template>
    <div class="text">
        <h1 class="titulo-analisis">Análisis de los algoritmos</h1>

        <p class="texto">{{introduccionAnalisis}}</p>
        <h2 class="titulo-analisis">Process Control Block</h2>
         <p class="texto">{{pcb}}</p>
        <h2 class="titulo-analisis">Cola Fibonacci</h2>
         <p class="texto">{{colaFibonacci}}</p>
        <h3 class="titulo-analisis">Análisis amortizado cola Fibonacci</h3>

    </div>
</template>

<script>
export default {
    name: 'Texto',
    data() {
        return {
        introduccionAnalisis: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni accusantium dolores minus tenetur. Rem saepe accusamus natus ratione commodi atque iste magnam eveniet expedita accusantium quod odio quidem explicabo consequatur molestias consequuntur totam quos itaque, in velit dicta animi non sit? Id ipsa odio illum sunt doloremque culpa repellat! Maxime exercitationem quo cumque tenetur eligendi qui. Vitae voluptatem necessitatibus labore, dicta quidem nobis qui sunt odit facilis praesentium eum ab sint quae? Quia incidunt voluptatem consequuntur cumque neque alias mollitia officia impedit explicabo quo, eius cupiditate qui obcaecati recusandae consequatur expedita temporibus est vero ut natus rerum, quaerat consectetur. Non.",
        pcb: "Aqui la descripción acerca del Process Control Block",
        colaFibonacci: "Aqui la descripcion de la cola Fibonacci"
        }
    }
}

</script>


<style>
.titulo-analisis {
    color: #7f696c;
;
}
.text {
    width: 800px;
    padding: 20px;
    margin: auto;
}
.texto {
    text-align: justify;
    font-size: 18px;
}
</style>