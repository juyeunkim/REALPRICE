<template>
  <v-app-bar id="app-toolbar" absolute app flat color="blue lighten-1">
    <v-btn v-if="responsive" dark icon @click.stop="onClickDrawer">
      <v-icon>mdi-view-list</v-icon>
    </v-btn>
    <router-link :to="{name:'home'}">
      <img class="logo" alt="logo" src="../assets/logo_white.png">
    </router-link>

    <v-spacer />

    <v-toolbar-items class="hidden-sm-and-down">
      <template v-if="userId=='' || userId==null || userId==undefined">
        <v-btn class="ml-2" text :to="{name: 'signup'}">회원가입</v-btn>

        <v-divider inset vertical />

        <v-btn class="ml-2" text :to="{name: 'signin'}">로그인</v-btn>
      </template>

      <template v-else>
        <v-btn class="ml-2" @click="logout">로그아웃</v-btn>

        <v-divider inset vertical />

        <v-btn class="ml-2" text :to="{name: 'mypage'}">마이페이지</v-btn>
      </template>
    </v-toolbar-items>

    <!-- 로그인한 유저 정보 -->
    <!-- <v-avatar>
      <img
        src="https://cdn.vuetifyjs.com/images/john.jpg"
        alt="John"
      >
    </v-avatar>-->
  </v-app-bar>
</template>

<script>
import { mapMutations, mapState } from "vuex";

export default {
  data: () => ({
    responsive: false
  }),
  computed: {
    ...mapState("app", ["drawer"]),
    userId: function() {
      return this.$store.getters["session/userStatus"];
    }
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
    },
    logout() {
      console.log("로그아웃!!");
      this.$alert("로그아웃 완료", "Success", "success");
      // dispatch로 action 호출
      this.$store.dispatch("session/logout");
      if (this.$route.path !== `/`) this.$router.push("home");
    }
  }
};
</script>

<style scoped>
.logo {
  width: 100px;
  margin: auto;
}
</style>