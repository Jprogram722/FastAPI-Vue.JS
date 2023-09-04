<template>
    <div class="form-container login">
      <form action="#" @submit.prevent="handleSubmit">
        <h1>Sign Up</h1>
        <label for="username">Username:</label>
        <input type="text" name="username" v-model="username">
        <label for="password">Password:</label>
        <input type="password" name="password" v-model="password">
        <slot name="re-password"></slot>
        <slot name="btn"></slot>
      </form>
    </div>
</template>

<script>
import { ref } from 'vue'

export default {
    name: 'login/signup component',
    setup (props ,context) {

        const username = ref('');
        const password = ref('');
        
        const handleSubmit = () => {
            context.emit('submitLogSign', {
                username: username.value,
                password: password.value
            });
        };

        return {username, password, handleSubmit}
    }
}
</script>

<style lang="scss" scoped>

</style>