<template>
  <!-- Grid row -->
  <!-- <mdb-row> -->
  <mdb-row class="store-row" @click.native="selectItem()">
    <!-- Grid column -->
    <mdb-col col="12" id="col">
      <!--Panel-->
      <mdb-card class="card-body2 mb-3 border-color">
        <mdb-media class="d-block d-md-flex cardMedia">
          <mdb-media-image
            class="d-flex avatar-2 mb-md-0 mb-3 mx-auto food-img"
            :src="(store.srcUrl===null)?require('@/assets/logo_ver1.png'):store.srcUrl"
            alt="image"
          />
          <!-- :src="store.srcUrl" -->
          <mdb-media-body class="text-center text-md-left ml-md-3 ml-0">
            <div class="card-body2">
              <!-- Title -->
              <h4 class="card-title font-weight-bold store-title">
                <a>
                  {{store.storeName}}
                  <span class="thumbnscore"><img class="thumb" src='@/assets/star.png'/> {{ score }}</span>
                </a>
              </h4>
              <!-- Data -->
              <p class="price-per">{{ store.menu }}</p>
              <hr class="line">
              <p class="price-font">{{ wonDisplay }}</p>
              <p class="distance-font">교통비 {{ distCostDisplay }} 포함</p>
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
    store: {
      type: Object,
      default: () => new Object()
    }
  },
  data(){
    return {
      defaultURL: "require('@/assets/logo_ver1.png')",
    }
  },
  computed: {
    score: function(){
      return this.store.score.toFixed(1);
    },
    percent: function(){
      return Math.floor((this.score / 5) * 100);
    },
    distCostDisplay: function(){
      return String(this.store.distanceCost).replace(/(\d)(?=(?:\d{3})+(?!\d))/g, "$1,") + "원";
    },
    wonDisplay: function() {
      return String(this.store.price + this.store.distanceCost).replace(/(\d)(?=(?:\d{3})+(?!\d))/g, "$1,") + "원";
    }
  },
  methods: {
    selectItem() {
      this.$emit("clickItem", this.store.id);
    },
    hoverItem(id){
      console.log("hover"+id);
      // this.$emit("hover", id);
    },
    outItem(){
      console.log("out");
      // this.$emit("out");
    }
  }
};
</script>

<style lang="scss" scoped>
@font-face {
  font-family: "TmonMonsori";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/TmonMonsori.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

#col{
  padding-top: 0px; 
  padding-bottom: 0px; 
}

.distance-font {
  margin: 0 0 0 0;
  font-size: 0.5vw;
  @media screen and (max-width: 600px) {
    font-size: 1.5vw;
  }
}
.price-font {
    font-family: 'TmonMonsori';
    font-size: 1.3vw;
    margin-bottom: 0px;
    color: #0F4C82;
    @media screen and (max-width: 600px) {
      font-size: 3vw;
    }
}

.price-per {
  color: orange;
  font-family: 'TmonMonsori';
  font-size: 1vw;
  margin-bottom: 5px;
  @media screen and (max-width: 600px) {
    width: 100%;
  }
}

.card-body2 {
  flex: 1 1 auto;
  min-height: 1px;
  padding: 0.5rem;
}

.store-title {
  font-size: 1vw;
  font-weight: bold;
  color: #0F4C82;
  @media screen and (max-width: 600px) {
    font-size: 3vw;
  }
}

.thumbnscore{
  @media screen and (max-width: 600px) {
    display: block;
  }
}

.thumb {
  width: 1vw;
  padding-bottom: 10px;
}

.food-img {
  width:  7vw;
  height: 7vw;
  margin-top: 0.5vw;
  padding: 0px;
  @media screen and (max-width: 600px) {
    width:  10vw;
    height: 10vw;
    margin: auto auto;
  }
}

.line {
  border: 1px dashed #0F4C82;
  margin: 0 0 0 0;
}

.border-color {
  border: 1.5px solid #0F4C82;
}

</style>