
<template>
  <header>
    <div class="navbar">
      <h1>Fast API test with vue JS</h1>
      <ul>
        <li><a href="#">About</a></li>
      </ul>
    </div>
  </header>

  <body>
    <div class="grid-container">
      <div class="grid-item" v-for="product in products">
        <img v-bind:src="product.img_path" alt="No Image Found">
        <p class="product-name">{{ product.name }}</p>
        <p class="product-id">Product number: #{{ product.id }}</p>
        <p class="product-catagory">category: {{ product.catagory }}</p>
        <p class="product-price">${{ product.price }}</p>
        <p class="product-stock">{{ product.stock }} left in stock</p>
      </div>
    </div>
    <div class="form-container">
      <form action="#" @submit="handleSubmit">
        <div>Enter A Product</div>
        <label for="name">Name:</label>
        <input type="text" name="name" v-model="name">
        <label for="catagory">Catagory:</label>
        <input type="text" name="description" v-model="catagory">
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

    <div class="form-container">
      <form action="#" @submit="handleDelete">
        <div>Delect a Product by Product Number</div>
        <label for="ID">Product Number:</label>
        <input type="number" name="ID" v-model="ID">
        <button class="btn">Submit Form</button>
      </form>
    </div>
  </body>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';

export default{
  name: 'main app',
  
  setup() {
    
    const defaultURL = 'http://localhost:8000/api'

    const name = ref('');
    const catagory = ref('');
    const price = ref('');
    const stock = ref('');
    const description = ref('');
    const ID = ref('');
    const img = ref('');
    const products = ref([]);
    let fileName = '';

    onMounted(async () => {
      try{
        const {data} = await axios.get(defaultURL+'/');
        console.log(data[0].img_path)
        products.value = data
        for(let i = 0; i < products.value.length; ++i){
          console.log(typeof products.value[i].img_path)
        }
      }
      catch(err){
        console.log(err.message);
      }
    })

    const getFile = (e) => {
      fileName = e.target.files[0].name;
      console.log(fileName)
    }

    const handleSubmit = async (e) => {
      try{
        const formData = {
          name: name.value,
          catagory: catagory.value,
          description: description.value,
          price: price.value,
          stock: stock.value,
          img_file: fileName
        }
        await axios.post(defaultURL + '/form', formData);
        // window.location.reload();
      }
      catch(err){
        console.log(err.message);
      }
    }
    
    const handleDelete = async () => {
      try{
        await axios.delete(defaultURL + '/delete/' + ID.value);
        window.location.reload();
      }
      catch(err){
        console.log(err.message);
      }
    }

    return {handleSubmit, handleDelete, getFile, name, catagory, price, stock, description, ID, img, products}
  }
}
</script>

<style scoped>
  .navbar{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px;
    gap: 40rem;
    margin: auto 0;
  }

  ul{
    list-style: none;
  }

  a{
    color: rgba(255, 255, 255, 0.87);
    text-decoration: none;
  }

  a:hover{
    color: #0ea5e9;
  }

  img{
    border-radius: 10px;
    width: 250px;
    height: 250px;
  }

  .grid-container{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    padding: 10px;
    grid-gap: 50px;
    margin: 20px 200px;
  }

  .grid-item{
    border: 1px solid #a1a1aa;
    border-radius: 10px;
    background-color: #171717;
    padding: 10px;
    width: 250px;
    word-wrap: break-word;
  }

  .grid-item > p {
    width: 250px;
  }

  .grid-item > .product-price{
    font-weight: bolder;
    font-size: x-large;
  }
  .btn{
    padding: 10px;
    cursor: pointer;
    background-color: #6366f1;
    border: none;
    border-radius: 10px;
    font-size: larger;
  }

  .btn:hover{
    background-color: #4f46e5;
  }

  .purchase-btn{
    width: 250px;
  }

  .form-container{
    margin: 20px auto;
    padding: 30px;
    width: min-content;
    background-color: #171717;
    border: 1px solid #a1a1aa;
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
