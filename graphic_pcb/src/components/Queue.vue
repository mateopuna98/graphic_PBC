<template>
    <div class="queue">
        <h1 class="h1-sub"> Cola {{type}}</h1>
        <div id="grafico-heap"></div>
    </div>
</template>


<script>
//import greuler from "greuler"

export default {
    name: 'Queue',
    props: {
        type: String,
    },
    created() {
        

    }
}

</script>
