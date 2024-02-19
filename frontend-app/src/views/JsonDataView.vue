<template>

    <div>
        <div>
            <v-data-table :headers="headersData" :items="jsonData" :items-per-page="itemPerPage" :sort-by="sortBy" :fixed-header="true" class="custom-table">  
                <template v-slot:top>
                    <v-toolbar flat v-bind:color="colorcode">
                        <v-toolbar-title>
                            <v-row>
                                <v-col cols="2" justify="end">
                                    <v-icon @click="go_back">mdi-backburger</v-icon>
                                    <v-icon @click="pick_color" :color="blue">mdi-palette</v-icon>
                                </v-col>
                                <v-col justify="end">
                                    {{ file_name }}
                                </v-col>
                            </v-row>  </v-toolbar-title>
                        <v-divider class="mx-4" inset vertical></v-divider>
                        <v-spacer></v-spacer>
                        <v-dialog v-model="dialog" max-width="500px">
                            <template v-slot:activator="{ props }">
                               
                                <v-btn light v-bind="props" @click="change_view()">
                                    Change View
                                </v-btn>
                                
                            </template>
                            
                        </v-dialog>
                        
                    </v-toolbar>
                </template>

                <template v-slot:item="{ item }">
                    <tr>
                        <td v-for="key in dynamicKeys" :key="key">
                            <template v-if="Array.isArray(item[key])">
                                <v-btn variant="tonal" prepend-icon="mdi-unfold-more-vertical" append-icon="mdi-dots-horizontal-circle-outline" @click="handleButtonClick(item[key], key)">view</v-btn>
                            </template>
                            <template v-else-if="typeof item[key] === 'object'">
                                <v-btn variant="tonal" prepend-icon="mdi-unfold-more-vertical" append-icon="mdi-dots-horizontal-circle-outline" @click="handleButtonClick(item[key], key)">View</v-btn>
                            </template>
                            <template v-else>{{ item[key] }}</template>
                        </td>
                    </tr>
                </template>
                <!-- eslint-disable -->
                <template v-slot:tfoot="{ item }">
                    <!-- Footer row with text fields -->
                    <tr>
                        <td v-for="key in dynamicKeys" :key="key">
                            <v-text-field v-model="searchText[key]"
                            @input="handleSearch(key, searchText[key])" hide-details :placeholder="`Search ${key}`" variant="underlined" clearable></v-text-field>
                        </td>
                    </tr>   

                    
                </template>
                <!-- eslint-enable -->
            </v-data-table>
        </div>

        <div>
            <v-row justify="space-around">

                <v-col cols="auto">
                  <v-dialog v-model="previewDialogVisible" transition="dialog-top-transition" width="auto">
                
                    <template v-slot:default="{ isActive }">
                      <v-card>
                        <v-toolbar v-bind:color="colorcode" >
                            <v-toolbar-title style="padding: 1em;">Data for column : {{ keyColumn }}   </v-toolbar-title>

                        </v-toolbar>
                        <v-card-text>
                          <div class="">
                                <v-table fixed-header v-if="columnArrayObj">
                                    <thead>
                                        <tr>
                                            <th v-for="header in recursiveHeadersData" :key="header" class="text-left" style="font-weight: 600;">{{ header }}</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                    <tr v-for="(item, index) in recursiveJsonData" :key="index">
                                        <td v-for="(value, key) in item" :key="key">{{ value }}</td>
                                    </tr>
                                    </tbody>
                                </v-table>

                                <v-table fixed-header v-if="columnArrayArr">
                                    
                                    <tbody>
                                    <tr v-for="value in recursiveJsonData" :key="value">
                                        <td >{{ value }}</td>
                                    </tr>
                                    </tbody>
                                </v-table>
                          </div>
                        </v-card-text>
                        <v-card-actions class="justify-end">
                          <v-btn variant="text" @click="isActive.value = false">Close</v-btn>
                        </v-card-actions>
                      </v-card>
                    </template>
                  </v-dialog>
                </v-col>

                
            </v-row>
        </div>

        <div>
            <v-dialog v-model="colorDialog" transition="dialog-top-transition" width="auto">
                
                        <template v-slot:default="{ isActive }">
                          <v-card>
                            <v-toolbar v-bind:color="colorcode" >
                                <v-toolbar-title style="padding: 1em;">Color Picker</v-toolbar-title>

                            </v-toolbar>
                            <v-card-text>
                              <div class="">
                                    <v-color-picker show-swatches v-model="colorcode"></v-color-picker>
                              </div>
                            </v-card-text>
                            <v-card-actions class="justify-end">
                                <!-- <v-btn variant="text" @click="handleColorPick">Pick</v-btn> -->
                              <v-btn variant="text" @click="isActive.value = false">Close</v-btn>
                            </v-card-actions>
                          </v-card>
                        </template>
                </v-dialog>
        </div>

        
    </div>
    
</template>

<script>


/* eslint-disable */
import axios from 'axios';
import { createToast } from "mosha-vue-toastify";
import {
    VDataTable,
    VDataTableServer,
    VDataTableVirtual,
} from "vuetify/components/VDataTable";

export default {
    name: 'JsonDataView',
    components: {
        VDataTable,
        VDataTableServer,
        VDataTableVirtual,
        
    },
    data() {
        return {
            colorDialog: false,
            colorcode: "black",
            itemPerPage:10,
            sortBy: null,
            columnArrayObj: false,
            columnArrayArr: false,
            previewDialogVisible:false,
            dialog: false,
            jsonEdit: false,
            dialogDelete: false,
            headersData: [],
            editedIndex: -1,
            editedItem: {
                name: '',
                calories: 0,
                fat: 0,
                carbs: 0,
                protein: 0,
            },
            defaultItem: {
                name: '',
                calories: 0,
                fat: 0,
                carbs: 0,
                protein: 0,
            },
            file_name : "",
            file_type: "",
            jsonData: null,
            keyColumn: null,
            searchText: {}
        }
    },
    computed: {
        dynamicKeys() {
            this.keys = Array()

            if (Array.isArray(this.rawJsonData)) {

                this.keys = Object.keys(this.rawJsonData[0]).map(head => (head));
            } else {
                this.keys  = Object.keys(this.rawJsonData).map(head => (head));
            }
            return this.keys
        }
    },
    watch: {
        dialog(val) {
            val || this.close()
        },
        dialogDelete(val) {
            val || this.closeDelete()
        },
    },
    mounted() {
        document.title = "View";
        // Change the icon
        this.newIcon = "mdi-new-icon";
    },
    beforeUnmount() {

    },
    methods: {
        pick_color(){
            this.colorDialog = true;
            
        }, 
        handleColorPick() {
            // Access the picked color from the 'colorcode' variable
            console.log('Picked Color:', this.colorcode);
            // You can perform any additional logic with the picked color here
        },
        searchByKey(array, key, searchText) {
            // Convert searchText to lowercase for case-insensitive search
            const search = searchText.toLowerCase();

            // Filter the array based on the key and searchText
            return array.filter(item => {
                // Convert item[key] to lowercase for case-insensitive search
                const value = String(item[key]).toLowerCase();
                // Check if the value contains the searchText
                return value.includes(search);
            });
        },
        handleSearch(key, text) {
            // Perform search/filtering based on the key and search text
            console.log(`Search for '${text}' in '${key}'`);
            // Implement your search logic here
            // Example usage
            this.data_prep(this.rawJsonData)
            // if (text == ""){
            //     console.log("CALL")
            //     this.data_prep(this.rawJsonData)
            // }
            
            this.filteredData = this.searchByKey(this.jsonData, key, text);
            if (this.filteredData){
                this.jsonData = this.filteredData;
            } else {
                this.jsonData = []
            }
            console.log(this.jsonData);

        },
        go_back() {
            this.$router.push(
                {
                    name: 'home'
                })
        },
        change_view(){
            this.$router.push(
                {
                    name: 'jsonedit',
                    query:
                    {
                        data: this.rawJsonData,
                        file_name: this.file_name,
                        file_type: this.file_type
                    }
                })
        },
        identifyArrayType(arr) {
            if (!Array.isArray(arr)) {
                return "Not an array";
            }

            // Check if array of arrays
            if (arr.every(innerArr => Array.isArray(innerArr))) {
                return "Array of arrays";
            }

            // Check if array of objects
            if (arr.every(innerArr => typeof innerArr === 'object' && innerArr !== null && !Array.isArray(innerArr))) {
                return "Array of objects";
            }

            // Check if array of strings
            if (arr.every(item => typeof item === 'string')) {
                return "Array of strings";
            }

            // Check if array of numbers
            if (arr.every(item => typeof item === 'number')) {
                return "Array of numbers";
            }

            // Check if array of booleans
            if (arr.every(item => typeof item === 'boolean')) {
                return "Array of booleans";
            }

            // If none of the above, return "Mixed array"
            return "Mixed array";
        },

        columnDataPopulate(arr) {
            if (Array.isArray(arr) && arr.length > 0) {
                // Check if arr is an array of objects
                if (typeof arr[0] === 'object' && arr[0] !== null) {
                    this.recursiveHeadersData = Object.keys(arr[0]);
                    // this.recursiveJsonData = arr;
                } else {
                    // Treat arr as a single object
                    this.recursiveHeadersData = Object.keys(arr);
                    // this.recursiveJsonData = [arr];
                }
            } else {
                // Handle case when arr is empty or not an array
                this.recursiveHeadersData = [];
                // this.recursiveJsonData = [];
            }
            return this.recursiveHeadersData;
        },

        handleButtonClick(columnArray, key) {
            this.keyColumn = key;
            this.previewDialogVisible = true
            // Access and process the array data here

            console.log(columnArray, key)
            let type_of_array = this.identifyArrayType(columnArray)
            console.log(type_of_array)
            if (type_of_array == 'Array of objects'){
                this.recursiveJsonData = columnArray
                this.recursiveHeadersData = this.columnDataPopulate(columnArray)
                this.columnArrayObj = true
                console.log("Clicked on people array:", this.recursiveJsonData, this.recursiveJsonData);
            } else {
                this.recursiveJsonData = columnArray
                this.columnArrayArr = true
            }
            
        },
        data_prep(data){
            
            this.jsonData = data
            this.previewDialogVisible = false
            if (Array.isArray(this.jsonData)) {
                
                this.headersData = Object.keys(this.jsonData[0]).map(head => ({
                    title: head,
                    align: 'start',
                    sortable: true,
                    key: head,
                }));
                
            } else {
                this.headersData = Object.keys(this.jsonData).map(head => ({
                    title: head,
                    align: 'start',
                    sortable: true,
                    key: head,
                }));
                this.jsonData = Array(this.jsonData)
            }
            // this.headersData.push({ title: 'Actions', align: "end", sortable: false, key: 'actions' },)
            //[{ key: 'calories', order: 'asc' }]
            this.sortBy = [{ key: Object.keys(this.jsonData[0])[0], order: 'asc' }]

            console.log(this.jsonData)
        },

        editItem(item) {
            this.editedIndex = this.desserts.indexOf(item)
            this.editedItem = Object.assign({}, item)
            this.dialog = true
        },

        deleteItem(item) {
            this.editedIndex = this.desserts.indexOf(item)
            this.editedItem = Object.assign({}, item)
            this.dialogDelete = true
        },

        deleteItemConfirm() {
            this.desserts.splice(this.editedIndex, 1)
            this.closeDelete()
        },

        close() {
            this.dialog = false
            this.$nextTick(() => {
                this.editedItem = Object.assign({}, this.defaultItem)
                this.editedIndex = -1
            })
        },

        closeDelete() {
            this.dialogDelete = false
            this.$nextTick(() => {
                this.editedItem = Object.assign({}, this.defaultItem)
                this.editedIndex = -1
            })
        },

        save() {
            if (this.editedIndex > -1) {
                Object.assign(this.desserts[this.editedIndex], this.editedItem)
            } else {
                this.desserts.push(this.editedItem)
            }
            this.close()
        },
    

    },
    created() {

        localStorage.setItem('jsonData', this.$route.query.data);

        this.rawJsonData = JSON.parse(this.$route.query.data);

        // this.jsonData = this.rawJsonData
        this.file_name = this.$route.query.file_name;
        this.file_type = this.$route.query.file_type;
        this.data_prep(this.rawJsonData)

    }
}
</script>

<style>
    span {
        font-weight: 600;
    }

    .custom-table {
    border-collapse: collapse;
    width: 100%;
    }

    .custom-table th,
    .custom-table td {
    border: 1px solid #dddddd;
    padding: 8px;
    text-align: left;
    }

    /* Define column widths */
    .custom-table th:nth-child(1),
    .custom-table td:nth-child(1) {
    width: 20%;
    }

    .custom-table th:nth-child(2),
    .custom-table td:nth-child(2) {
    width: 30%;
    }
</style>
