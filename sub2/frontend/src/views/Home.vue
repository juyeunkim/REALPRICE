<template>
  <div id="app">
    <v-dialog
      v-model="dialog"
      max-width="700"
    >
      <STOREDETAIL :store="selectedStore" @close="closeDetail" />
    </v-dialog>
    <v-card-text class="text-center">
      <img class="logo" alt="logo" src="@/assets/logo_white.png">
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
          color="white"
          :size="50"
        />
      </div>
      <div class="explain" v-if="!isLoading">
        더 많은 결과를 보고 싶다면? <br>
        왼쪽 상단 지도 아이콘을 클릭하세요
      </div>
      
      <Cards :stores="RealPriceList" :isSearched="isSearched" @clickItem="selectItem"/>
    </v-card-text>
  </div>
</template>


<script>
import STOREDETAIL from '@/components/realprice/StoreDetail';
import Cards from '@/components/landing/Cards.vue'
import api from '@/api/index.js'
import { mapState, mapActions, mapMutations } from "vuex";

export default {
  name: 'Home',
  components: {
    STOREDETAIL,
    Cards
  },
  mounted() {
    // this.setMenuWhite(false);
    this.getLocation();
  },
  computed: {
    ...mapState({
      RealPriceList: state => state.data.realPriceStores,
    }),
    // num(inputPrice) {
    // }
  },
  watch: {
    inputPrice() {
      this.num = (!isNaN(this.inputPrice))?true:false;
    },
  },
  data(){
    return {
      isSearched: false,
      num: false,
      selectedStore: null,
      dialog: false,
      inputPrice: '',
      searchResult: [],
      geoLocation: {
        latitude: 0,
        longitude: 0,
      },
      isLoading: false
    }
  },
  methods: {
    ...mapActions("data", ["postRealPrice"]),
    ...mapMutations("data", ["setMenuWhite"]),
    closeDetail: function(){
      this.dialog = false;
      this.selectedStore = null;
    },
    selectItem: function(id){
      this.RealPriceList.forEach(el => {
        if(el.id == id){
          this.selectedStore = el;
        }
      });
      this.dialog = true;
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
          "radius":500
      }).then(()=>{
        this.isLoading = false;
        this.isSearched = true;
      }
      );
      }

      
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
          vm.geoLocation.latitude = 37.49798640700624;
          vm.geoLocation.longitude = 127.02765249685851;
        }, {
          enableHighAccuracy: false,
          maximumAge: 0,
          timeout: Infinity
        });
      } else {
        console.log('GPS를 지원하지 않습니다');
        vm.geoLocation.latitude = 37.49798640700624;
        vm.geoLocation.longitude = 127.02765249685851;
      }
    },
  }
}
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap');

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  background-color: #0F4C82;
}

.logo{
  width: 19.8vw;
  margin: auto;
  @media screen and (max-width: 600px) {
    width: 50vw;
  }
}

.size-20per {
  width: 50%;
  margin: auto;
  border-radius: 10rem;
  @media screen and (max-width: 600px) {
    width: 80vw;
  }
}

.explain{
  color: white;
  @media screen and (max-width: 600px) {
    display: none;
  }
}
</style>
