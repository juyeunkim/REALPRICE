<template>
  <div>
    <v-container fluid>
      <v-layout row>
        <v-flex xs12 md6 offset-md3>
          <v-card>
            <v-toolbar color="indigo" dark>
              <v-toolbar-title>회원정보 수정</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <span class="title">Personal Info</span>

              <!-- 이메일 수정 불가능 -->
              <v-text-field
                v-model="userInfo.email"
                class="mt-5"
                label="Email"
                required
                readonly
                disabled
              />

              <!-- 이름 -->
              <v-text-field
                v-model="userInfo.profile.name"
                :rules="nameRules"
                label="Name"
                class="mt-5"
                required
                @keyup.enter="submit"
              />

              <!-- 휴대폰 번호 -->
              <v-text-field
                v-model="userInfo.profile.phone"
                :rules="phoneRules"
                label="휴대폰"
                class="mt-5"
                required
                @keyup.enter="submit"
              />

              <!-- 주소 -->
              <v-text-field
                v-model="userInfo.profile.address"
                :rules="[() => userInfo.profile.address.length > 0 || 'This field is required']"
                label="주소"
                class="mt-5"
                required
                @keyup.enter="submit"
              />

              <!-- 취향 -->
              <v-combobox
                v-model="tags"
                :items="items"
                hide-selected
                hint="리스트에 없다면 추가해주세요"
                label="싫어하는 음식(재료)를 선택해주세요"
                multiple
                persistent-hint
                small-chips
              >
                <template v-slot:no-data>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title>
                        음식을 추가하고
                        <kbd>enter</kbd> 를 눌러주세요
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </template>
              </v-combobox>
            </v-card-text>

            <v-divider class="mt-5" />
            <v-card-actions>
              <!-- <v-btn flat>Cancel</v-btn> -->
              <v-spacer />
              <v-btn color="primary" to="/mypage">취소</v-btn>
              <v-btn color="primary" @click="submit">수정</v-btn>
              <v-btn color="primary" @click="secession">삭제</v-btn>
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
    items: ["오이", "고수", "민트"],
    tags: [],

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
    this.tags = this.userInfo.profile.tag.split(",");
  },
  methods: {
    submit() {
      console.log(this.userInfo);
      if (
        this.userInfo.profile.name != "" &&
        this.userInfo.profile.phone != ""
      ) {
        this.userInfo.profile.tag = this.tags.toString();
        console.log(this.userInfo);
        var data = {
          email: this.userInfo.email,
          password: "string",
          profile: {
            address: this.userInfo.profile.address,
            born_year: this.userInfo.profile.born_year,
            gender: this.userInfo.profile.gender,
            name: this.userInfo.profile.name,
            phone: this.userInfo.profile.phone,
            tag: this.userInfo.profile.tag
          }
        };
        api
          .updateUser(sessionStorage.getItem("pk"), data)
          .then(res => {
            console.log(res);
            this.$alert("정보수정 성공", "Success", "success");
            this.$router.push("/mypage");
          })
          .catch(exp => {
            console.log(exp);
            this.$alert("정보수정 실패", "Warning", "warning");
          });
      } else {
        this.$alert("항목을 모두 입력해주세요", "Warning", "warning");
      }
    },
    secession() {
      // alert로 정말 탈퇴할건지 묻고, 맞으면 탈퇴
      this.$confirm("정말 탈퇴하시겠습니까?").then(() => {
        api.deleteUser(sessionStorage.getItem("pk"));
        this.$alert("삭제 완료", "Success", "success");
        sessionStorage.clear();
        this.$router.push("/");
      });
    }
  }
};
</script>

<style>
</style>