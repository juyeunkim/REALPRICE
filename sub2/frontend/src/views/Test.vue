<template>
    <div class="app">
        <img class="search-logo" alt="logo" src="@/assets/logo_blue.png">

        <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
        <input class="form-control size-20per" type="text" placeholder="가격을 찾아보세요." aria-label="Search" v-on:keyup.enter="search" v-model="inputPrice"/>

        <div class="map-frame">
          <div class="map-col1">
              <Map :restaurants="RealPriceList" :user="geoLocation" @clickItem="selectItem" @drawCircle="selectCircle"/>
          </div>
          <div class="map-col2 scrollbar scrollbar-blue bordered-blue">
              <StoreCards v-bind:stores2="searchResult"/>
              <!-- test -->
          </div>
        </div>
        
        <img class="marker" src="@/assets/marker.png"/>

    </div>
</template>

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=eac48c3548025ce4e0b61b1512b4282c"></script>

<script>

import StoreCards from '@/components/search_map/StoreCards.vue'
import Map from "@/components/Map";
import axios from 'axios'

export default {
  name: 'Landing',
  components: {
    StoreCards,
    Map
  },
  props:{
    inputPrice: String,
    searchResult: Array
  },
  data() {
    return {
      geoLocation: {
        latitude: 37.50128969810118,
        longitude: 127.03960183847694,
      },
    }
  },
  computed: {
    ...mapState({
      RealPriceList: state => state.data.realPriceList,
    })
  },
  methods: {
    search:  function () {
      axios
      .get('http://13.125.68.33:8080/api/getStores/')
      .then(response => {
        console.log(response.data.stores)
        this.searchResult = response.data.stores
        })

      // alert('Hello ' + this.inputPrice + '!')
      // `event` 는 네이티브 DOM 이벤트입니다
      //if (event) {
      //  alert(event.target.tagName)
      //}
    },
    selectItem: function(id){
      this.RealPriceList.forEach(el => {
        if(el.id == id){
          this.selectedStore = el;
        }
      });
      this.dialog = true;
    },
    selectCircle: function(c, r){
      this.center = c;
      this.radius = r;
    },
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap');

.app {
  background-color: white;
}

.search-logo{
  width: 120px;
  display: flex;
  margin-top: 10px;
  margin-left: 10px;
  /* margin: auto; */
}

.marker{
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
  border: 8px solid #0F4C82;
  display: flex;
  padding: 5px;
}

.map-col1 {
  float: left;
  width: 80%
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
  background-color: #F5F5F5;
  border-radius: 10px;
}

.scrollbar-blue::-webkit-scrollbar {
  width: 12px;
  background-color: #F5F5F5;
}

.scrollbar-blue::-webkit-scrollbar-thumb {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.1);
  background-color: #0F4C82;
}
</style>
