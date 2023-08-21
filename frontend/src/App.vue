<template>
  <header>
    <div class="navbar">
      <h1>Fast API test with vue JS</h1>
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

</style>
