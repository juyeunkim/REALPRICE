<template>
  <div class="storeDetail">
    <v-card>
      <v-card-title class="headline">
        <p style="margin-bottom: 0px;">{{ store.store_name }}</p>
        <p
          class="orange--text"
          style="padding-left: 10px; margin-bottom: 0px;"
        >{{ store.avg_score }}</p>
        <v-spacer />
        <v-btn icon>
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
      </v-card-title>

      <v-card-text>
        주소: {{ store.address }}
        <br />
        전화번호: {{ store.tel }}
        <br />
        카테고리: {{ store.category }}
        <br />
        평균가격: {{ store.avg_price }} <v-icon small>fas fa-won-sign</v-icon>
        <br />
        평균평점: {{ store.avg_score }}
        <br />
      </v-card-text>
      <v-divider />
      <v-chip class="ma-2" color="primary">리뷰 만족 그래프</v-chip>
      <DoughnutChart :percent="percent" :visible-value="true" />
      <v-divider />
      <v-chip class="ma-2" color="primary">Review</v-chip>
      <REVIEW v-for="review in dataReviews" :key="review.id" :review="review" />
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
      percent: "25",
      dataReviews: [],
    };
  },
  computed: {
    tags: function() {
      return this.store.categories.reduce((acc, v) => {
        return `${acc} #${v}`;
      }, "");
    },
    reviews: function() {
      return this.$store.getters["data/reviews"];
    }
  },
  watch: {
    store: function() {
      this.getReviews();
    },
    reviews: function() {
      this.dataReviews = this.reviews;
    }
  },
  created() {
    this.$store.dispatch("data/getReviews", this.store.id);
  },
  methods: {
    getReviews() {
      console.log("AAAAAAAAAAAA");
      this.$store.dispatch("data/getReviews", this.store.id);
    },
    emitClose: function() {
      this.$emit("close");
      this.dataReviews = null;
    }
  }
};
</script>

<style>
</style>