<template>
  <div class="app">
    <img class="search-logo" alt="logo" src="@/assets/logo_blue.png">

    <!-- 가격 입력창 -->
    <input
      v-model="inputPrice"
      class="form-control size-20per"
      type="text"
      placeholder="가격을 찾아보세요."
      aria-label="Search"
      @keyup.enter="searchSubmit"
    >
    <v-dialog
      v-model="dialog"
      max-width="700"
    >
      <STOREDETAIL :store="selectedStore" @close="closeDetail" />
    </v-dialog>

    <!-- 태그창 -->
    <div>
      <mdb-badge v-for="tag in tagList" :key="tag.id" pill color="blue">{{tag.name}}</mdb-badge>
    </div>

    <!-- 지도창 -->
    <div class="map-frame">
      <div class="map-col1">
        <Map :restaurants="RealPriceList" :user="geoLocation" :map="center" :zoom="zoom" @clickItem="selectItem" @drawCircle="selectCircle"/>
      </div>
      <div class="map-col2 scrollbar scrollbar-blue bordered-blue">
        <StoreCards :stores="RealPriceList" @clickItem="selectItem"/>
        <!-- <StoreCard v-for="store in RealPriceList" :key="store.id" :store="store" @clickItem="selectItem" /> -->
      </div>
      
    </div>

    <img class="marker" src="@/assets/marker.png">
  </div>
</template>

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=eac48c3548025ce4e0b61b1512b4282c"></script>

<script>
import STOREDETAIL from '@/components/realprice/StoreDetail';
import StoreCards from '@/components/search_map/StoreCards.vue'
import StoreCard from "@/components/search_map/StoreCard.vue";
import Map from "@/components/Map.vue";
import api from '@/api/index.js'
import { mapState, mapActions, mapMutations } from "vuex";
import { mdbBadge } from 'mdbvue';

export default {
  name: "Landing",
  components: {
    STOREDETAIL,
    StoreCards,
    StoreCard,
    Map,
    mdbBadge
  },
  data() {
    return {
      inputPrice: 5000,
      selectedStore: null,
      dialog: false,
      geoLocation: {
        latitude: 0,
        longitude: 0,
      },
      center: {
        Ha: 0,
        Ga: 0,
      },
      radius: 0,
      zoom: 0,
    }
  },
  computed: {
    ...mapState({
      RealPriceList: state => state.data.realPriceList.stores,
      tagList: state => state.data.realPriceList.tags,
    }),
    userLocation() {
        return this.geoLocation;
    },
  },
  mounted() {
    this.getLocation();
  },
  destroyed() {
      // this.clearRealPrice();
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
    selectCircle: function(center, radius, level, str){
      // console.log("drawCircle");
      
      this.center.Ha = center.getLat();
      this.center.Ga = center.getLng();
      this.radius = radius;
      this.zoom = level;
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
          vm.geoLocation.latitude = 37.50128969810118;
          vm.geoLocation.longitude = 127.03960183847694;
        }, {
          enableHighAccuracy: false,
          maximumAge: 0,
          timeout: Infinity
        });
      } else {
        console.log('GPS를 지원하지 않습니다');
        vm.geoLocation.latitude = 37.50128969810118;
        vm.geoLocation.longitude = 127.03960183847694;
      }
    },
    searchSubmit: function() {
      const vm = this;
      this.postRealPrice({
          "price": parseInt(vm.inputPrice), 
          "ulatitude": parseFloat(vm.geoLocation.latitude),
          "ulongitude": parseFloat(vm.geoLocation.longitude),
          "mlatitude": parseFloat(vm.center.Ha), 
          "mlongitude": parseFloat(vm.center.Ga),
          "radius":parseFloat(vm.radius)
      });
      
    }
  },
}
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap");

.app {
  background-color: white;
}

.search-logo {
  width: 120px;
  display: flex;
  margin-top: 10px;
  margin-left: 10px;
  /* margin: auto; */
}

.marker {
  width: 50px;
  position: absolute;
  bottom: 10px;
  right: 10px;
  /* margin: auto; */
}

.size-20per {
  width: 25%;
  margin: auto;
  border-radius: 10rem;
}

.map-frame {
  width: 90%;
  max-height: 41vw;
  margin: auto;
  margin-top: 20px;
  border: 8px solid #0f4c82;
  display: flex;
  padding: 5px;
}

.map-col1 {
  float: left;
  width: 80%;
}

.map-col2 {
  float: right;
  width: 20%;
  margin-left: 10px;
  overflow: scroll;
}

.store-card {
  width: 20%;
}

.scrollbar {
  float: right;
  background: #fff;
  overflow-y: scroll;
  overflow-x: hidden;
  margin-bottom: 0px;
  padding-right: 10px;
}

.scrollbar-blue::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.1);
  background-color: #f5f5f5;
  border-radius: 10px;
}

.scrollbar-blue::-webkit-scrollbar {
  width: 12px;
  background-color: #f5f5f5;
}

.scrollbar-blue::-webkit-scrollbar-thumb {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.1);
  background-color: #0f4c82;
}
</style>
