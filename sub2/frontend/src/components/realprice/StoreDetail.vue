<template>
  <div class="storeDetail">
      <v-card>
            <v-card-title class="headline">Use Google's location service?</v-card-title>

            <v-card-text>
              Let Google help apps determine location. This means sending anonymous location data to Google, even when no apps are running.
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn
                color="green darken-1"
                text
                @click="emitClose"
              >
                Disagree
              </v-btn>

              <v-btn
                color="green darken-1"
                text
                @click="emitClose"
              >
                Agree
              </v-btn>
            </v-card-actions>
          </v-card>
  </div>
</template>

<script>
export default {
    methods: {
        emitClose: function () {
            this.$emit('close')
        }
    },
}
</script>

<style>

</style>