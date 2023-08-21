<template>
    <div class="wrapper">
        <div>
            <img class="product-img" :src="product.img_path" alt="No Image Found">
        </div>
        <div>
            <h1 class="product-name">{{ product.name }}</h1>
            <h1 class="product-price">${{ product.price }}</h1>
            <p class="product-category">Category: {{ product.category_name }}</p>
            <p class="product-category">Overview: {{ product.description }}</p>
            <p v-if="product.stock > 0"><i class="fa-solid fa-check check"></i> Avalible In Store</p>
            <button class="btn">Add To Cart</button>
        </div>
    </div>
</template>

<script>
import { onMounted, ref } from 'vue';
import axios from 'axios';

export default {
    name: "Product View",
    props: ['id'],
    setup (props, context) {

        const defaultURL = 'http://localhost:8000/api';

        const product = ref('');

        onMounted(async () => {
            const {data} = await axios.get(defaultURL + '/get_one/' + props.id);
            product.value = data;
        })

        return {product}
    }
}
</script>

<style>
    .wrapper{
        padding-top: 35px;
        width: 80%;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 60% 40%;
    }

    .product-img{
        width: 600px;
        height: auto;
    }

    .product-price{
        font-size: larger;
        font-weight: bolder;
    }

    .check{
        color: #4ade80;
    }
</style>