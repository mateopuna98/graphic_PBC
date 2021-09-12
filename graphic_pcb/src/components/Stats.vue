<template>
    <div class="stats">
        <h1>Stats {{type}}</h1>
    </div>
</template>


<script>
export default {
    name: 'Stats',
    props: {
        type: String
    }
}

</script>

<style scoped>
    h1 {
        color: green
    }
    .stats {
        background: lightblue;
    }
</style>