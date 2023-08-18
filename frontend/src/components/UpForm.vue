<template>
    <div class="form-container">
      <form action="#" @submit.prevent="handleUpdate">
        <div>Update A Product By Product ID</div>
        <label for="ID">Product Number:</label>
        <input type="number" name="ID" v-model="ID">
        <label for="name">Name:</label>
        <input type="text" name="name" v-model="name">
        <label for="catagory">Catagory:</label>
        <select name="catagory" v-model="category">
          <option value="electronics">Electronics</option>
          <option value="transportation">Transportation</option>
          <option value="education">Education</option>
          <option value="sports">Sports</option>
          <option value="equipment">Tools And Equipment</option>
        </select>
        <label for="description">Description:</label>
        <input type="text" name="description" v-model="description">
        <label for="price">Price:</label>
        <input type="number" name="price" step="any" v-model="price">
        <label for="stock">Stock:</label>
        <input type="number" name="stock" v-model="stock">
        <label for="product-img">Image:</label>
        <input type="file" name="product-img" @change="getFile">
        <button class="btn">Submit Form</button>
      </form>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    name: 'Update form component',
    setup (props, context) {
        const ID = ref(null);
        const name = ref(null);
        const category = ref(null);
        const price = ref(null);
        const stock = ref(null);
        const description = ref(null);

        let fileName = null

        const getFile = (e) => {
            fileName = e.target.files[0].name;
            console.log(fileName);
        }

        function handleUpdate() {
            context.emit('submitUpdate', {
                id: ID.value,
                name: name.value,
                category: category.value,
                price: price.value,
                stock: stock.value,
                description: description.value,
                img_file: fileName
            })
        }

        return {handleUpdate, getFile, ID, name, category, price, stock, description}
    }
}
</script>

<style>

</style>