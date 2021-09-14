<template>
    <div class="pcb">
        <h1 class="h1-sub"> PCB {{type}}</h1>
        <div  v-if="estadoMonstruo === 'monstruo-tranquilo'" class="monstruo-tranquilo"></div>
        <div  v-if="estadoMonstruo === 'monstruo-excitado'" class="monstruo-excitado"></div>
        <div v-else-if="estadoMonstruo === 'monstruo-normal'" class="monstruo-normal"></div>
    </div>
</template>


<script>
export default {
    name: 'PCB',
    props: {
        type: String
    },
    computed: {
      estadoMonstruo() {
        return this.$store.state.estadoMonstruo
      }
    }
}

</script>


<style scoped>

.monstruo-normal {
  width: 190px;
  height: 240px;
  margin: 2% auto;
  background: url('https://treehouse-code-samples.s3.amazonaws.com/CSS-DD/codepen/blog/monster.png') left center;
  -webkit-animation: play .6s steps(10) infinite;
}

.monstruo-excitado {
  width: 190px;
  height: 240px;
  margin: 2% auto;
  background: url('https://treehouse-code-samples.s3.amazonaws.com/CSS-DD/codepen/blog/monster.png') left center;
  -webkit-animation: play .15s steps(10) infinite;
}

.monstruo-tranquilo {
  width: 190px;
  height: 240px;
  margin: 2% auto;
  background: url('https://treehouse-code-samples.s3.amazonaws.com/CSS-DD/codepen/blog/monster.png') left center;

}

@-webkit-keyframes play {
  100% { background-position: -1900px; }
}
</style>