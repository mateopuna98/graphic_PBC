<template>
  <div class="button">
    <button @click="onClick()">Añadir {{ cantidadProcesos }} procesos en ambas colas</button>
  </div>
</template>


<script>
export default {
  name: "Boton",
  data() {
    return {
      cantidadProcesos: parseInt(Math.random() * 10),
    };
  },
  methods: {
    onClick() {
      const n = this.cantidadProcesos;
      console.log(n);
      this.cantidadProcesos = parseInt(Math.random() * 10);
    },
  },
};
</script>

<style scoped>
button {
  font-family: "Roboto Slab", serif;
  padding: 20px;
  color: white;
  background-color: #52a6bf;
  border: 0px;

  /* color: orange */
}
.button {
  padding: 100x;
}
</style>