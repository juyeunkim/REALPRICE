<template>
  <div class="app">
    <img class="search-logo" alt="logo" src="../assets/logo_blue.png">

    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <input
      v-model="inputPrice"
      class="form-control size-20per"
      type="text"
      placeholder="가격을 찾아보세요."
      aria-label="Search"
      @keyup.enter="search"
    >
    <v-dialog
      v-model="dialog"
      max-width="700"
    >
      <STOREDETAIL :store="selectedStore" @close="closeDetail" />
    </v-dialog>
    <div class="map-frame">
      <div class="map-col1">
        <Map />
      </div>
      <div class="map-col2 scrollbar scrollbar-blue bordered-blue">
        <StoreCard v-for="store in searchResult" :key="store.id" :store="store" @clickItem="selectItem" />
      </div>
      
    </div>

    <img class="marker" src="@/assets/marker.png">
  </div>
</template>

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=eac48c3548025ce4e0b61b1512b4282c"></script>

<script>
import STOREDETAIL from '@/components/realprice/StoreDetail';
import StoreCard from "@/components/search_map/StoreCard.vue";
import Map from "@/components/search_map/Map.vue";
import api from '@/api/index.js'

export default {
  name: "Landing",
  components: {
    STOREDETAIL,
    StoreCard,
    Map
  },
  data() {
    return {
      selectedStore: null,
      inputPrice: '',
      searchResult: [],
      dialog: false,
    }
  },
  methods: {
    search: function() {
      var data = {
        price : parseInt(this.inputPrice),
        ulatitude : 37.272618,
        ulongitude:127.038970,
        mlatitude : 37.501235,
        mlongitude : 127.039511,
        radius:1000
      }

      api.getStores(data)
      .then(response => {
        console.log(response.data.stores)
        this.searchResult = response.data.stores
        })
    },
    selectItem: function(id){
      console.log('IN!')
      this.searchResult.forEach(el => {
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
  }
};
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
