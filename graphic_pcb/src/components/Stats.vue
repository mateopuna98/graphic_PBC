<template>
  <div class="stats">
    <h1 class="h1-stats">Estadísticas {{ type }}</h1>
    <ul>
      <li>Procesos terminados:        {{procesosTerminados}}</li>
    </ul>
    <h4>Promedio en los últimos 10 procesos:</h4>
    <ul>
      <li>Prioridad promedio:         {{prioridadPromedio}}</li>
      <li>Tamaño de cola promedio:    {{tamanoPromedio}}</li>
      <li>Tiempo de espera promedio:  {{esperaPromedio}}</li>
      <li>Valor ponderado de pérdida: {{ponderado}}</li>

    </ul>
  </div>
</template>


<script>
export default {
  name: "Stats",
  props: {
    type: String,
  },
  data() {
      return {
          procesosTerminados: 0,
          prioridadPromedio: 0,
          tamanoPromedio: 0,
          esperaPromedio: 0,
          ponderado: 0
      } 
  }
};
</script>

<style scoped>
    h4 {
    text-align: left;
    padding-left: 20px;

    }
    ul, li { 
    margin: 0; 
    padding-left: 10px;
    text-align: left;
    list-style-type: none;
    font-size: 15px;

    }
</style>