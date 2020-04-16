<template>
  <v-col cols="12" sm="4" order="-1" order-sm="2">
    <v-card min-height="300" min-width="150" elevation="0">
      <v-col offset="3" cols="20" class="center">
        <v-avatar size="50">
          <v-img class="card-img" src="https://cdn.vuetifyjs.com/images/john.jpg" />
        </v-avatar>
      </v-col>
      <v-col offset="1" cols="10" class="background">
        <v-row>
          <v-col>
            <!------------------ PROFILE DATA ------------------>
            <div class="text-center mb-3 title text-secundario font-weight-bold">
              <span>{{ user }}</span>
            </div>
          </v-col>
        </v-row>
      </v-col>
    </v-card>
    <!-- TODO : 자기 자신일때만 search 버튼이 나오도록 -->
    <SEARCH />
  </v-col>
</template>

<script>
import SEARCH from "@/components/realprice/Search";
export default {
  components: {
    SEARCH
  },
  props: {
    user: String
  }
};
</script>

<style>
</style>