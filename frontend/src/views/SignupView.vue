<template>
    <LogSign>
        <template v-slot:re-password>
            <label for="re-password">Confirm Password:</label>
            <input type="password" name="re-password" v-model="rePassword">
        </template>
        <template v-slot:btn>
            <button class="btn">Sign up</button>
        </template>
    </LogSign>
</template>

<script>
import { ref } from 'vue';
import LogSign from '../components/LogSign.vue'

export default {
    name: "Signup View",
    components: {LogSign},
    setup () {
        

        return {}
    }
}
</script>

<style lang="scss" scoped>

</style>