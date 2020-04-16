<template>
  <v-container class="mt-5">
    <!-- <h3>검색결과로 나온 결과값 - 검색결과에따라 다르게 보여줄 예정</h3>
    맛 : {{ RealPrice.taste }} <br>
    거리 : {{ RealPrice.distance }} <br>
    가격 : {{ RealPrice.price }} <br> -->
    <v-flex v-for="store in stores" :key="store.id">
      <store-list-card
        :id="store.id"
        :name="store.name"
        :categories="store.categories"
        :address="store.address"
        :tel="store.tel"
      />
    </v-flex>
  </v-container>
</template>

<script>
import StoreListCard from "@/components/StoreListCard";
export default {
  components: {
    StoreListCard
  },
  data() {
    return {
      stores: [
        {
          id: "id1",
          name: "식당1",
          categories: ["식당1의 카테고리1","식당1의 카테고리2"],
          address: "식당1의 주소",
          tel: "식당1의 전화번호",
        },
        {
          id: "id2",
          name: "식당2",
          categories: ["식당2의 카테고리1","식당2의 카테고리2"],
          address: "식당2의 주소",
          tel: "식당2의 전화번호",
        },
        {
          id: "id3",
          name: "식당3",
          categories: ["식당3의 카테고리1","식당3의 카테고리2"],
          address: "식당3의 주소",
          tel: "식당3의 전화번호",
        }
      ]
    }
  },
  computed: {
    RealPrice: function() {
      return this.$store.getters["data/RealPrice"];
    }
  },
}
</script>

<style>

</style>