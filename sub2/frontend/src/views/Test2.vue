<template>
  <v-container>
    <!-- <v-card-text class="text-center">
      <p class="display-2 pa-5">테스트도 식후경</p>
      <p class="display-3 pa-2">🍱🍜🥡</p>
      <p class="display-3 pa-2">🍰🍔</p>
    </v-card-text> -->
    <VUEMAP />
    <!-- <VUEMAP2  :restaurants="this.RealPriceList" :user="this.multicampus"/> -->
    <!-- <VUEMAP2 /> -->
    
  </v-container>
</template>

<script>
import VUEMAP from '@/components/realprice/VueMap';
import VUEMAP2 from '@/components/realprice/VueMap2';
import VueDaumMap from 'vue-daum-map'
// import STOREDETAIL from '@/components/realprice/StoreDetail';
import LIST from "@/components/realprice/List";
import { mapState, mapActions } from "vuex";
export default {
  components: {
    // STOREDETAIL,
    VUEMAP2,
    VUEMAP,
    LIST,
  },
  data () {
    return {
      appKey: '57215b8d43e496f299e5cb6980099e42', // 테스트용 appkey
      center: {lat:33.450701, lng:126.570667}, // 지도의 중심 좌표
      level: 3, // 지도의 레벨(확대, 축소 정도),
      mapTypeId: VueDaumMap.MapTypeId.NORMAL, // 맵 타입
      libraries: [], // 추가로 불러올 라이브러리
      map: null, // 지도 객체. 지도가 로드되면 할당됨.

      dialog: false,
      selectedNum: 100,
      multicampus: {
        latitude: 37.50128969810118,
        longitude: 127.03960183847694,
      }
    }
  },
  computed: {
    ...mapState({
      SearchRealPrice: state => state.data.searchRealPrice,
      RealPriceList: state => state.data.realPriceList,
    })
  },
  methods: {
    // 지도가 로드 완료되면 load 이벤트 발생
    onLoad (map) {
        this.map = map
    }
  },
}
</script>