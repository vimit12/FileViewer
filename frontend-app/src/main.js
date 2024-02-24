import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import '@mdi/font/css/materialdesignicons.min.css';
import ToastPlugin from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-bootstrap.css';



// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

// import JsonEditor from 'vue-json-edit'


const vuetify = createVuetify({
    components,
    directives,
})

createApp(App).use(router).use(vuetify).use(VueAxios, axios).use(ToastPlugin).mount('#app')
