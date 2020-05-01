<template>
  <div class="app">
    <!-- 가격 입력창 -->
    <v-text-field
      v-model="inputPrice"
      class="size-20per"
      solo
      append-icon="search"
      label="금액을 입력하세요."
      suffix="원"
      :rules="[() => !!num || '숫자만 입력하세요.']"
      @click:append="searchSubmit"
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
    <div v-if="(tagList.length > 0) && !isLoading">
    원하는 태그를 선택하세요
    </div>
    <!-- 태그창 -->
    <div class="tags" v-if="(tagList.length > 0) && !isLoading">
      <mdb-badge pill color='blue' class="tag" v-show="!(tagList===null)" @click.native="allTag">All</mdb-badge>
      <mdb-badge v-for="tag in tagList"
      :key="tag.id"
      pill
      :color="(selectedTags.includes(tag.name))?'success':'blue'"
      class="tag"
      v-show="(tag.id < 61)" 
      @click.native="selectTag(tag.name)"># {{tag.name}}</mdb-badge>
    </div>
    <div v-if="(RealPriceList.length > 0) && !isLoading">
    지도를 움직여서 다시 검색해보세요
    </div>
    <!-- 지도창 -->
    <div class="map-frame">
      <div class="map-col1">
        <Map :restaurants="selectedStores" :user="geoLocation" :map="center" :zoom="zoom" @clickItem="selectItem" @drawCircle="selectCircle"/>
      </div>
      <div class="map-col2 scrollbar scrollbar-blue bordered-blue">
        <StoreCards :stores="selectedStores" :total="RealPriceList.length" :isSearched="isSearched" @clickItem="selectItem" @next="nextStores"/>
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
      isSearched: false,
      hoverId: -1,
      numsOfStore: 50,
      num: false,
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
  watch: {
    inputPrice() {
      this.num = (!isNaN(this.inputPrice))?true:false;
    },
  },
  computed: {
    ...mapState({
      RealPriceList: state => state.data.realPriceStores,
      tagList: state => state.data.realPriceTags,
    }),
    userLocation() {
        return this.geoLocation;
    },
    selectedStores() {
      var vm = this;
      let arr = [];
      if(this.selectedTags.length < 1){
        return this.RealPriceList.slice(0, (this.RealPriceList.length>this.numsOfStore)?this.numsOfStore:this.RealPriceList.length);
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
    hoverItem(id){
      this.hoverId = id;
    },
    outItem(){
      this.hoverId = -1;
    },
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
            "mlatitude": parseFloat(vm.center.Ha), 
            "mlongitude": parseFloat(vm.center.Ga),
            "radius":parseFloat(vm.radius)
        }).then(()=>{
          this.isLoading = false;
          this.isSearched = true;
          this.numsOfStore = 50;
        });
      }
    },
    nextStores: function() {
      // console.log('next!');
      if(this.RealPriceList.length >= this.numsOfStore + 30){
        this.numsOfStore += 30;
      } else {
        this.numsOfStore = this.RealPriceList.length;
      }
    }
  },
}
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap");
.app {
  background-color: white;
  // height: calc(200px + 50vw + 120px);
  padding-top: 10px;
  padding-bottom: 10px;
  text-align: center;
  @media screen and (max-width: 600px) {
    height: 110vh;
    // padding-bottom: 120px;
  }
}

.tags{
  width: 90%;
  margin: auto;
  // height: calc(200px - 7vw);
  border-bottom-width: 10px;
  margin-bottom: 15px;

  .tag{
    // margin-left: 0.1vw;
    margin-right: 0.8vw;
    // font-size: 0.8vw;
  }
  .hover{
    font-size: 1vw;
  }
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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
  @media screen and (max-width: 600px) {
    width: 60vw;
  }
}

.map-frame {
  width: 90%;
  // max-height: 41vw;
  height: 42vw;
  margin: auto;
  margin-top: 20px;
  border: 8px solid #0f4c82;
  display: flex;
  padding: 5px;
  @media screen and (max-width: 600px) {
    padding: 0px;
    border: 0px;
    position: relative;
  }
}

.map-col1 {
  float: left;
  width: 75%;
  @media screen and (max-width: 600px) {
    // position: absolute;
    width: 100%;
    height: 50vw;
  }
}

.map-col2 {
  float: right;
  width: 25%;
  margin-left: 10px;
  overflow: scroll;
  @media screen and (max-width: 600px) {
    position: absolute;
    margin-bottom: 10px;
    top: 50vw;
    float: left;
    width: 100%;
    height: 60vw;
    overflow: unset;
    overflow-y: hidden;
    overflow-x: auto;
    display: flex; /* or inline-flex */
    flex-direction: row;
    // width: 100vw;
    margin-left: 0px;
    white-space:nowrap;
    // position: absolute;
  }
}

.scrollbar {
  float: right;
  background: #fff;
  overflow-y: scroll;
  overflow-x: hidden;
  margin-bottom: 0px;
  padding-right: 10px;
  @media screen and (max-width: 600px) {
    // float: none;
    overflow-x: scroll;
    overflow-y: hidden;
  }
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

</style>
