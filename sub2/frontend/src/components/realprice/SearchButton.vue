<template>
  <v-container>
    <v-card class="mx-auto" max-width="500">
      <v-card-text class="text-center">
        <v-slider v-model="RealPrice.taste" min="0" max="5" label="맛" thumb-label />
        <v-slider v-model="RealPrice.distance" min="0" max="5" label="거리" thumb-label />
        <v-slider v-model="RealPrice.price" min="0" max="5" label="가격" thumb-label />
        <v-btn large color="blue lighten-1 white--text ma-5" rounded @click="Search">검색하기</v-btn>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data(){
    return{
    //   RealPrice: {
    //     taste: 0,
    //     distance: 0,
    //     price: 0
    // }
    }
  },
  computed: {
    RealPrice: function() {
      return this.$store.getters["data/RealPrice"];
    }
  },
  methods: {
    ...mapActions("data", ["postQuestion"]),
    Search: function() {
      const params = {
        "curLatitude":"37.503652",
        "curLongitude":"127.038125",
        "maxDistance":"0.2",
        "minPoint":"4",
        "maxPrice":"15000",
        "foodfilter":""
      };
      this.postQuestion(params);
    },
  }
};
</script>