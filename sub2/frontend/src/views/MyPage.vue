<template>
  <div>
    <v-col cols="12" sm="4" order="-1" order-sm="2">
      <v-card min-height="300" min-width="150" elevation="0">
        <v-row class="pa-3">
          <!-- profile img -->
          <v-col offset="3" cols="20" class="center">
            <v-avatar size="200">
              <v-img class="card-img" src="https://cdn.vuetifyjs.com/images/john.jpg" />
            </v-avatar>
          </v-col>
          <!-- END : profile img -->
          <v-col offset="1" cols="10" class="background">
            <v-row>
              <v-col>
                <!------------------ PROFILE DATA ------------------>
                <div class="text-center mb-3 title text-secundario font-weight-bold">
                  <span>@</span>
                  {{ userInfo.profile.name }}
                </div>
                <div class="text-center mb-3">
                  <v-icon>{{ mdiEmail }}</v-icon>
                  <span>{{ userInfo.email }}</span>
                </div>
                <div class="text-center mb-3">
                  <v-icon>{{ mdiMapMarker }}</v-icon>
                  <span>{{ userInfo.profile.address }}</span>
                </div>
                <div class="text-center mb-3">
                  <v-icon>{{ mdiCellphoneIphone }}</v-icon>
                  <span>{{ userInfo.profile.phone }}</span>
                </div>
                <div class="text-center">
                  <v-icon>{{ mdiCalendar }}</v-icon>
                  <span>{{ userInfo.profile.born_year }}</span>
                </div>
                <!------------------ END PROFILE DATA ------------------>
                <div class="text-center mt-5">
                  <v-btn color="#32BCC3" to="/edituser" elevation="0" dark>
                    <v-icon left>{{ mdiPencil }}</v-icon>Edit Profile
                  </v-btn>
                  <v-btn color="#32BCC3" to="/editpw" elevation="0" dark>
                    <v-icon left>{{ mdiLockCheck }}</v-icon> Edit Password
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
import {
  mdiCalendar,
  mdiPencil,
  mdiMapMarker,
  mdiCellphoneIphone,
  mdiEmail,
  mdiLockCheck
} from "@mdi/js";

export default {
  data: () => ({
    mdiCalendar,
    mdiPencil,
    mdiMapMarker,
    mdiCellphoneIphone,
    mdiEmail,
    mdiLockCheck
  }),
  computed: {
    userInfo: function(){
      return this.$store.getters['data/userInfo']
    }
  },
  created() {
    this.$store.dispatch('data/userInfo', sessionStorage.getItem('pk'))
  },

  methods: {}
};
</script>

<style>
</style>