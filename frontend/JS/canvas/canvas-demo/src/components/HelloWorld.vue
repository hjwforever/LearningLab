<script setup>
  import {ref, onMounted, reactive} from 'vue'
  const canvas = ref(null);
  const image = ref(new Image());
  const offscreen = ref(null);
  const offCtx = ref(null);
  const ctx = ref(null);
  const rect = reactive({w:200,h:50,x:100,y:100});
  image.value.onload = async () => {
    // let offsreen = new OffscreenCanvas(image.value.width, image.value.height);
    // let offCtx = offsreen.getContext('2d');
    // offCtx.drawImage(image.value, 0, 0);
    // console.log('offCtx', offCtx)
  };
  image.value.src = 'https://cn.vitejs.dev/logo.svg';
  onMounted(() => {
    offscreen.value = new OffscreenCanvas(1000, 1000);
    offCtx.value = offscreen.value.getContext('2d');
    console.log('image.value.width, image.value.height',image.value.width, image.value.height)
    offCtx.value.drawImage(
        image.value,
        0,
        0
      );

    ctx.value = canvas.value.getContext('2d');
    ctx.value.drawImage(
        offscreen.value,
        400,
        400
      );
  })
  const rotate = (degree) => {
      if (degree < 0) {
        offCtx.translate(0, this.bitMap.width);
        offCtx.rotate((-90 * Math.PI) / 180);
        [this.imagePosition.width, this.imagePosition.height] = [
          this.imagePosition.height,
          this.imagePosition.width
        ];
      } else if (degree > 0) {
        offCtx.translate(this.bitMap.height, 0);
        offCtx.rotate((90 * Math.PI) / 180);
        [this.imagePosition.width, this.imagePosition.height] = [
          this.imagePosition.height,
          this.imagePosition.width
        ];
      }
      offCtx.drawImage(this.bitMap, 0, 0);
      this.bitMap.close();
      this.bitMap = offsreen.transferToImageBitmap();
      console.log('bitMap', this.bitMap);
      this.drawImage();
    }
  const rotateTest = () => {
    offCtx.value.save();
    offCtx.value.clearRect(0, 0, offscreen.value.width, offscreen.value.height);
    console.log('offscreen.value.width / 2, offscreen.value.height / 2',offscreen.value.width / 2, offscreen.value.height / 2)
        offCtx.value.drawImage(
      image.value,
      0,
      0
    );
    offCtx.value.translate( image.value.width / 2, image.value.height / 2);
    offCtx.value.rotate(30 * Math.PI / 180);
    offCtx.value.translate(-image.value.width / 2, -image.value.height / 2);
    // offCtx.value.restore();

    ctx.value.clearRect(0, 0, canvas.value.width, canvas.value.height);
    ctx.value.drawImage(
      offscreen.value,
      400,
      400
    );
  }
</script>
<template>
  <button @click="rotateTest">rotateTest</button>
  <canvas ref="canvas" width="1000" height="1000"></canvas>
</template>

<style scoped>
a {
  color: #42b983;
}
</style>
