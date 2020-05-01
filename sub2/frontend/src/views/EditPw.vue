<template>
  <div>
    <v-container fluid>
      <v-layout row>
        <v-flex xs12 md6 offset-md3>
          <v-card>
            <v-toolbar color="indigo" dark>
              <v-toolbar-title>비밀번호 수정</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <span class="title">Personal Info</span>

              

            </v-card-text>

            <v-divider class="mt-5" />
            <v-card-actions>
              <!-- <v-btn flat>Cancel</v-btn> -->
              <v-spacer />
              <v-btn color="primary" to="/mypage">취소</v-btn>
              <v-btn color="primary" @click="submit">수정</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import api from "../api/index";

export default {
  data: () => ({
    items: ["오이", "고수"],

    // 유효성 검사
    nameRules: [
      v => !!v || "Name is required",
      v => v.length <= 10 || "Name must be less than 10 characters"
    ],
    phoneRules: [
      v => !!v || "Phone is required",
      v =>
        /^[0-9]{3}-([0-9]{3}|[0-9]{4})-[0-9]{4}$/.test(v) ||
        "Phone must be valid"
    ]
  }),
  computed: {
    userInfo: function() {
      return this.$store.getters["data/userInfo"];
    }
  },
  created() {
    this.$store.dispatch("data/userInfo", sessionStorage.getItem("pk"));
  },
  methods: {
    submit() {
      console.log(userInfo)
      if (userInfo.profile.name != "" && userInfo.profile.phone != "") {
        console.log(userInfo);
        // api.updateUser(sessionStorage.getItem("pk"), userInfo)
        // Axios
        //     Axios.post("/api/users/", data)
        //       .then(res => {
        //         console.log(res);
        //         this.$alert("회원가입 성공", "Success", "success");
        //       })
        //       .catch(exp => {
        //         console.log("실패");
        //         this.$alert("회원가입 실패", "Warning", "warning");
        //       });
        //   } else {
        //     this.$alert("항목을 모두 입력해주세요", "Warning", "warning");
        // TODO : 마이페이지로 이동
        this.$router.push('/mypage')
      }else{
        this.$alert("항목을 모두 입력해주세요","Warning","warning");
      }

    },
    
  }
};
</script>

<style>
</style>