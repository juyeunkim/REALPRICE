<template>
  <v-container class="mt-5" fill-height>
    <v-layout column>
      <v-flex>
        <v-card class="text-center">
          <p class="display-3 pa-2">💸💵💰</p>
          <p class="display-2 pa-5">REAL PRICE</p>
          <SEARCHFORM @search="searchSubmit"/>
        </v-card>
      </v-flex>
      <v-flex>
        <v-dialog
          v-model="dialog"
          persistent
          max-width="700"
        >
          <STOREDETAIL :store="selectedStore" @close="closeDetail" />
        </v-dialog>
        <v-layout row>
          <v-flex xs8>
            <div v-if="center !== null">{{center.getLat()}}</div>
            <div v-if="center !== null">{{center.getLng()}}</div>
            <div>{{radius}}</div>
            <Map :restaurants="RealPriceList" :user="userLocation" @clickItem="selectItem" @drawCircle="selectCircle"/>
          </v-flex>
          <v-flex xs4>
            <LIST :restaurants="RealPriceList" @clickItem="selectItem" />
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import STOREDETAIL from '@/components/realprice/StoreDetail';
import SEARCHFORM from "@/components/realprice/SearchForm";
import LIST from "@/components/realprice/List";
import Map from "@/components/Map";
import { mapState, mapActions, mapMutations } from "vuex";

export default {
  components: {
    STOREDETAIL,
    SEARCHFORM,
    LIST,
    Map
  },
  data() {
    return {
      selectedStore: null,
      dialog: false,
      geoLocation: {
        latitude: 37.50128969810118,
        longitude: 127.03960183847694,
      },
      center: null,
      radius: 0,
    }
  },
  computed: {
    ...mapState({
      RealPriceList: state => state.data.realPriceList,
    }),
    userLocation() {
        return this.geoLocation;
    },
  },
  mounted() {
    this.getLocation();
  },
  destroyed() {
      this.clearRealPrice();
  },
  methods:{
    ...mapActions("data", ["postRealPrice"]),
    ...mapMutations("data", ["clearRealPrice"]),
    selectItem: function(id){
      this.RealPriceList.forEach(el => {
        if(el.id == id){
          this.selectedStore = el;
        }
      });
      this.dialog = true;
    },
    getReviews: function(){
      consol.log('!!!')
      this.$store.dispatch("data/getReviews", this.selectedStore.id);
    },
    closeDetail: function(){
      console.log("closeDetail");
      this.dialog = false;
      // this.selectedStore = null;
    },
    selectCircle: function(c, r){
      // console.log("drawCircle");
      // console.log(c);
      this.center = c;
      this.radius = r;
    },
    getLocation: function() {
      const vm = this;
      if (navigator.geolocation) { // GPS를 지원하면
        navigator.geolocation.getCurrentPosition(function(position) {
          // alert(position.coords.latitude + ' ' + position.coords.longitude);
          vm.geoLocation.latitude = position.coords.latitude;
          vm.geoLocation.longitude = position.coords.longitude;
        }, function(error) {
          console.error(error);
        }, {
          enableHighAccuracy: false,
          maximumAge: 0,
          timeout: Infinity
        });
      } else {
        console.log('GPS를 지원하지 않습니다');
      }
    },
    searchSubmit: function(inputPrice) {
      const vm = this;
      this.postRealPrice({
          "price": parseInt(inputPrice), 
          "ulatitude": parseFloat(vm.geoLocation.latitude),
          "ulongitude": parseFloat(vm.geoLocation.longitude),
          "mlatitude": parseFloat(vm.center.Ha), 
          "mlongitude": parseFloat(vm.center.Ga)
      });
      
    }
  },
};
</script>