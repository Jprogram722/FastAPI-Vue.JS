<template>
  <div>
    <Items :products="products"/>
    <Form @submitForm="handleSubmit"/>
    <UpForm @submitUpdate="handleUpdate"/>
    <DelForm @submitDelete="handleDelete"/>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import Form from '../components/form.vue';
import DelForm from '../components/DelForm.vue';
import Items from '../components/Items.vue';
import UpForm from '../components/UpForm.vue';

export default{
  name: 'main app',
  components: { Form, DelForm, Items, UpForm },
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

    /**
    * Sends a request to the api to update an item in the database
    * @param {ObjectLiteral} formInfo the info contained in the form
    */
    const handleUpdate = async (formInfo) => {
      try{
        console.log(formInfo);
        await axios.patch(defaultURL+ '/update/' + formInfo.id, formInfo);
        window.location.reload();
      }
      catch(err){
        console.log(err.message);
      }
    }

    return {handleSubmit, handleDelete, handleUpdate, products}
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
    justify-content: space-between;
    padding: 10px;
    gap: 40rem;
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
    color: #DFF1FF;
    padding: 10px;
    cursor: pointer;
    background-color: #475569;
    border: none;
    border-radius: 10px;
    font-size: larger;
  }

  .btn:hover{
    background-color: #334155;
  }

  .purchase-btn{
    width: 250px;
  }
</style>
