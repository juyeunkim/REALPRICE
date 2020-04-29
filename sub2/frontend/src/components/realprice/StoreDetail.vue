<template>
  <div class="storeDetail">
    <v-card>
      <v-card-title class="headline" style="padding-left: 30px; padding-top: 30px;">
        <p style="margin-bottom: 0px;">{{ store.storeName }}</p>
        <img class="star" src="@/assets/star.png" />
        <p class="orange--text" style="padding-left: 5px; margin-bottom: 0px;">{{ score }}</p>
        <v-spacer />
      </v-card-title>
      <v-divider />

      <!-- 식당 정보 -->
      <v-card-text>
        <v-chip class="ma-2" color="primary">식당 정보</v-chip>
        
        <v-simple-table>
          <template v-slot:default>
            <tbody>
              <tr>
                <td> 주소 </td>
                <td>
                  {{ store.address }}
                </td>
              </tr>
              <tr>
                <td> 가격 </td>
                <td>
                  {{ store.price }} <v-icon small>fas fa-won-sign</v-icon>
                </td>
              </tr>
              <tr>
                <td> 교통비 </td>
                <td>
                  {{ store.distanceCost }} <v-icon small>fas fa-won-sign</v-icon>
                </td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
        
        <v-chip class="ma-2" color="primary">먹을 수 있는 메뉴</v-chip>
        메뉴 수 : {{ menus.length }}
        <v-simple-table dense>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">메뉴</th>
                <th class="text-left">가격</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="menu in menus" :key="menu.id">
                <td>{{ menu.menu_name }}</td>
                <td>
                  {{ menu.price }}
                  <v-icon small>fas fa-won-sign</v-icon>
                </td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
        
        <v-divider />
        <v-chip class="ma-2" color="primary">리뷰 만족 그래프</v-chip>
        <div class="columns">
          <div class="column">
            <DoughnutChart :percent="percent" :visible-value="true" />
          </div>
          <!-- 먹을 수 있는 메뉴 개수로 그래프 만들기 -->
          <!-- <div class="column">
          <DoughnutChart
            :percent="percent"
            :visible-value="true"
            :foreground-color="'purple'"
            :empty-text="'N/A'"
          />
          </div>-->
        </div>
        <v-divider />
        <v-chip class="ma-2" color="primary">Review</v-chip>
        리뷰 수 : {{ reviews.length }}
        <v-container fluid>
          <REVIEW v-for="review in reviews" :key="review.id" :review="review" />
        </v-container>
        <!-- <v-card-actions>
          <v-spacer />
          <v-btn color="blue darken-1" text @click="emitClose">닫기</v-btn>
        </v-card-actions>-->
      </v-card-text>
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
    };
  },
  computed: {
    score: function() {
      return this.store.score.toFixed(1);
    },
    percent: function() {
      return (this.score / 5).toFixed(2) * 100;
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
      this.$store.dispatch("data/getStoreInfo", this.store.id);
    },
    emitClose: function() {
      this.$emit("close");
    }
  }
};
</script>

<style scpoed>
.v-data-table tbody tr:hover:not(.v-data-table__expanded__content) {
  background: #ffffff !important;
}
.star {
  width: 2vw;
  padding-left: 10px;
}

.fa-won-sign {
  font-size: 14px;
}
</style>