<template>
    <div class="form-container">
      <form action="#" @submit.prevent="handleDelete">
        <div>Delect a Product by Product Number</div>
        <label for="ID">Product Number:</label>
        <input type="number" name="ID" v-model="ID">
        <button class="btn">Submit Form</button>
      </form>
    </div>
</template>

<script>
import { ref } from 'vue';
 
export default {
    name: "Delete Form Component",
    setup (props, context) {
        const ID = ref('');

        function handleDelete() {
            context.emit('submitDelete', {id: ID.value});
        }

        return {handleDelete, ID}
    }
}
</script>

<style>
  
</style>