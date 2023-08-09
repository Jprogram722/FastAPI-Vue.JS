
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
    <Form @submitForm="handleSubmit"/>
    <DelForm @submitDelete="handleDelete"/>
  </body>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import Form from './components/Form.vue';
import DelForm from './components/DelForm.vue';

export default{
  name: 'main app',
  components: {Form, DelForm},
  setup() {
    
    const defaultURL = 'http://localhost:8000/api';
    
    const products = ref([]);

    onMounted(async () => {
      try{
        const {data} = await axios.get(defaultURL+'/');
        products.value = data
      }
      catch(err){
        console.log(err.message);
      }
    })

    const handleSubmit = async (formInfo) => {
      try{
        await axios.post(defaultURL + '/form', formInfo);
        window.location.reload();
      }
      catch(err){
        console.log(err.message);
      }
    }
    
    const handleDelete = async (formInfo) => {
      try{
        await axios.delete(defaultURL + '/delete/' + formInfo.id);
        window.location.reload();
      }
      catch(err){
        console.log(err.message);
      }
    }

    return {handleSubmit, handleDelete, products}
  }
}
</script>

<style>
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
</style>
