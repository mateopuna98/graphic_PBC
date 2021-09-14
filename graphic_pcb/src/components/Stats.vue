<template>
  <div class="stats">
    <h1 class="h1-sub">Estadísticas {{ type }}</h1>
    <ul v-if="type === 'Fibonacci'">
      <li>Procesos terminados: {{ statsFibo.procesosTerminados }}</li>
      <li>Tamaño actual cola: {{ statsFibo.tamanoCola }}</li>
    </ul>

    <ul v-else>
      <li>Procesos terminados: {{ statsFifo.procesosTerminados }}</li>
      <li>Tamaño actual cola: {{ statsFifo.tamanoCola }}</li>
    </ul>
    <h5>Promedio en los últimos 10 procesos:</h5>
    <ul v-if="type === 'Fibonacci'">
      <li>Prioridad promedio: {{ statsFibo.prioridadPromedio }}</li>
      <li>Tamaño de cola promedio: {{ statsFibo.tamanoColaPromedio }}</li>
      <li>Tiempo de espera promedio: {{ statsFibo.tiempoEsperaPromedio }}</li>
      <li>Valor ponderado de pérdida: {{ statsFibo.valorPonderadoPerdida }}</li>
    </ul>
    <ul v-else>
      <li>Prioridad promedio: {{ statsFifo.prioridadPromedio }}</li>
      <li>Tamaño de cola promedio: {{ statsFifo.tamanoColaPromedio }}</li>
      <li>Tiempo de espera promedio: {{ statsFifo.tiempoEsperaPromedio }}</li>
      <li>Valor ponderado de pérdida: {{ statsFifo.valorPonderadoPerdida }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Stats",
  props: {
    type: String,
  },
  computed: {
    statsFibo() {
      return this.$store.state.estadisticas.fibonacciHeap;
    },
    statsFifo() {
      return this.$store.state.estadisticas.fifo;
    },
  },
};
</script>

<style scoped>
h4 {
  text-align: left;
  padding-left: 20px;
}
ul,
li {
  margin: 0;
  padding-left: 10px;
  text-align: left;
  list-style-type: none;
  font-size: 15px;
}
</style>