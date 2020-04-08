<template>
  <v-container class="mt-5" fill-height>
    <Map :restaurants="this.list" :user="this.multicampus"/>
    <!-- <v-card-text class="text-center">
      <p class="display-2 pa-5">테스트도 식후경</p>
      <p class="display-3 pa-2">🍱🍜🥡</p>
      <p class="display-3 pa-2">🍰🍔</p>
    </v-card-text> -->
  </v-container>
</template>

<script>
import Map from "@/components/Map";
import { mapState, mapActions } from "vuex";
export default {
  components: {
    Map,
  },
  data () {
    return {
      multicampus: {
        lat: 37.50128969810118,
        lng: 127.03960183847694,
      },
      list: [
          {
              title: '새마을식당 역삼GS점',
              lat: 37.5029438450506,
              lng: 127.03713443439975,
          },
          {
              title: '아리네술상', 
              lat: 37.50255638865731,
              lng: 127.03721058059857,
          },
          {
              title: '바나프레소 테헤란로점', 
              lat: 37.50112544622184,
              lng: 127.03905608614859,
          },
      ],
    }
  },
  computed: {
   
  },
  methods: {
    
  },
}
</script>