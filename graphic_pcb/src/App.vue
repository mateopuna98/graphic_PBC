<template>
  <div>
    <div class="mainGrid">
      <div class="c1">
        <div class="c11">
          <PCB type="Fibonacci" />
          <Button />
        </div>

        <PCB type="FIFO" />

      </div>
      <div class="c2">
        <Queue type="Fibonacci" />
        <Queue type="FIFO" />


      </div>
      <div class="c3">
        <Stats type="Fibonacci" />
        <Stats type="FIFO" />

      </div>

    </div>
  </div>
</template>

<script>
import Button from "./components/Button";
import PCB from "./components/PCB";
import Queue from "./components/Queue";
import Stats from "./components/Stats";

export default {
  name: "App",
  components: {
    Button,
    PCB,
    Queue,
    Stats,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.mainGrid {
  display: grid;
  grid-template-columns: 2fr 4fr 2fr;
  height: 800px;
  gap: 1em
}
.c1 {
  display: grid;
  grid-template-rows: 1fr 1fr ;
  background: #2c3e50;
}
.c11 {
  display: grid;
  grid-template-rows: 3fr 1fr ;
  background: #2c3e50;
}
.c2 {
  display: grid;
  grid-template-rows: 1fr 1fr ;
  background: #2c3e50;
}
.c3 {
  display: grid;
  grid-template-rows: 1fr 1fr ;
  background: #2c3e50;
}
</style>
