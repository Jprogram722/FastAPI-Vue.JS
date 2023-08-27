<template>
  <div>
    <Modal :modalToggle="modalToggle" @close-modal="toggleModal">
      <Form @submitForm="handleSubmit"/>
    </Modal>
    <Navbar/>
    <button class="btn product-btn" @click.left="toggleModal">Add A Product</button>
    <div class="product-promo" v-if="promo_product">
      <div class="wrapper">
        <img class="promo-pic" :src="promo_product.img_path">
        <div>
          <RouterLink :to="{name: 'product', params: {id: promo_product.id}}"><p class="big-text">{{ promo_product.name }}</p></RouterLink>
          <p>{{ promo_product.description }}</p>
          <p class="large-text">${{ promo_product.price }}</p>
        </div>
      </div>
    </div>
    <div class="spinner-container" v-else>
      <div class="spinner"></div>
      <p>Now Loading...</p>
    </div>
    <Items :products="products" @deleteProduct="handleDelete"/>
  </div>
</template>

<script>
import { RouterLink } from 'vue-router';
import axios from 'axios';
import { ref, onMounted } from 'vue';
import Form from '../components/form.vue';
import Items from '../components/Items.vue';
import Modal from '../components/Modal.vue';
import Navbar from '../components/Navbar.vue';

export default{
  name: 'main app',
  components: { Form, Items, Modal, Navbar },
  setup() {
    
    const defaultURL = 'http://localhost:8000/api';
    
    const products = ref([]);
    const promo_product = ref('');
    const modalToggle = ref(false);

    function getRandomInt(max) {
      return Math.floor(Math.random() * max);
    }

    onMounted(async () => {
      try{
        const {data} = await axios.get(defaultURL+'/');
        products.value = data
        const randomInt = getRandomInt(products.value.length);
        promo_product.value = products.value[randomInt];
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

    const toggleModal = () => {
      modalToggle.value = !modalToggle.value;
    }

    return {toggleModal, handleSubmit, handleDelete, products, modalToggle, promo_product}
  }
}
</script>

<style>
  .form-container{
    background-color: #1e293b;
  }

  .navbar{
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px;
    gap: 65rem;
    margin: auto 0;
  }

  ul{
    list-style: none;
  }

  img{
    border-radius: 10px;
    width: 250px;
    height: 250px;
  }

  .btn{
    color: #1e293b;
    padding: 10px;
    cursor: pointer;
    background-color: #daa21c;
    border: none;
    border-radius: 10px;
    font-size: larger;
  }

  .btn:hover{
    background-color: #b18110;
  }

  .purchase-btn{
    width: 250px;
  }

  .product-btn {
    float: right;
    margin-right: 150px;
  }

  .product-promo {
    margin-top: 75px;
    background-color: #DAA21C;
    color: #1E293B;
    padding: 10px;

  }

  .wrapper {
      display: grid;
      grid-template-columns: 50% 50%;
      width: 70%;
      margin: 0 auto;
    }

  .promo-pic {
    width: 500px;
    height: auto;
    margin-bottom: 40px;
  }

  .big-text {
    font-size: xx-large;
    font-weight: bolder;
    color: #1E293B;
  }

  .large-text {
    font-size: larger;
  }

  .spinner-container {
    left: 50%;
    top: 50%;
    position: absolute;
    transform: translate(-50%, -50%);
  }

  .spinner {
    border: 6px solid #DAA21C;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    border-top-color: #DFF1FF;
    animation: spin 1s infinite ease-in-out;
  }

  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
</style>
