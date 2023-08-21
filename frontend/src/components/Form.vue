<template>
    <div class="form-container">
      <form action="#" @submit.prevent="handleSubmit">
        <div>Enter A Product</div>
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
    name: "Form Component",
    setup (props, context) {
        const name = ref('');
        const category = ref('');
        const price = ref('');
        const stock = ref('');
        const description = ref('');

        let fileName;

        const getFile = (e) => {
            fileName = e.target.files[0].name;
            console.log(fileName);
        }

        function handleSubmit() {
            context.emit('submitForm', {
                name: name.value,
                category: category.value,
                price: price.value,
                stock: stock.value,
                description: description.value,
                img_file: fileName
            })
        }

        return {handleSubmit, getFile, name, category, price, stock, description}
    }
}
</script>

<style>
    .form-container{
    margin: 20px auto;
    padding: 30px;
    width: min-content;
    border: 2px solid #DFF1FF;
    border-radius: 10px;
  }

  .form-container > form > div{
    font-size: larger;
    margin-bottom: 20px;
  }

  .form-container > form > label{
    font-size: larger;
  }

  .form-container > form > input{
    padding: 10px;
    margin-bottom: 10px;
    width: 350px;
    font-size: 18px;
  }
</style>