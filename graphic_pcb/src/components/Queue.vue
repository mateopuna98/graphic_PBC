<template>
    <div :id="`${type}Display`" @mouseover="hover = true" @mouseout="hover = false">
        <h1 class="h1-sub"> Cola {{type}}</h1>
        <div id="graphics" class="graphics">

            <cytoscape ref="cy" :config="config">
                <cy-element
                    v-for="def in elements"
                    :key="`${def.data.id}`"
                    :definition="def"
                />
            </cytoscape>`
        </div>

        

    </div>
</template>


<script>

export default {
    name: 'Queue',
    props: {
        type: String,
        elements: Array
    },

    data() {
        return {
            config: {
            style: [
                {
                selector: 'node[label]',
                style: {
                    label: 'data(label)',
                },
                },
                {
                selector: 'edge[label]',
                style: {
                    label: 'data(label)',
                    'curve-style': 'bezier',
                },
                },
            ],
            },
            hover: false,
        }
    },

    watch: {
    hover: function (val) {

      if (val) {
        document.querySelector("#" + this.type.toLowerCase() + "Display").style.border= "2px solid #9c9ea4"
      } else {
        document.querySelector("#" + this.type.toLowerCase() + "Display").style.border= "0px solid #9c9ea4"
      }

    }

  }
    
}

</script>

<style scoped>

#cytoscape-div {
  height: 100% !important;
  min-height: unset !important;
}

.graph-container {
  font-family: sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.cy-graph {
  height: 400px;
  width: 600px;
  background: lightblue;
  border: 1px solid red;
  display: block;
}

</style>
