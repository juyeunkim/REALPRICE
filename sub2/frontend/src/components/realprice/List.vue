<template>
  <v-container
    id="scroll-target" class="mt-5 overflow-y-auto" >
    <!-- <h3>검색결과로 나온 결과값 - 검색결과에따라 다르게 보여줄 예정</h3>
    맛 : {{ RealPrice.taste }} <br>
    거리 : {{ RealPrice.distance }} <br>
    가격 : {{ RealPrice.price }} <br> -->
    <v-flex v-for="store in restaurants" :key="store.id">
      <store-list-card
        :store="store"
        @clickItem="selectItem(store.id)"
      />
    </v-flex>
  </v-container>
</template>

<script>
import StoreListCard from "@/components/realprice/StoreListCard";
// import { mapState, mapActions } from "vuex";
export default {
  components: {
    StoreListCard
  },
  props: {
      restaurants: {
          type: Array,
          default: function(){
              return []
          },
      },
  },
  methods: {
    selectItem: function(id){
      // console.log(id);
      this.$emit('clickItem', id);
    },
  }
}
</script>

<style lang="scss" scoped>
#scroll-target {
  max-height: 90vh;
}
</style>