<template>
  <div class="row px-1">
    <Card
      v-for="store in stores"
      :key="store.id"
      :srcUrl="store.srcUrl"
      :storeName="store.storeName"
      :price="store.price"
    />
  </div>
</template>

<script>
import Card from "./Card.vue";

export default {
  name: "CardPages",
  components: {
    Card
  },
  props: {
    stores: Array
  }
};
</script>

<style scoped>
</style>



