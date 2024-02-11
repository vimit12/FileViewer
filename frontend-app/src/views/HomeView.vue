<template>
    <div class="text-center">
        <v-btn
          color="success"
          @click="dialog = true"
        >
          Open Dialog
        </v-btn>

        <v-dialog
          v-model="dialog"
          width="auto"
        >
          <v-card>
            <v-card-text>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </v-card-text>
            <v-card-actions>
              <v-btn color="success" block @click="dialog = false">Close Dialog</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
</template>

<script>
export default {
    name: 'HomeView',
    components: {
        
    },
    data() {
        return {
            dialog: false,
        }
    },
    mounted() {
        
    },
    beforeUnmount() {
        
    },
    methods: {
        
    }
}
</script>

<style>
/* Add your scoped styles here */
</style>
