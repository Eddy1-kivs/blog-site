<template>
  <div
    class="px-2 bg-[#fde7be] py-2 min-h-screen press-start-text text-gray-900 md:px-20"
  >
    <slot></slot>
  </div>
</template>
<script setup>
definePageMeta({
  layout: "font-layout",
});
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");

.press-start-text {
  font-family: "Press Start 2P";
}
</style>
