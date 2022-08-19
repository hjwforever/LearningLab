<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import { ref, defineAsyncComponent } from 'vue'
// import HelloWorld from './components/HelloWorld.vue'
// import AzCalculator from 'az-ui-calculator'
// const Calculator = defineAsyncComponent(() => import('./components/Calculator.vue'))
const YamlEditor = defineAsyncComponent(() => import('./components/YamlEditor/index.vue'))

const value = ref(0)
</script>

<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png" /> -->
  <!-- <HelloWorld msg="Hello Vue 3 + Vite" /> -->
  <!-- <AzCalculator /> -->
  <!-- <Calculator style="right: 0; bottom: 0" /> -->
  <YamlEditor />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
