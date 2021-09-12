<template>
    <div class="button">
        <button @click="onClick()"> Añadir {{cantidadProcesos}} procesos</button>
    </div>
</template>


<script>
 export default{
     name : "Boton",
     data() {
         return {
            cantidadProcesos: parseInt(Math.random()*10)
         }
     },
     methods: {
        onClick() {
            const n = this.cantidadProcesos
            console.log(n)
            this.cantidadProcesos = parseInt(Math.random()*10)
        }
     }
 }
</script>

<style scoped>
 button {
     padding: 10px;
     color: orange
 }
 .button {
     background: lightgreen;
 }
</style>