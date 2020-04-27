<template>
<!-- 메인 컬러 블루 #0F4C82 -->
  <v-container class="mt-5 mainColor" fill-height>
    <v-card-text class="text-center">
      <p class="display-3 pa-2">💸💵💰</p>
      <!-- <p class="display-2 pa-5">REAL PRICE</p> -->
      <img class="logo" src="../assets/logo_white.png">
      <p class="display-2 pa-5">REAL PRICE</p>
      <v-btn color="primary" @click="test">State값 확인</v-btn>
    </v-card-text>
  </v-container>
</template>

<style scoped>
.mainColor {
  background-color: #0F4C82
}
.logo {
  width: 300px;
}
</style>

<script>
import { Component, Vue } from 'vue-property-decorator';
export default {
  methods:{
    test(){
      console.log(this.$store.state)
    },
    // fclick(){
    // alert('Hello @lbzui/vue!');
    // }
  }
};
</script>