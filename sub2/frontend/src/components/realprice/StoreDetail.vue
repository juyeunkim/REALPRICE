<template>
  <div class="storeDetail">
    <v-card>
      <v-card-title class="headline" style="padding-left: 30px; padding-top: 30px;">
        <p style="margin-bottom: 0px;">{{ store.storeName }}</p>
        <p class="orange--text" style="padding-left: 10px; margin-bottom: 0px;">{{ score }}</p>
        <v-spacer />
      </v-card-title>
      <v-divider />

      <!-- 식당 정보 -->
      <v-chip class="ma-2" color="primary">식당 정보</v-chip>
      <v-data-table
        :headers="headers"
        :items="items"
        hide-default-header
        hide-default-footer
        class="elevation-1"
      />

      <v-chip class="ma-2" color="primary">먹을 수 있는 메뉴</v-chip>

      <v-card-text>
        <p v-for="menu in menus" :key="menu.id">{{ menu.menu_name }} : {{ menu.price }}</p>

        <p>
          가격: {{ store.price }}
          <v-icon small>fas fa-won-sign</v-icon>
        </p>
      </v-card-text>
      <v-divider />
      <v-chip class="ma-2" color="primary">리뷰 만족 그래프</v-chip>
      <div class="columns">
        <div class="column">
          <DoughnutChart :percent="percent" :visible-value="true" />
        </div>
        <div class="column">
          <DoughnutChart
            :percent="percent"
            :visible-value="true"
            :foreground-color="'purple'"
            :empty-text="'N/A'"
          />
        </div>
      </div>
      <v-divider />
      <v-chip class="ma-2" color="primary">Review</v-chip>
      <v-container fluid>
        <REVIEW v-for="review in reviews" :key="review.id" :review="review" />
      </v-container>
      <v-card-actions>
        <v-spacer />
        <v-btn color="blue darken-1" text @click="emitClose">닫기</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import REVIEW from "./Review";
import DoughnutChart from "../DoughnutChart.vue";

export default {
  components: {
    REVIEW,
    DoughnutChart
  },
  props: {
    store: {
      type: Object,
      default: () => new Object()
    }
  },
  data() {
    return {
      headers: [
        {
          name: "Dessert (100g serving)",
          value: "name"
        },
        { text: "Value", value: "value" }
      ],
      items: [
        {
          name: "주소",
          value: this.store.address
        },
        {
          name: "가격",
          value: this.store.price
        },
        {
          name: "교통비",
          value: this.store.price
        }
      ]
    };
  },
  computed: {
    score: function(){
      return this.store.score.toFixed(2)
    },
    percent:function(){
      return (this.score / 5) * 100;
    },
    tags: function() {
      return this.store.categories.reduce((acc, v) => {
        return `${acc} #${v}`;
      }, "");
    },
    reviews: function() {
      return this.$store.getters["data/reviews"];
    },
    // price 이하인 음식메뉴만 보여주기
    menus: function() {
      return this.$store.getters["data/menus"].filter(list => {
        return list.price <= this.store.price;
      });
    }
  },
  watch: {
    store: function() {
      this.getStore();
    },
    reviews: function() {
      this.dataReviews = this.reviews;
    }
  },
  created() {
    this.$store.dispatch("data/getStoreInfo", this.store.id);
  },
  methods: {
    getStore() {
      console.log("AAAAAAAAAAAA");
      this.$store.dispatch("data/getStoreInfo", this.store.id);
    },
    emitClose: function() {
      this.$emit("close");
      this.$store.state.reviews = null;
    }
  }
};
</script>

<style>
.v-data-table tbody tr:hover:not(.v-data-table__expanded__content) {
  background: #ffffff !important;
}
</style>