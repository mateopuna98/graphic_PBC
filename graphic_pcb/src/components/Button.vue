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
      cantidadProcesos: parseInt(1 + Math.random() * 5),
    };
  },
  methods: {
    onClick() {
      console.log(this.$store.dispatch('agregarProcesos', { 'cantidad': this.cantidadProcesos }))
      this.$store.dispatch('excitarMonstruo')
      this.cantidadProcesos = parseInt(1 + Math.random() * 5);
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
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>