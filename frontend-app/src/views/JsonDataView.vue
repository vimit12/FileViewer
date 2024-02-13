<template>

    <div>
        <div>
            <!-- <v-data-table :headers="headersData" :items="jsonData" :sort-by="[{ key: 'calories', order: 'asc' }]"> -->
            <v-data-table :headers="headersData" :items="jsonData" >
                

                
                <template v-slot:top>
                    <v-toolbar flat color="black">
                        <v-toolbar-title> {{file_name}} </v-toolbar-title>
                        <v-divider class="mx-4" inset vertical></v-divider>
                        <v-spacer></v-spacer>
                        <v-dialog v-model="dialog" max-width="500px">
                            <template v-slot:activator="{ props }">
                                <v-btn color="primary" dark class="mb-2" v-bind="props">
                                    New Item
                                </v-btn>
                            </template>
                            <v-card>
                                <v-card-title>
                                    <span class="text-h5">{{ formTitle }}</span>
                                </v-card-title>

                                <v-card-text>
                                    <v-container>
                                        <v-row>
                                            <v-col cols="12" sm="6" md="4">
                                                <v-text-field v-model="editedItem.name" label="Dessert name"></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="4">
                                                <v-text-field v-model="editedItem.calories" label="Calories"></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="4">
                                                <v-text-field v-model="editedItem.fat" label="Fat (g)"></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="4">
                                                <v-text-field v-model="editedItem.carbs" label="Carbs (g)"></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="4">
                                                <v-text-field v-model="editedItem.protein" label="Protein (g)"></v-text-field>
                                            </v-col>
                                        </v-row>
                                    </v-container>
                                </v-card-text>

                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn color="blue-darken-1" variant="text" @click="close">
                                        Cancel
                                    </v-btn>
                                    <v-btn color="blue-darken-1" variant="text" @click="save">
                                        Save
                                    </v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                        <v-dialog v-model="dialogDelete" max-width="500px">
                            <v-card>
                                <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn color="blue-darken-1" variant="text" @click="closeDelete">Cancel</v-btn>
                                    <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">OK</v-btn>
                                    <v-spacer></v-spacer>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                    </v-toolbar>
                </template>

                <template v-slot:item="{ item }">
                <tr>
                    <td v-for="key in dynamicKeys" :key="key">
                        <template v-if="Array.isArray(item[key])">
                        
                            <v-btn variant="tonal" prepend-icon="mdi-unfold-more-vertical" append-icon="mdi-dots-horizontal-circle-outline" @click="handleButtonClick(item[key], key)">view</v-btn>
                        </template>

                        <template v-else>{{ item[key] }}</template>
                    </td>
                </tr>
                </template>
                
                
                
                <!-- <template v-slot:[`item.actions`]="{ item }">
                    
                    <v-icon size="small" class="me-2" @click="editItem(item)">
                        mdi-pencil
                    </v-icon>
                    <v-icon size="small" @click="deleteItem(item)">
                        mdi-delete
                    </v-icon>
                </template> -->

                
            </v-data-table>
        </div>

        <div>
            <v-row justify="space-around">

                <v-col cols="auto">
                  <v-dialog v-model="previewDialogVisible" transition="dialog-top-transition" width="auto">
                
                    <template v-slot:default="{ isActive }">
                      <v-card>
                        <v-toolbar color="black" >
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
            columnArrayObj: false,
            columnArrayArr: false,
            previewDialogVisible:false,
            dialog: false,
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
            keyColumn: null
        }
    },
    computed: {
        formTitle() {
            return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
        },
        dynamicKeys() {
            this.keys = Array()

            if (Array.isArray(this.jsonData)) {

                this.keys = Object.keys(this.jsonData[0]).map(head => (head));
            } else {
                this.keys  = Object.keys(this.jsonData).map(head => (head));
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
    },
    beforeUnmount() {

    },
    methods: {
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
        data_prep(){
            this.previewDialogVisible = false
            if (Array.isArray(this.jsonData)) {
                
                this.headersData = Object.keys(this.jsonData[0]).map(head => ({
                    title: head,
                    align: 'start',
                    sortable: false,
                    key: head,
                }));
            } else {
                this.headersData = Object.keys(this.jsonData).map(head => ({
                    title: head,
                    align: 'start',
                    sortable: false,
                    key: head,
                }));
                this.jsonData = Array(this.jsonData)
            }
            // this.headersData.push({ title: 'Actions', align: "end", sortable: false, key: 'actions' },)


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

        this.jsonData = JSON.parse(this.$route.query.data);
        this.file_name = this.$route.query.file_name;
        this.file_type = this.$route.query.file_type;
        this.data_prep()

    }
}
</script>

<style>
span {
    font-weight: 600;
}
</style>
