<template>
  <div class="app">
    <img class="search-logo" alt="logo" src="../assets/logo_blue.png">

    <!-- 가격 입력창 -->
    <v-text-field
      v-model="inputPrice"
      class="size-20per"
      solo
      label="가격을 찾아보세요."
      append-icon="search"
      @keyup.enter="search"
    />
    <input
      v-model="inputPrice"
      class="form-control size-20per"
      type="text"
      placeholder="가격을 찾아보세요."
      aria-label="Search"
      @keyup.enter="search"
    >
    <v-dialog v-model="dialog" max-width="700">
      <STOREDETAIL :store="selectedStore" @close="closeDetail" />
    </v-dialog>

    <!-- 태그창 -->
    <div>
      <mdb-badge v-for="tag in tags" :key="tag.id" pill color="blue">{{tag.name}}</mdb-badge>
    </div>

    <!-- 지도창 -->
    <div class="map-frame">
      <div class="map-col1">
        <Map />
      </div>
      <div class="map-col2 scrollbar scrollbar-blue bordered-blue">
        <StoreCard
          v-for="store in searchResult"
          :key="store.id"
          :store="store"
          @clickItem="selectItem"
        />
      </div>
    </div>

    <img class="marker" src="@/assets/marker.png">
  </div>
</template>

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=eac48c3548025ce4e0b61b1512b4282c"></script>

<script>
import STOREDETAIL from "@/components/realprice/StoreDetail";
import StoreCard from "@/components/search_map/StoreCard.vue";
import Map from "@/components/search_map/Map.vue";
import api from "@/api/index.js";
import { mdbBadge } from "mdbvue";

export default {
  name: "Landing",
  components: {
    STOREDETAIL,
    StoreCard,
    Map,
    mdbBadge
  },
  data() {
    return {
      selectedStore: null,
      inputPrice: "",
      searchResult: [],
      dialog: false,
      tags: []
    };
  },
  methods: {
    search: function() {
      var price = parseInt(this.inputPrice);

      if (!Number.isInteger(price) || price <= 0) {
        this.$alert("숫자만 입력해주세요", "Warning", "warning");
      } else {
        var data = {
          price: parseInt(this.inputPrice),
          ulatitude: 37.272618,
          ulongitude: 127.03897,
          mlatitude: 37.501235,
          mlongitude: 127.039511,
          radius: 1000
        };

        api.getStores(data).then(response => {
          console.log(response.data.stores);
          this.searchResult = response.data.stores;
          this.tags = response.data.tags;
        });
      }
    },
    selectItem: function(id) {
      console.log("IN!");
      this.searchResult.forEach(el => {
        if (el.id == id) {
          this.selectedStore = el;
        }
      });
      this.dialog = true;
    },
    getReviews: function() {
      consol.log("!!!");
      this.$store.dispatch("data/getReviews", this.selectedStore.id);
    },
    closeDetail: function() {
      console.log("closeDetail");
      this.dialog = false;
      // this.selectedStore = null;
    }
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap");

.app {
  background-color: white;
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
</style>
