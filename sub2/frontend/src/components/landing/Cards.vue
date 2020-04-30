<template>
  <div class="row px-1">
    <Card
      v-for="store in stores"
      :key="store.id"
      :store="store"
      @clickItem="selectItem"
    />
    <div class="emptyText" v-if="isSearched && !(this.stores.length > 0)">
      <!-- <img class="no-result" alt="logo" src="@/assets/crying.png"> -->
      <p class="no-result-font">😱해당 금액으로 먹을 수 있는 메뉴가 없습니다.</p>
    </div>
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
      }
    },
    isSearched: {
      type: Boolean,
      default: false,
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
  text-align: center;
  margin-left: calc(4vw - 20px);
  // margin-right: calc(5vw - 20px);
  // margin-left: calc(5vw - 4px);
  // margin-right: calc(5vw - 4px);
  @media screen and (max-width: 600px) {
    margin: auto;
  }
}
.no-result-font{
  color: white;
  font-size:2vw;
}
.emptyText{
  margin: auto;
  text-align: center;
}
</style>



