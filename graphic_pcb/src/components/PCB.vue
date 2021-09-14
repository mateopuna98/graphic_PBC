<template>
    <div class="pcb">
        <h1 class="h1-sub"> PCB {{type}}</h1>

        <div  v-if="estadoMonstruo === 'monstruo-tranquilo'" class="monstruo-tranquilo"></div>
        <div  v-if="estadoMonstruo === 'monstruo-excitado'" class="monstruo-excitado"></div>
        <div v-else-if="estadoMonstruo === 'monstruo-normal'" class="monstruo-normal"></div>
        
        <p>Process Data:</p>
        <div class="processData">

          <div class="dataRow">
            <p class="title">PID:</p>
            <p class="data">{{process["PID"]}}</p>
          </div>

        </div>
        <div class="processData">

          <div class="dataRow">
            <p class="title">Prioridad:</p>
            <p class="data">{{process["prioridad"]}}</p>
          </div>

        </div>

        <div class="countdown">
          
          <p>Time to end:</p>

        </div>

    </div>
</template>


<script>
export default {
    name: 'PCB',
    props: {
        type: String,
        process: Object
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

.processData {
  display: grid;
  grid-template-rows: 33% 33%;
}

.dataRow {
  display: grid;
  grid-template-columns: 50% 50%;
  margin-top: -1vh;
}

.title {
  text-align: left;
  margin-left: 1vw;
}

.data {
  text-align: right;
  margin-right: 1vw;
}

.countdown {

  display: grid;
  grid-template-rows: 50% 50%;
  margin-top: -1vh;

}

</style>