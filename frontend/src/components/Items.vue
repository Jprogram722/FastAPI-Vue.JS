<template>
    <div class="grid-container">
      <div class="grid-item" v-for="product in props.products">
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
import { RouterLink } from 'vue-router';

export default {
    name: 'Items Component',
    props: ['products'],
    setup (props, context) {
        return {props}
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
    border: 2px solid #DFF1FF;
    border-radius: 10px;
    background-color: #1e293b;
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

  .product-name{
    font-size: large;
    font-weight: bold;
    width: 250px;
  }
  
  .product-name:hover{
    width: 250px;
    background-color: #334155;
  }

  .check{
    color: #4ade80;
  }
</style>