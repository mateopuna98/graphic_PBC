<template>
    <div class="pcb">
        <h1> PCB {{type}}</h1>
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
h1 {
    color: blue
}
.pcb {
    background: lightgoldenrodyellow;
}
</style>