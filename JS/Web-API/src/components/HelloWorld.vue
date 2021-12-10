<template>
  <h1>{{ msg }}</h1>
  <video controls id="video" width="576" height="324">
    <source :src="videoSrc" />
  </video>
  <br>
  <button type="button" @click="count++">count is: {{ count }}</button>
  <p>
    Edit
    <code>components/NewWebAPI.vue</code> to test hot module replacement.
  </p>
</template>

<script setup>
import { ref } from 'vue'

defineProps({ msg: String })

const count = ref(0),
      videoSrc = ref('https://cloud.video.taobao.com/play/u/2780279213/p/1/e/6/t/1/d/ld/36255062.mp4')
</script>