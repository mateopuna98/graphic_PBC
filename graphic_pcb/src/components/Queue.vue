<template>
    <div class="queue">
        <h1 class="h1-sub"> Cola {{type}}</h1>
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
