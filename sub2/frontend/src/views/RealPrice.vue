<template>
  <v-container class="mt-5" fill-height>
    <v-layout column>
      <v-flex>
        <v-card class="text-center">
          <p class="display-3 pa-2">💸💵💰</p>
          <p class="display-2 pa-5">REAL PRICE</p>
          <SEARCH />
        </v-card>
      </v-flex>
      <v-flex>
        <v-layout row>
          <v-flex xs8>
            <Map :restaurants="this.RealPrice" :user="this.multicampus"/>
          </v-flex>
          <v-flex xs4>
            <LIST :restaurants="this.RealPrice"/>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import SEARCH from "@/components/realprice/SearchButton";
import LIST from "@/components/realprice/List";
import Map from "@/components/Map";
import { mapState, mapActions, mapMutations } from "vuex";

export default {
  components: {
    SEARCH,
    LIST,
    Map
  },
  data() {
    return {
      param: {
        "curLatitude":"37.503652",
        "curLongitude":"127.038125",
        "maxDistance":"0.2",
        "minPoint":"4",
        "maxPrice":"15000",
        "foodfilter":""
      },
      multicampus: {
        latitude: 37.50128969810118,
        longitude: 127.03960183847694,
      },
      list: [
          {
              title: '새마을식당 역삼GS점',
              lat: 37.5029438450506,
              lng: 127.03713443439975,
          },
          // {
          //     title: '아리네술상', 
          //     lat: 37.50255638865731,
          //     lng: 127.03721058059857,
          // },
          // {
          //     title: '바나프레소 테헤란로점', 
          //     lat: 37.50112544622184,
          //     lng: 127.03905608614859,
          // },
      ],
    }
  },
  destroyed() {
      this.clearRealPrice();
  },
  computed: {
    RealPrice: function() {
      return this.$store.getters["data/RealPrice"];
    }
  },
  methods:{
    ...mapMutations("data", ["clearRealPrice"]),
    search(){
      console.log(realPrice)
    }
  },
};
</script>