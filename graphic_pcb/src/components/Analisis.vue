<template>
  <div class="analisis">
      <img src="https://kbaile03.github.io/projects/fibo_dijk/images/graph_icon.png" alt="graph icon">
      <h1 id="titulo">Colas prioritarias PCB con Fibonacci Heap y FIFO - Una visualización</h1>
      <h2 class="nombre">Mateo Puña</h2>
      <h2 class="nombre">Javier Soruco</h2>
      <h2 class="Introduccion">Introducción</h2>
      <p class="parrafo">{{introduccion}} </p>
      <h2 class="Introduccion"> Qué es un PCB?</h2>
            <p class="parrafo">Aqui es la introduccion hdp</p>

      <h2 class="Introduccion"> Descripción del gráfico</h2>
            <p class="parrafo">Aqui es la introduccion hdp</p>

      <h2 class="Introduccion"> Explicación de estadísticas</h2>
            <p class="parrafo">Aqui es la introduccion hdp</p>



  </div>
</template>

<script>

export default {
    name: 'Analisis',
    data() {
        return {
        introduccion: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Veniam repellendus harum cumque vel iure suscipit, natus quas explicabo non, expedita blanditiis et quisquam aliquam! Velit corrupti voluptate quia nobis veniam, deleniti unde beatae cumque voluptates, voluptatibus quidem deserunt eum vero. Illo voluptatibus iure animi nihil hic, magnam laboriosam exercitationem dicta ullam, a nam provident culpa dolorum, fuga ratione deleniti dignissimos unde. Magnam accusamus a voluptatibus dolorem consequatur quidem autem vel maiores hic, neque minima, necessitatibus corporis, voluptas amet beatae! Velit provident eveniet optio, quos natus nesciunt. Nam officiis quaerat voluptas, reiciendis itaque a eligendi nihil earum mollitia, repellendus culpa doloribus!"
        }
    }
}

</script>

<style scoped>
 #titulo{
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

 .Introduccion{
     color: #b26e63;
     font-size: 2.5em;
 }
 .parrafo {
    font-size: 20px;     
    justify-content: center;
    width: 60%;
    text-align: justify;
        margin: auto;


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
</style>

