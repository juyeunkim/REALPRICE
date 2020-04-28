<template>
  <!-- Grid row -->
  <mdb-row class="store-row">
    <!-- Grid column -->
    <mdb-col md="10" lg="8" xl="12" class="mb-r">
      <!--Panel-->
      <mdb-card class="card-body2 mb-3 border-color">
        <mdb-media class="d-block d-md-flex">
          <mdb-media-image
            class="d-flex avatar-2 mb-md-0 mb-3 mx-auto food-img"
            :src="srcUrl"
            alt="Generic placeholder image"
          />
          <mdb-media-body class="text-center text-md-left ml-md-3 ml-0">
            <div class="card-body2">
              <!-- Title -->
              <h4 class="card-title font-weight-bold store-title">
                <a>{{s.storeName}}</a>
              </h4>
              <!-- Data -->
              <p class="price-per">
                가성비 {{s.score}}%
                <img class="thumb" src="@/assets/good.png">
              </p>
              <hr class="line">
              <p class="price-font">{{ s.price }}</p>
            </div>
          </mdb-media-body>
        </mdb-media>
      </mdb-card>
      <!--/.Panel-->
    </mdb-col>
    <!-- Grid column -->
  </mdb-row>
  <!-- Grid row -->
</template>

<script>
import {
  mdbMedia,
  mdbMediaBody,
  mdbMediaImage,
  mdbCard,
  mdbCol,
  mdbRow
} from "mdbvue";

export default {
  name: "StoreCard",
  components: {
    mdbMedia,
    mdbMediaBody,
    mdbMediaImage,
    mdbCard,
    mdbCol,
    mdbRow
  },
  props: {
    storeInfo: Object
    // srcUrl: String,
    // storeName: String,
    // price: String,
    // percent: String
  },
  computed: {
    s() {
      return this.storeInfo;
    },
    wonDisplay: function() {
      return this.price.replace(/(\d)(?=(?:\d{3})+(?!\d))/g, "$1,") + "원";
    }
  }
};
</script>

<style scoped>
@font-face {
  font-family: "TmonMonsori";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/TmonMonsori.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

.price-font {
  font-family: "TmonMonsori";
  font-size: 1.3vw;
  margin-bottom: 0px;
  color: #0f4c82;
}

.price-per {
  color: orange;
  font-family: "TmonMonsori";
  font-size: 1vw;
  margin-bottom: 5px;
}

.card-body2 {
  flex: 1 1 auto;
  min-height: 1px;
  padding: 0.5rem;
}

.store-title {
  font-size: 1vw;
  font-weight: bold;
  color: #0f4c82;
}

.thumb {
  width: 1vw;
}

.food-img {
  width: 5vw;
  margin-top: 0.5vw;
}

.line {
  border: 1px dashed #0F4C82;
  margin: 0 0 0 0;
}

.border-color {
  border: 1.5px solid #0F4C82;
}

.store-row {

}
</style>