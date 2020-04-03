<template>
  <div>
    <v-col cols="12" sm="4" order="-1" order-sm="2">
      <v-card min-height="300" min-width="150" elevation="0">
        <v-row class="pa-3">
          <v-col offset="3" cols="20" class="center">
            <v-avatar size="200">
              <v-img class="card-img" src="https://cdn.vuetifyjs.com/images/john.jpg" />
            </v-avatar>
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
                <div class="text-center mb-3">
                  <v-icon>{{svg.location}}</v-icon>
                  <span>주소</span>
                </div>
                <div class="text-center">
                  <v-icon>{{svg.calendar}}</v-icon>
                  <span>생년월일</span>
                </div>
                <!------------------ END PROFILE DATA ------------------>
                <div class="mt-5">
                  <v-btn color="#32BCC3" to="/edituser" elevation="0" dark>
                    <v-icon left>{{svg.pencil}}</v-icon>Edit Profile
                  </v-btn>
                </div>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-card>
    </v-col>
  </div>
</template>

<script>
// import Profile from "../components/profile/Profile.vue";
import {
  mdiMapMarker,
  mdiWeb,
  mdiCalendar,
  mdiPencil,
  mdiCameraRetakeOutline
} from "@mdi/js";

export default {
  components: {
    // Profile
  },
  data: () => {
    return {
      svg: {
        location: mdiMapMarker,
        web: mdiWeb,
        calendar: mdiCalendar,
        pencil: mdiPencil,
        camera: mdiCameraRetakeOutline
      }
    };
  },

  methods: {}
};
</script>

<style>
</style>