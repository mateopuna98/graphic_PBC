<template>
    <div class="pcb">
        <h1 class="h1-pcb"> PCB {{type}}</h1>
        <div class="monster"></div>
    </div>
</template>


<script>
export default {
    name: 'PCB',
    props: {
        type: String
    }
}

</script>


<style scoped>
/* h1 {
    color: blue
} */
/* .pcb {
    background: lig;
} */
.monster {
  width: 190px;
  height: 240px;
  margin: 2% auto;
  background: url('https://treehouse-code-samples.s3.amazonaws.com/CSS-DD/codepen/blog/monster.png') left center;
  -webkit-animation: play .6s steps(10) infinite;
}

@-webkit-keyframes play {
  100% { background-position: -1900px; }
}
</style>