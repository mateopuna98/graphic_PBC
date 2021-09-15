<template>
  <div
    class="canvas"
    :id="`${type}Display`"
    @mouseover="hover = true"
    @mouseout="hover = false"
  >
    <h1 class="h1-sub title">Cola {{ type }}</h1>
    <div id="graphics" class="graphics">
      <cytoscape class ="cyto" :id="`${type}canvas`" :ref="`${type}cy`" :config="config">
        <cy-element
          v-for="def in elements"
          :key="`${def.data.id}`"
          :definition="def"
        /> </cytoscape
      >`
    </div>
  </div>
</template>


<script>
export default {
  name: "Queue",
  props: {
    type: String,
    elements: Array,
  },

  data() {
    return {
      config: {
        wheelSensitivity: 0.2,
        style: [
          {
            selector: "node[label]",
            style: {
              label: "data(label)",
            },
          },
          {
            selector: "edge[label]",
            style: {
              label: "data(label)",
              "curve-style": "bezier",
            },
          },
        ],
      },
      hover: false,
    };
  },

  watch: {
    hover: function (val) {
      if (val) {
        document.querySelector(
          "#" + this.type.toLowerCase() + "Display"
        ).style.border = "2px solid #9c9ea4";
      } else {
        document.querySelector(
          "#" + this.type.toLowerCase() + "Display"
        ).style.border = "0px solid #9c9ea4";
      }
    },
  },
};
</script>

<style scoped>
.title {
  text-align: center;
}
#cytoscape-div {
  height: 800px ;
}
.canvas {
  overflow: hidden;
  height: 100%;
}

.graphics {
height: 100%;
}

.cyto {
height: 100%;
}

</style>
