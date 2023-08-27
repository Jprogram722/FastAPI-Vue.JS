<template>
    <div class="spinner-container">
        <div class="spinner"></div>
        <p>Now Loading...</p>
    </div>
</template>

<script>
export default {
    setup () {
        

        return {}
    }
}
</script>

<style scoped>
    .spinner-container {
    left: 50%;
    top: 50%;
    position: absolute;
    transform: translate(-50%, -50%);
  }

  .spinner {
    margin: 0 auto;
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