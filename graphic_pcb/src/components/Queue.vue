<template>
    <div class="queue">
        <h1 class="h1-queue"> Cola {{type}}</h1>
    </div>
</template>


<script>
export default {
    name: 'Queue',
    props: {
        type: String
    }
}

</script>

<style scoped>
    /* h1 {
        color: red
    } */
    /* .queue {
        background: lightcoral;
    } */
</style>