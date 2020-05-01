<template>
<div style="display: flex;  bottom: 0;  left: 0;  right: 0; z-index:100;">
  <v-footer class="footer" height="auto" color="blue lighten-1" dark v-show="!colorWhite">
    <v-layout>
      <v-flex color="indigo" dark py-3 text-xs-center white--text xs12>
        &copy;2020 —
        <strong>SSAFY</strong>
        <p style="color : white"><b> <strong>A206</strong>  All rights reserved.</b></p> 
        <strong style="color : white">김주연</strong> &nbsp;
        <strong style="color : white">박정환</strong> &nbsp;
        <strong style="color : white">백창현</strong> &nbsp;
        <strong style="color : white">전경윤</strong> &nbsp;
        <strong style="color : white">정구헌</strong> &nbsp;
      </v-flex>
    </v-layout>
  </v-footer>
  <div class="footer white" height="auto" v-show="colorWhite">
    <v-layout>
      <v-flex py-3 text-xs-center xs12>
        &copy;2020 —
        <strong>SSAFY</strong>
        <p style="color : blue lighten-1"><b> <strong>A206</strong>  All rights reserved.</b></p> 
        <strong style="color : blue lighten-1">김주연</strong> &nbsp;
        <strong style="color : blue lighten-1">박정환</strong> &nbsp;
        <strong style="color : blue lighten-1">백창현</strong> &nbsp;
        <strong style="color : blue lighten-1">전경윤</strong> &nbsp;
        <strong style="color : blue lighten-1">정구헌</strong> &nbsp;
      </v-flex>
    </v-layout>
  </div>
</div>
</template>
<script>
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState({
      colorWhite: state => state.data.menuWhite,
    }),
  },
};
</script>
<style lang="scss" scoped>
  .footer{
    width: 100%;
    height: 120px;
    text-align: center;
  }
  .white{
    background-color: white;
  }
</style>
