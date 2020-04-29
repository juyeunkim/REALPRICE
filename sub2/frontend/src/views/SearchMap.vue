<template>
  <div class="app">
    <!-- 가격 입력창 -->
    <v-text-field
      v-model="inputPrice"
      class="size-20per"
      solo
      label="가격을 찾아보세요."
      append-icon="search"
      @keyup.enter="searchSubmit"
    />
    <div v-if="isLoading">
      <v-progress-circular
        indeterminate
        color="primary"
        :size="50"
      />
    </div>
    
    <v-dialog
      v-model="dialog"
      max-width="700"
    >
      <STOREDETAIL :store="selectedStore" @close="closeDetail" />
    </v-dialog>
    
    원하는 태그를 선택하세요
    <!-- 태그창 -->
    <div class="tags">
      <mdb-badge pill color='blue' class="tag" v-show="!(tagList===null)" @click.native="allTag">All</mdb-badge>
      <mdb-badge v-for="tag in tagList"
      :key="tag.id"
      pill
      :color="(selectedTags.includes(tag.name))?'success':'blue'"
      class="tag"
      v-show="(tag.id < 61)" 
      @click.native="selectTag(tag.name)"># {{tag.name}}</mdb-badge>
    </div>
    범위를 조정하고 싶다면?
    지도를 움직여서 다시 검색하세요
    <!-- 지도창 -->
    <div class="map-frame">
      <div class="map-col1">
        <Map :restaurants="selectedStores" :user="geoLocation" :map="center" :zoom="zoom" @clickItem="selectItem" @drawCircle="selectCircle"/>
      </div>
      <div class="map-col2 scrollbar scrollbar-blue bordered-blue">
        <StoreCards :stores="selectedStores" @clickItem="selectItem" />
        <!-- <StoreCard v-for="store in RealPriceList" :key="store.id" :store="store" @clickItem="selectItem" /> -->
      </div>
    </div>

    <!-- <img class="marker" src="@/assets/marker.png"> -->
  </div>
</template>

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=eac48c3548025ce4e0b61b1512b4282c"></script>

<script>
import STOREDETAIL from '@/components/realprice/StoreDetail';
import StoreCards from '@/components/search_map/StoreCards.vue'
import Map from "@/components/Map.vue";
import api from '@/api/index.js'
import { mapState, mapActions, mapMutations } from "vuex";
import { mdbBadge } from 'mdbvue';

export default {
  name: "Landing",
  components: {
    STOREDETAIL,
    StoreCards,
    Map,
    mdbBadge
  },
  data() {
    return {
      selectedTags: [],
      inputPrice: '',
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
      radius: 5,
      zoom: 0,
      isLoading: false
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
    selectedStores() {
      var vm = this;
      let arr = [];
      if(this.selectedTags.length < 1){
        return this.RealPriceList;
      } else {
        this.RealPriceList.forEach(el => {
          var isIn = false;
          el.tags.forEach(t => {
            if(vm.selectedTags.includes(t)){
              isIn = true;
            }
          })

          if(isIn) {
            arr.push(el);
          }
        })
        return arr;
      }
    },
  },
  mounted() {
    this.setMenuWhite(true);
    this.getLocation();
  },
  destroyed() {
    this.setMenuWhite(false);
  },
  methods:{
    ...mapActions("data", ["postRealPrice"]),
    ...mapMutations("data", ["clearRealPrice", "setMenuWhite"]),
    allTag(){
      var vm = this;
      if(this.selectedTags.length < 1){
        this.tagList.forEach(t => {
          vm.selectedTags.push(t.name);
        })
      } else {
        this.selectedTags = [];
      }
    },
    selectTag(key){ 
      if(this.selectedTags.includes(key)){
        const idx = this.selectedTags.indexOf(key)
        if (idx > -1) this.selectedTags.splice(idx, 1)
      } else {
        this.selectedTags.push(key);
      }
    },
    selectItem: function(id){
      this.RealPriceList.forEach(el => {
        if(el.id == id){
          this.selectedStore = el;
        }
      });
      this.dialog = true;
    },
    getReviews: function() {
      consol.log("!!!");
      this.$store.dispatch("data/getReviews", this.selectedStore.id);
    },
    closeDetail: function(){
      this.dialog = false;
      // this.selectedStore = null;
    },
    selectCircle: function(center, radius, level, str){      
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
          vm.geoLocation.latitude = 37.497986408991245;
          vm.geoLocation.longitude = 127.02764401536562;
        }, {
          enableHighAccuracy: false,
          maximumAge: 0,
          timeout: Infinity
        });
      } else {
        console.log('GPS를 지원하지 않습니다');
        vm.geoLocation.latitude = 37.497986408991245;
        vm.geoLocation.longitude = 127.027644015365624;
      }
    },
    searchSubmit: function() {
      const vm = this;
      var price = parseInt(vm.inputPrice);
      if(!Number.isInteger(price) || price <= 0){
        this.$alert("숫자만 입력해주세요", "Warning", "warning");
      }else{
        this.isLoading = true;
        this.postRealPrice({
          "price": parseInt(vm.inputPrice), 
          "ulatitude": parseFloat(vm.geoLocation.latitude),
          "ulongitude": parseFloat(vm.geoLocation.longitude),
          "mlatitude": parseFloat(vm.geoLocation.latitude), 
          "mlongitude": parseFloat(vm.geoLocation.longitude),
          "radius":parseFloat(vm.radius)
       }).then(()=>{
        this.isLoading = false;
      }
      );
      }
      
    }
  },
}
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap");
.app {
  background-color: white;
  height: calc(100vh-120px);
  padding-bottom: 10px;
  text-align: center;
}

.tags{
  width: 90%;
  margin: auto;
  .tag{
    // margin-left: 0.1vw;
    margin-right: 0.8vw;
    // font-size: 0.8vw;
  }
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
}

.v-input__slot{
  text-align: right;
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

.v-progress-circular {
margin: 1rem;
}

.tags{
  
  border-bottom-width: 10px;
  margin-bottom: 15px;

}
</style>
