<template>
    <div class="grid-container">
      <div class="grid-item" v-for="product in props.products">
        <button class="del-btn" @click.left="deleteProduct(product.id)"><i class="fa-solid fa-x"></i></button>
        <img v-bind:src="product.img_path" alt="No Image Found">
        <RouterLink :to="{name: 'product', params: {id: product.id}}"><p class="product-name">{{ product.name }}</p></RouterLink>
        <p class="product-id">Product number: #{{ product.id }}</p>
        <p class="product-catagory">category: {{ product.category_name }}</p>
        <p class="product-price">${{ product.price }}</p>
        <p v-if="product.stock > 0"><i class="fa-solid fa-check check"></i> Avalible In Store</p>
        <p v-else><i class="fa-solid fa-x" style="color: #d73737;"></i> Not in Stock</p>
      </div>
    </div>
</template>

<script>
import axios from 'axios';
import { RouterLink } from 'vue-router';

export default {
    name: 'Items Component',
    props: ['products'],
    setup (props, context) {

      const deleteProduct = async (product_id) => {
          context.emit('deleteProduct', {id: product_id});
      }

      return {props, deleteProduct}
    }
}
</script>

<style scoped>
    .grid-container{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    padding: 10px;
    grid-gap: 50px;
    margin: 20px 200px;
  }

  .grid-item{
    background-color: #334155;
    border-radius: 10px;
    padding: 15px;
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

  .product-name{
    text-align: center;
    font-size: large;
    font-weight: bold;
    width: 250px;
    transition: all 75ms;
  }
  
  .product-name:hover{
    width: 250px;
    background-color: #1e293b;
    border-radius: 10px;
  }

  .check{
    color: #4ade80;
  }

  .del-btn {
    cursor: pointer;
    float: right;
    padding: 5px 9px 5px 9px;
    margin-bottom: 10px;
    color: #d73737;
    background-color: #334155;
    border: none;
    border-radius: 50px;
    transition: all 75ms;
  }

  .del-btn:hover {
    background-color: #d73737;
    color: #334155;
  }
</style>