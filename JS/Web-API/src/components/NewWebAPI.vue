<template>
  <img src="../assets/logo.png" alt="Vue logo" id="logo" />
  <div id="new-api">
    <button @click="fullScreen">fullScreen</button>
    <hr />
    <input v-model="copy" />
    <button @click="performCopy" id="copy">copy</button>
    <br />
    <input type="text" disabled v-model="paste" />
    <button @click="performPaste">paste</button>
    <hr />
    <!-- <el-slider v-model="slider"></el-slider> -->
    <input type="range"  v-model="slider" name="points" min="0" max="100" /> slider(0~100):
    <div :style="{ width: slider + 'px' }" id="resizeDom"> {{ slider }} </div>
    <hr />
    imageCapture
    <hr />
    broadcastChannel
    <button @click="send">send</button>
    <hr />
    <button @click="vibrate">vibrate</button>
  </div>
</template>

<script>
import { defineComponent } from "vue"
export default defineComponent({
  name: 'NewWebAPI',
  methods: {
    fullScreen() {
      document.getElementById('logo').requestFullscreen({ options: { navigationUI: 'false' } })
    },
    async performCopy(event) {
      event.preventDefault()
      try {
        await navigator.clipboard.writeText(this.copy) // 将copy的值写入剪贴板
        console.log(`${this.copy} copied to clipboard`)
      } catch (err) {
        console.error('Failed to copy: ', err)
      }
    },
    async performPaste(event) {
      event.preventDefault()
      try {
        const text = await navigator.clipboard.readText() // 从剪贴板读取上一次复制的值
        this.paste = text
        console.log('Pasted content: ', text)
      } catch (err) {
        console.error('Failed to read clipboard contents: ', err)
      }
    },
    send() {
      const CHANNEL_NAME = 'greenroots_channel'
      const bc = new BroadcastChannel(CHANNEL_NAME)
      const message = 'I am wonderful!'
      bc.postMessage(message)
    },
    vibrate() {
      // 无效
      navigator.vibrate(20000)
    },
  },
  mounted: function () {
    const resizeDom = document.getElementById('resizeDom')
    const resizeObserver = new ResizeObserver((entries) => {
      console.log('entries', entries)
      for (const entry of entries) {
        // Get the button element and color it
        // based on the range values like this,
        entry.target.style.color = 'blue'
      }
    })
    resizeObserver.observe(resizeDom)
    const CHANNEL_NAME = 'greenroots_channel'
    const bc = new BroadcastChannel(CHANNEL_NAME)
    bc.addEventListener('message', function (event) {
      console.log('event', event)
      console.log(`Received message, "${event.data}", on the channel, "${CHANNEL_NAME}"`)
    })
    console.log('performance.memory', performance.memory)
    console.log('navigator.connection', navigator.connection)
    const [entry] = performance.getEntriesByType('navigation')
    console.table(entry)
    navigator.getBattery().then(function (battery) {
      // handle the charging change event
      battery.addEventListener('chargingchange', function () {
        console.log('Battery charging? ' + (battery.charging ? 'Yes' : 'No'))
      })
      // handle charge level change
      battery.addEventListener('levelchange', function () {
        console.log('Battery level: ' + battery.level * 100 + '%')
      })
      // handle charging time change
      battery.addEventListener('chargingtimechange', function () {
        console.log('Battery charging time: ' + battery.chargingTime + ' seconds')
      })
      // handle discharging time change
      battery.addEventListener('dischargingtimechange', function () {
        console.log('Battery discharging time: ' + battery.dischargingTime + ' seconds')
      })
    })
  },
});
</script>

<script setup>
import { ref } from 'vue'

const slider = ref(30),
      copy  = ref(''),
      paste = ref('')
</script>

<style scoped>
a {
  color: #42b983;
}
#resizeDom {
  display: inline-block;
  text-align: center;
  margin: 0 auto;
  background-color: orangered;
  white-space: nowrap;
}
</style>
