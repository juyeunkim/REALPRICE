<template>
  <v-container class="mt-5">
    <v-card class="mx-auto" max-width="500">
      <v-card-text class="text-center">
        <p class="display-3 pa-2">💸💵💰</p>
        <p class="display-2 pa-5">REAL PRICE</p>// 현재위치 표시
        <v-slider v-model="RealPrice.taste" min="0" max="5" label="맛" thumb-label />
        <v-slider v-model="RealPrice.distance" min="0" max="5" label="거리" thumb-label />
        <v-slider v-model="RealPrice.price" min="0" max="5" label="가격" thumb-label />
        <v-btn large color="blue lighten-1 white--text ma-5" rounded @click="search">검색하기</v-btn>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  data: () => ({}),
  computed: {
    RealPrice: function() {
      return this.$store.getters["data/RealPrice"];
    }
  },
  methods: {
    search() {
      // 일단 home 으로 이동
      this.$router.push("/");
    }
  }
};
</script>