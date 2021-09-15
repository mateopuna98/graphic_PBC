<template>

  <div class="main">
    <link href='https://fonts.googleapis.com/css?family=Roboto Slab' rel='stylesheet'>

    <div id="header">
      <h1>Proyecto Final Algorítmica II</h1>
    </div>
    <Analisis />

    <div class="mainGrid">

      <div class="c1">
        <div class="c11">
          <PCB class="pcb-fibo" type="Fibonacci" :process=$store.getters.getPBCFibonacciHeap :estadoMonstruo=$store.state.estadoMonstruoFibonacci />
          <Button />
        </div>
        <PCB class="pcb-fifo" type="FIFO" :process=$store.getters.getPBCFifo :estadoMonstruo=$store.state.estadoMonstruoFIFO />
      </div>

      <div class="c2">

        <Queue id="fibonacciDisplay" type="Fibonacci" :elements=$store.getters.getFibonacciHeap />
        <Queue id="fifoDisplay" type="FIFO" :elements=$store.getters.getFifo />
      </div>

      <div class="c3">
        <Stats type="Fibonacci" />
        <Stats type="FIFO" />
      </div>

    </div>

    <div>

      <Texto />
    </div>
    </div>
</template>

<script>
import Button from "./components/Button";
import PCB from "./components/PCB";
import Queue from "./components/Queue";
import Stats from "./components/Stats";
import Texto from "./components/Texto";
import Analisis from "./components/Analisis";

export default {
  name: "App",
  components: {
    Button,
    PCB,
    Queue,
    Stats,
    Texto,
    Analisis
  },

  created() {
    this.$store.dispatch('getData')
  },

};
</script>

<style>

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

#header {
  position: fixed;
  display: block;
  height: 50px;
  width: 100%;
  background-color: #52a6bf;
  margin-right: -8px;
}
#header h1{
  color: white;
  text-align: left;
  font-size: 20px;
  padding-left: 10px;
}
html body {
  height: 100%;
  margin: 0;
}

html * {
    font-family: "Roboto Slab", serif !important;
}
.main {
  position:absolute;
  top:0px;
  right:0px;
  bottom:0px;
  left:0px;  
  background: #ffffff;

}
h1 {
  font-weight: 100;
  color: #808080;
}
.h1-sub {
  color: #7f696c;
}
.mainGrid {
  display: grid;
  grid-template-columns: 2fr 4fr 2fr;
  height: 1400px;
  padding: 50px;
  gap: 1em
}
.c1 {
  display: grid;
  grid-template-rows: 60% 40%;
}
.c11 {
  display: grid;
  grid-template-rows: 3fr 1fr ;
}
.pcb-fibo:hover {
    border: 0.1em solid #9c9ea4;
}

.pcb-fifo:hover {
    border: 0.1em solid #9c9ea4;
}
.c2 {
  display: grid;
  grid-template-rows: 60% 40%;
}
.c3 {
  display: grid;
  grid-template-rows: 60% 40%;
}

.c3 div:hover {
  border: 0.1em solid #9c9ea4;
}

</style>
