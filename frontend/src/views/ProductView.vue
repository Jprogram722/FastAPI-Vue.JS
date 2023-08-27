<template>
    <Modal :modalToggle="modalToggle" @close-modal="toggleModal">
        <UpForm @submitUpdate="handleUpdate"/>
    </Modal>
    <Navbar/>
    <div class="wrapper" v-if="product">
        <div>
            <img class="product-img" :src="product.img_path" alt="No Image Found">
        </div>
        <div class="product-details">
            <button class="edit-btn" @click="toggleModal"><i class="fa-solid fa-pencil"></i></button>
            <h1 class="product-name">{{ product.name }}</h1>
            <p class="product-number">Product #: {{ product.id }}</p>
            <h1 class="product-price">${{ product.price }}</h1>
            <p class="product-category">Category: {{ product.category_name }}</p>
            <p class="product-category">Overview: {{ product.description }}</p>
            <p v-if="product.stock > 0"><i class="fa-solid fa-check check"></i> Avalible In Store</p>
            <p v-else><i class="fa-solid fa-x" style="color: #d73737;"></i> Not in Stock</p>
            <button class="btn" @click.left="productInCart(product.stock)">Add To Cart</button>
        </div>
    </div>
    <div v-else>
        <Spinner/>
    </div>
</template>

<script>
import { onMounted, ref } from 'vue';
import axios from 'axios';
import Navbar from '../components/Navbar.vue';
import UpForm from '../components/UpForm.vue';
import Modal from '../components/Modal.vue';
import Spinner from '../components/Spinner.vue';

export default {
    name: "Product View",
    components: { Navbar, UpForm, Modal, Spinner, Spinner },
    props: ['id'],
    setup(props, context) {
        const defaultURL = 'http://localhost:8000/api';
        const product = ref('');
        const modalToggle = ref(false);


        onMounted(async () => {
            const { data } = await axios.get(defaultURL + '/get_one/' + props.id);
            product.value = data;
            console.log(product.value.stock)
        });

        const toggleModal = () => {
            modalToggle.value = !modalToggle.value;
        }

        /**
        * Sends a request to the api to update an item in the database
        * @param {ObjectLiteral} formInfo the info contained in the form
        */
        const handleUpdate = async (formInfo) => {
            try{
                console.log(formInfo);
                await axios.patch(defaultURL+ '/update/' + props.id, formInfo);
                window.location.reload();
            }
            catch(err){
                console.log(err.message);
            }
        }

        const productInCart = async (product_stock) => {
            try {
                console.log("Bought");
                await axios.patch(defaultURL + '/update/' + props.id, {stock: product_stock - 1});
                window.location.reload();
            }
            catch(err){
                console.log(err.message);
            }
        }


        return { product, handleUpdate, toggleModal, modalToggle, productInCart };
    },
}
</script>

<style>
    .wrapper{
        padding-top: 35px;
        display: grid;
        grid-template-columns: 50% 50%;
        width: 70%;
        margin: 0 auto;
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

    .product-details {
        background-color: #334155;
        padding: 30px;
        border: none;
        border-radius: 10px;
    }

    .edit-btn {
        padding: 5px 7px 5px 7px;
        float: right;
        cursor: pointer;
        font-size: larger;
        color: #DFF1FF;
        background-color: #334155;
        border-radius: 100%;
        border: none;
        transition: all 75ms;
    }

    .edit-btn:hover {
        color: #334155;
        background-color: #DFF1FF;
    }
</style>