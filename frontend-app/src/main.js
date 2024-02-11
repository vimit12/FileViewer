import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/lib/components'
import * as directives from 'vuetify/lib/directives'

const vuetify = createVuetify({
    components,
    directives
})

createApp(App).use(router).use(vuetify).use(VueAxios, axios).mount('#app')
