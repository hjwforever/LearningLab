<template>
  <div class="home">
    <TimePicker />
  </div>
</template>

<script>
  import TimePicker from '@/components/TimePicker';

  export default {
    name: 'Home',
    components: {
      TimePicker,
    },
  };
</script>
