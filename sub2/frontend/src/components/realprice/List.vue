<template>
  <v-container class="mt-5">
    ////// 검색결과로 나온 결과값 <br>
    맛 : {{ RealPrice.taste }} <br>
    거리 : {{ RealPrice.distance }} <br>
    가격 : {{ RealPrice.price }} <br>
  </v-container>
</template>

<script>
export default {
    computed: {
    RealPrice: function() {
      return this.$store.getters["data/RealPrice"];
    }
  },
}
</script>

<style>

</style>