<template>
  <div class="row px-1">
    <Card
      v-for="store in stores"
      :key="store.id"
      :store="store"
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
    stores: {
      type: Array,
      default: function(){
          return []
      },
    }
  },
  computed: {

  }
};
</script>

<style scoped>
</style>



