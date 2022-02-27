<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import NewWebAPI from './components/NewWebAPI.vue'
import Drag from './components/Drag.vue'
</script>

<template>
  <NewWebAPI msg="Hello Vue 3 + Vite" />
  <Drag />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #332c50;
  margin-top: 60px;
}
</style>
