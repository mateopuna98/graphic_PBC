<template>
  <div class="boton">
    <button
    id="botonAgregar"
    @click="onClick()"
    >Añadir
    {{ cantidadProcesos }} procesos en ambas colas
    </button>
  </div>
</template>


<script>
export default {
  name: "Boton",
  data() {
    return {
      cantidadProcesos: parseInt(1 + Math.random() * 5),
      kencha: false
    };
  },
  methods: {
    onClick() {
      this.$store.dispatch('agregarProcesos', { 'cantidad': this.cantidadProcesos })
      this.$store.dispatch('excitarMonstruo')
      this.kencha = true
      document.querySelector('#botonAgregar').style.background = "#52a6bf8c" 
      setTimeout(() => {
        this.kencha = false
        document.querySelector('#botonAgregar').style.background = "#52a6bf" 
        this.cantidadProcesos = parseInt(1 + Math.random() * 10);
      }, 200);
    },
  },
};
</script>

<style scoped>
button {
  font-family: "Roboto Slab", serif;
  padding: 20px;
  color: white;
  background: #52a6bf;
  border: 0px;

  /* color: orange */
}
.boton {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>