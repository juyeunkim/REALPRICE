<template>
  <div>
    <v-container fluid>
      <v-layout row wrap>
        <v-flex xs12 md6 offset-md3>
          <v-card>
            <v-toolbar color="indigo" dark>
              <v-toolbar-title>로그인</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <!-- 이메일 -->
              <v-text-field
                v-model="email"
                :rules="emailRules"
                label="Email을 입력하세요"
                class="mt-5"
                required
              />

              <!-- 비밀번호 -->
              <v-text-field
                v-model="password"
                :rules="[() => password.length > 0 || 'This field is required']"
                label="Password을 입력하세요"
                class="mt-5"
                required
                type="password"
              />
            </v-card-text>

            <v-divider class="mt-5" />
            <v-card-actions>
              <v-spacer />
              <v-btn color="primary" @click="submit">Submit</v-btn>
            </v-card-actions>
          </v-card>
          <v-card>
            ////// 소셜 로그인 추가
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {
  data: () => {
    return {
      emailRules: [
        v => !!v || "E-mail is required",
        v =>
          /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
          "E-mail must be valid"
      ],

      email: "",
      password: ""
    };
  },
  methods:{
    submit() {
      // Axios를 통해 유효한 회원인지 판단

      
    }
  }
};
</script>

<style>
</style>