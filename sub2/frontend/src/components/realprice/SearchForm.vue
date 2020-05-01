<template>
  <v-container>
    <v-card class="mx-auto" max-width="500">
      <v-card-text class="text-center">
        <!-- <v-select
          :items="orderby"
          label="orderby"
          v-model="Options.searchOptions.orderby"
          dense
        ></v-select>
        <v-select
          :items="searchType"
          label="searchType"
          v-model="Options.searchOptions.searchType"
          dense
        ></v-select>
        <v-select
          :items="searchNum"
          label="searchNum"
          v-model="Options.searchOptions.searchNum"
          dense
        ></v-select>

        <v-list
          :dense=true
        >
          <v-subheader>userInfo</v-subheader>
          <v-list-item-group color="primary">
            <v-list-item
              v-for="(user, i) in Options.userInfo"
              :key="i"
              :inactive=true
            >
              <v-list-item-avatar>
                <v-img :src="user.avatar"></v-img>
                <v-icon class="red--text" @click="minusUser(i)">fas fa-times</v-icon>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title>{{user.curLatitude}} , {{user.curLongitude}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
        <v-layout row>
          <v-flex xs5>
            <v-text-field label="curLatitude" hide-details="auto" v-model="tmpUser.curLatitude"></v-text-field>
          </v-flex>
          <v-flex xs5>
             :rules="userRules"
            <v-text-field label="curLongitude" hide-details="auto" v-model="tmpUser.curLongitude"></v-text-field>
          </v-flex>
          <v-flex xs2>
            <v-icon class="green--text" @click="plusUser">fas fa-plus</v-icon>
          </v-flex>
        </v-layout>



        <v-list
          :dense=true
        >
          <v-subheader>areaInfo</v-subheader>
          <v-list-item-group v-model="userNum" color="primary">
            <v-list-item
              v-for="(area, i) in Options.areaInfo"
              :key="i"
              :inactive=true
            >
              <v-list-item-avatar>
                <v-img :src="user.avatar"></v-img>
                <v-icon class="red--text" @click="minusArea(i)">fas fa-times</v-icon>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title>{{area.address}} , {{area.detailAddr}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
        <v-layout row>
          <v-flex xs5>
            <v-text-field label="address" hide-details="auto" v-model="tmpArea.address"></v-text-field>
          </v-flex>
          <v-flex xs5>
             :rules="userRules"
            <v-text-field label="detailAddr" hide-details="auto" v-model="tmpArea.detailAddr"></v-text-field>
          </v-flex>
          <v-flex xs2>
            <v-icon class="green--text" @click="plusArea">fas fa-plus</v-icon>
          </v-flex>
        </v-layout>
        <v-slider v-model="Options.maxDistance" min="0" max="50" label="최대거리(km)" thumb-label />
        <v-slider v-model="Options.minPoint" min="0" max="5" label="최소평점(점)" thumb-label />
        <v-slider v-model="Options.maxPrice" min="1000" max="50000" label="최대가격(원)" thumb-label /> -->
        <input v-model="inputPrice" class="form-control size-20per" type="text" placeholder="가격을 찾아보세요." aria-label="Search" @keyup.enter="Search">
        <v-btn large color="blue lighten-1 white--text ma-5" rounded @click="Search">검색하기</v-btn>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data() {
    return {
      // tmpArea:{
      //   address:'',
      //   detailAddr:'',
      // },
      // tmpUser:{
      //   curLatitude: '',
      //   curLongitude: '',
      // },
      // userNum: 5,
      // userRules: [
      //   value => (value && value.length >= 6) || 'Min 7 characters',
      // ],
      // orderby: ['distance', 'avg_score', 'avg_price'],
      // searchType: ['area', 'user'],
      // searchNum: ['one', 'many'],
      

      // Options: {
      //   searchOptions: {
      //       orderby: "avg_score",
      //       searchType: "area",
      //       searchNum: "many"
      //   },
      //   userInfo: [
      //       {
      //           curLatitude: 37.511069,
      //           curLongitude: 127.021327
      //       },
      //       {
      //           curLatitude: 37.497887,
      //           curLongitude: 127.027535
      //       }
      //   ],
      //   areaInfo: [
      //       {
      //           address:"서울특별시 강남구 역삼동",
      //           detailAddr:""
      //       },
      //       {
      //           address:"서울특별시 강남구 역삼동",
      //           detailAddr:"671-3"
      //       },
      //       {
      //           address:"강남",
      //           detailAddr:""
      //       }
      //   ],
      //   maxDistance: 1,
      //   minPoint: 3,
      //   maxPrice: 10,
      //   foodfilter: ""
      // },
      inputPrice: 10000,
    };
  },
  computed: {
    RealPrice: function() {
      return this.$store.getters["data/RealPrice"];
    }
  },
  methods: {
    // ...mapActions("data", []),
    Search: function() {
      // params.maxPrice = this.Options.maxPrice * 1000;
      // console.log(this.Options);
      // console.log(params);
      this.$emit('search', this.inputPrice);
    },
    plusUser: function() {
      var tmp = [{
        curLatitude: this.tmpUser.curLatitude,
        curLongitude: this.tmpUser.curLongitude,
      }];
      this.Options.userInfo = this.Options.userInfo.concat(tmp);
    },
    minusUser: function(idx) {
      var length = this.Options.userInfo.length;
      var a = this.Options.userInfo.slice(0,idx);
      var b = this.Options.userInfo.slice(idx+1, length);
      this.Options.userInfo = a.concat(b);
    },
    plusArea: function() {
      var tmp = [{
        address: this.tmpArea.address,
        detailAddr: this.tmpArea.detailAddr,
      }];
      this.Options.areaInfo = this.Options.areaInfo.concat(tmp);
    },
    minusArea: function(idx) {
      var length = this.Options.areaInfo.length;
      var a = this.Options.areaInfo.slice(0,idx);
      var b = this.Options.areaInfo.slice(idx+1, length);
      this.Options.areaInfo = a.concat(b);
    },
  }
};
</script>