<template>
  <div>
    <v-app-bar
      v-show="!colorWhite"
      id="app-toolbar"
      class="toolbar"
      absolute
      app
      flat
      color="blue lighten-1"
    >
      <!-- <v-btn v-if="responsive" dark icon @click.stop="onClickDrawer">
      <v-icon>mdi-view-list</v-icon>
      </v-btn>-->
      <router-link :to="{name:'home'}">
        <img class="logo" alt="logo" src="@/assets/logo_white.png">
      </router-link>

      <v-toolbar-items>
        <!-- <v-btn class="ml-2 linkBtn" text :to="{name: 'landing'}"><v-icon>fas fa-won-sign</v-icon></v-btn> -->
        <v-btn class="ml-2 linkBtn" text :to="{name: 'searchmap'}">
          <v-icon>mdi-map</v-icon>
        </v-btn>
      </v-toolbar-items>
      <v-spacer />

      <v-toolbar-items>
        <template v-if="userId=='' || userId==null || userId==undefined">
          <v-btn class="ml-2" text :to="{name: 'signup'}">SignUp</v-btn>

          <v-divider inset vertical />

          <v-btn class="ml-2" text :to="{name: 'signin'}">LogIn</v-btn>
        </template>

        <template v-else>
          <v-btn class="ml-2" text @click="logout">LogOut</v-btn>

          <v-divider inset vertical />

          <v-btn class="ml-2" text :to="{name: 'mypage'}">MyPage</v-btn>
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
    <v-app-bar v-show="colorWhite" id="app-toolbar" absolute app flat color="white lighten-1">
      <!-- <v-btn v-if="responsive" dark icon @click.stop="onClickDrawer">
      <v-icon>mdi-view-list</v-icon>
      </v-btn>-->
      <router-link :to="{name:'home'}">
        <img class="logo" alt="logo" src="@/assets/logo_blue.png">
      </router-link>

      <v-toolbar-items>
        <!-- <v-btn class="ml-2" text :to="{name: 'landing'}"><v-icon>fas fa-won-sign</v-icon></v-btn> -->
        <v-btn class="ml-2" text :to="{name: 'searchmap'}">
          <v-icon>mdi-map</v-icon>
        </v-btn>
      </v-toolbar-items>
      <v-spacer />

      <v-toolbar-items>
        <template v-if="userId=='' || userId==null || userId==undefined">
          <v-btn class="ml-2" text :to="{name: 'signup'}">SignUp</v-btn>

          <v-divider inset vertical />

          <v-btn class="ml-2" text :to="{name: 'signin'}">LogIn</v-btn>
        </template>

        <template v-else>
          <v-btn class="ml-2" text @click="logout">LogOut</v-btn>

          <v-divider inset vertical />

          <v-btn class="ml-2" text :to="{name: 'mypage'}">MyPage</v-btn>
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
  </div>
</template>

<script>
import { mapMutations, mapState } from "vuex";

export default {
  data: () => ({
    responsive: false
  }),
  computed: {
    // ...mapState("app", ["drawer"]),
    userId: function() {
      return this.$store.getters["session/userStatus"];
    },
    ...mapState({
      colorWhite: state => state.data.menuWhite
    })
  },
  mounted() {
    // this.onResponsiveInverted();
    // window.addEventListener("resize", this.onResponsiveInverted);
  },
  beforeDestroy() {
    // window.removeEventListener("resize", this.onResponsiveInverted);
  },

  methods: {
    // ...mapMutations("app", ["setDrawer"]),
    // onClickDrawer() {
    //   this.setDrawer(!this.drawer);
    // },
    // onResponsiveInverted() {
    //   if (window.innerWidth < 900) {
    //     this.responsive = true;
    //   } else {
    //     this.responsive = false;
    //   }
    // },
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

<style lang="scss" scoped>
.toolbar {
  width: 100%;
  height: 10vw;
}
.logo {
  width: 100px;
  margin: auto;
}
.linkBtn{
  @media screen and (max-width: 600px){
    // display: none;
  }
}
</style>