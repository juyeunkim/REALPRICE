<template>
  <v-container class="mt-5" fill-height>
    <v-card-tile class="text-center" max-width="344">
      <p class="display-3 pa-2">💸💵💰</p>
      <p class="display-2 pa-5">REAL PRICE</p>
      // 현재위치 표시 
      <v-slider v-model="taste" min="0" max="5" label="맛　" thumb-label />
      <v-slider v-model="distance" min="0" max="5" label="거리" thumb-label />
      <v-slider v-model="price" min="0" max="5" label="가격" thumb-label />
      <v-btn large color="blue lighten-1 white--text ma-5" rounded to="/search">검색하기</v-btn>
    </v-card-tile>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    taste: 50,
    distance: 50,
    price: 50
  })
};
</script>