<template>
  <header>
    <div class="navbar">
      <h1>Ecommerce Mockup Website</h1>
      <ul>
        <li><a href="#">About</a></li>
      </ul>
    </div>
  </header>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style>
  .navbar{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 65rem;
}

</style>
