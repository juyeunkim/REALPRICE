<template>
  <div>
    sdafsdffs
    <v-row class="pa-3">
      <v-col offset="1" cols="10" class="center relative">
        <v-avatar size="200">
          <v-img class="card-img" src="https://cdn.vuetifyjs.com/images/john.jpg"/>
        </v-avatar>

        <!------------------ EDIT IMAGE BUTTON ------------------>
        <!-- <div v-if="isAuthenticated && userCredentials.handle === data.handle">
          <input type="file" id="imageInput" hidden @change="handleImageChange" />
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn
                class="mx-2"
                fab
                small
                color="#32BCC3"
                absolute
                right
                bottom
                @click="editImage"
                v-on="on"
                dark
              >
                <v-icon dark>{{svg.camera}}</v-icon>
              </v-btn>
            </template>
            <span>Edit Profile Image</span>
          </v-tooltip>
        </div> -->
        <!------------------ EDIT IMAGE BUTTON ------------------>
      </v-col>
      <v-col offset="1" cols="10" class="background">
        <v-row>
          <v-col>
            <!------------------ PROFILE DATA ------------------>
            <div class="text-center mb-3 title text-secundario font-weight-bold">
              <span>@</span>
              이름
            </div>
            <!-- <div v-if="data.bio" class="text-center mb-3 pr-5 pl-5 font-weight-regular">{{data.bio}}</div> -->
            <div v-if="data.location" class="text-center mb-3">
              <v-icon>{{svg.location}}</v-icon>
              <span>주소</span>
            </div>
            <div class="text-center">
              <v-icon>{{svg.calendar}}</v-icon>
              <span>생년월일</span>
            </div>
            <!------------------ END PROFILE DATA ------------------>
            <div class="mt-5">
              ////// 수정 버튼
              <AppEditProfile :data="data"></AppEditProfile>
            </div>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>
<script>
// COMPONENTS
import AppEditProfile from "@/components/Profile/AppEditProfile.vue";
// SVG ICONS
import {
  mdiMapMarker,
  mdiWeb,
  mdiCalendar,
  mdiPencil,
  mdiCameraRetakeOutline
} from "@mdi/js";
// VUEX
import { mapGetters } from "vuex";
export default {
  components: {
    AppEditProfile
  },
  props: {
    data: {
      type: Object
    }
  },
  data: () => ({
    name:'profile',
    svg: {
      location: mdiMapMarker,
      web: mdiWeb,
      calendar: mdiCalendar,
      pencil: mdiPencil,
      camera: mdiCameraRetakeOutline
    },
  }),
  methods: {
    // handleImageChange(event) {
    //   const image = event.target.files[0];
    //   const formData = new FormData();
    //   formData.append("image", image, image.name);
    //   this.$store.dispatch("UPLOAD_IMAGE", formData);
    // },
    // editImage() {
    //   const imageInput = document.getElementById("imageInput");
    //   imageInput.click();
    // }
  },
  computed: {
    // ...mapGetters(["isAuthenticated", "userCredentials"])
  }
};
</script>