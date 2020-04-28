<template>
  <div class="row px-1">
    <Card
      v-for="store in stores"
      :key="store.id"
      :store="store"
      @clickItem="selectItem"
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
  methods: {
    selectItem(id) {
      this.$emit("clickItem", id);
    }
  }
};
</script>

<style lang="scss" scoped>
.row{
  margin-left: 1vw;
  margin-right: 1vw;
  @media screen and (max-width: 600px) {
    margin-left: 0.5vw;
    margin-right: 0.5vw;
  }
}
</style>



