<template>
  <v-app-bar id="app-toolbar" app flat color="blue lighten-1">
    <v-btn v-if="responsive" dark icon @click.stop="onClickDrawer">
      <v-icon>mdi-view-list</v-icon>
    </v-btn>
    <v-spacer />
    <!-- 더보기 버튼 (미완성) -->
    <!-- <v-toolbar-items>
      <v-btn icon>
        <v-icon>mdi-dots-vertical </v-icon>
      </v-btn>
    </v-toolbar-items>-->

    <!-- 로그인한 유저 정보 -->
    <!-- <v-avatar>
      <img
        src="https://cdn.vuetifyjs.com/images/john.jpg"
        alt="John"
      >
    </v-avatar> -->
    
    <v-list rounded>
      <v-list-item router-link :to="{name: 'signup'}">회원가입</v-list-item>
    </v-list>
    <v-list rounded>
      <v-list-item router-link :to="{name: 'signin'}">로그인</v-list-item>
    </v-list>
    <v-list rounded>
      <v-list-item router-link :to="{name: 'mypage'}">마이페이지</v-list-item>
    </v-list>
  </v-app-bar>
</template>

<script>
import { mapMutations, mapState } from "vuex";

export default {
  data: () => ({
    responsive: false,
    items:[
      
    ]
  }),
  computed: {
    ...mapState("app", ["drawer"])
  },
  mounted() {
    this.onResponsiveInverted();
    window.addEventListener("resize", this.onResponsiveInverted);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.onResponsiveInverted);
  },

  methods: {
    ...mapMutations("app", ["setDrawer"]),
    onClickDrawer() {
      this.setDrawer(!this.drawer);
    },
    onResponsiveInverted() {
      if (window.innerWidth < 900) {
        this.responsive = true;
      } else {
        this.responsive = false;
      }
    }
  }
};
</script>
