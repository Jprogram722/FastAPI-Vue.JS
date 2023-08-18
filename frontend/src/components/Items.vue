<template>
    <div class="grid-container">
      <div class="grid-item" v-for="product in props.products">
        <img v-bind:src="product.img_path" alt="No Image Found">
        <p class="product-name">{{ product.name }}</p>
        <p class="product-id">Product number: #{{ product.id }}</p>
        <p class="product-catagory">category: {{ product.category_name }}</p>
        <p class="product-price">${{ product.price }}</p>
        <p class="product-stock">{{ product.stock }} left in stock</p>
      </div>
    </div>
</template>

<script>
export default {
    name: 'Items Component',
    props: ['products'],
    setup (props, context) {
        return {props}
    }
}
</script>

<style>
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
</style>