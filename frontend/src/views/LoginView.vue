<template>
    <LogSign>
        <template v-slot:btn>
            <button class="btn">Log in</button>
        </template>
    </LogSign>
</template>

<script>
import { ref } from 'vue';
import LogSign from '../components/LogSign.vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

export default {
    name: 'Login View',
    components: {LogSign},
    setup () {
        

        return {}
    }
}
</script>

<style>
    .login {
        margin-top: 250px;
    }
</style>