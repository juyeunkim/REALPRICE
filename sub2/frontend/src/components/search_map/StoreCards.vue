<template>
  <div>
    <StoreCard v-for="store in stores" :key="store.id" :store="store" />
  </div>
</template>

<script>
import StoreCard from "./StoreCard.vue";

export default {
  name: "StoreCards",
  components: {
    StoreCard
  },
  props: {
    stores: {
      type: Array,
      default: () => new Object()
    }
  }
};
</script>


