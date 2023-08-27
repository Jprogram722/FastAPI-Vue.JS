<template>
    <Navbar/>
    <div class="err-container">
        <i class="fas fa-exclamation-triangle err-symbol" style="color: #c41c1c;"></i>
        <h1 class="err-msg">Error 404: Page Not Found</h1>
    </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';

export default {
    name: 'NotFound View',
    components: {Navbar},
    setup () {
        

        return {}
    }
}
</script>

<style>
    .err-container{
        display: grid;
        margin: 100px auto;
        width: 400px;
    }

    .err-symbol {
        margin: 0 auto;
        width: 50%;
        font-size: 200px;
    }

  .err-msg {
    font-size: x-larger;
    font-weight: bold;
  }
</style>