<template>
        
    <div>
            <!-- <div id="jsoneditor" style="width: 400px; height: 400px;"></div>
            <json-editor dataInput="jsonData"></json-editor> -->
                
            <div id="editorjs"> </div>
    </div>
</template>

<script>


/* eslint-disable */
import axios from 'axios';
import { createToast } from "mosha-vue-toastify";


// import { JSONEditor } from '@kassaila/vue-json-editor'
// import JsonEditor from '@kassaila/vue-json-editor/src/components/json-editor.vue';
import { EditorJS } from '@editorjs/editorjs'


export default {
    name: 'JsonEditView',
    components: {
        EditorJS
    },
    data() {
        return {
            
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
        // this.jsonData = JSON.parse(localStorage.getItem('jsonData'));

        this.rawJsonData = JSON.parse(this.$route.query.data);

        // this.jsonData = this.rawJsonData
        this.file_name = this.$route.query.file_name;
        this.file_type = this.$route.query.file_type;
        alert(JSON.stringify(this.rawJsonData))

    }
}
</script>

<style>

</style>
