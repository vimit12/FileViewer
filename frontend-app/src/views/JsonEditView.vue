<template>
        
    <div>
            <!-- <div id="jsoneditor" style="width: 400px; height: 400px;"></div> -->
            <json-editor dataInput="jsonData"></json-editor>
    </div>
</template>

<script>


/* eslint-disable */
import axios from 'axios';
import { createToast } from "mosha-vue-toastify";


// import { JSONEditor } from '@kassaila/vue-json-editor'
import JsonEditor from '@kassaila/vue-json-editor/src/components/json-editor.vue';


export default {
    name: 'JsonEditView',
    components: {
        // JSONEditor
        JsonEditor
    },
    data() {
        return {
            json: {
                "name": "Vimit"
            }
        }
    },
    computed: {
        
    },
    watch: {
       
    },
    mounted() {
    },
    beforeUnmount() {

    },
    methods: {

        
    },
    created() {
        this.jsonData = JSON.parse(localStorage.getItem('jsonData'));

        

    }
}
</script>

<style>

</style>
