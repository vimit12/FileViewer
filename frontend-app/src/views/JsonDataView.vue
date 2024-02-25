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
                        <v-dialog v-model="dialog" persistent width="auto">
                            <template v-slot:activator="{ props }">
                               
                                <v-btn light v-bind="props" @click="change_view()">
                                    Export Data
                                </v-btn>
                                <v-btn light v-bind="props" @click="dialog = true">
                                    Add New
                                </v-btn>
                                
                            </template>


                            <v-card>
                                
                                <v-card-title v-bind:color="colorcode">
                                    <span class="text-h5">{{ formTitle }}</span>
                                    <v-divider></v-divider>
                                </v-card-title>

                                <v-card-text>
                                    <v-container>
                                        <v-row>
                                            <v-col  cols="12" sm="6" md="4" v-for="key in dynamicKeys" :key="key" >
                                                <v-textarea v-if="key !== 'Action'" clearable :label="key" prepend-icon="mdi-ruler-square-compass" variant="outlined" v-model="formData[key]"></v-textarea>
                                            </v-col>
                                        </v-row>
                                    </v-container>
                                </v-card-text>

                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn color="blue-darken-1" variant="text" @click="close">Cancel</v-btn>
                                    <v-btn color="blue-darken-1" variant="text" @click="save()">Save</v-btn>
                                </v-card-actions>
                            </v-card>
                            
   
                        </v-dialog>
                        
                    </v-toolbar>
                </template>

                <template v-slot:item="{ item }">
                    
                    <tr>
                        <td v-for="key in dynamicKeys" :key="key">
                            <template v-if="Array.isArray(item[key]) && item[key].length !== 0">
                                <v-btn variant="tonal" prepend-icon="mdi-unfold-more-vertical" append-icon="mdi-dots-horizontal-circle-outline" @click="handleButtonClick(item[key], key)">view</v-btn>
                            </template>
                            <template v-else-if="typeof item[key] === 'object' && Object.keys(item[key]).length === 0">
                                    {{ item[key] }}
                            </template>
                            <template v-else-if="Array.isArray(item[key]) && item[key].length === 0">
                                {{ item[key] }}
                            </template>
                            <template v-else-if="typeof item[key] === 'object'">
                                <v-btn variant="tonal" prepend-icon="mdi-unfold-more-vertical" append-icon="mdi-dots-horizontal-circle-outline" @click="handleButtonClick(item[key], key)">View</v-btn>
                            </template>
                            
                            <template v-else>{{ item[key] }}</template>
                                <v-icon size="small" class="me-2" @click="editItem(item)" v-if="key=='Action'">mdi-pencil</v-icon>
                                <v-icon size="small" class="me-2" @click="deleteItem(item)" v-if="key == 'Action'">mdi-delete</v-icon>
                        </td>
                    </tr>

                    
                </template>

                

                <!-- eslint-disable -->
                <template v-slot:tfoot="{ item }">
                    <!-- Footer row with text fields -->
                    <tr>
                        <td v-for="key in dynamicKeys" :key="key">
                            <v-text-field v-model="searchText[key]" v-if="key != 'Action'"
                            @input="handleSearch(key, searchText[key])" hide-details :placeholder="`Search ${key}`" variant="underlined" clearable></v-text-field>
                        </td>
                    </tr>   

                    
                </template>
                <!-- eslint-enable -->
            </v-data-table>
        </div>

        <div>
            <!-- This section is to view recursive data -->
            <v-row justify="space-around">

                <v-col cols="auto">
                  <v-dialog v-model="previewDialogVisible" transition="dialog-top-transition" width="auto">
                
                    <template v-slot:default="{ isActive }">
                      <v-card>
                        <v-toolbar v-bind:color="colorcode" >
                            <v-row>
                                <v-col cols="8">
                                    <v-toolbar-title style="padding: 2em;">Data for column : {{ keyColumn }}   </v-toolbar-title>
                                </v-col>

                            </v-row>
                            

                        </v-toolbar>
                        <v-card-text>
                          <div class="">

                                <v-data-table v-if="columnArrayObj" :headers="recursiveHeadersData" :items="recursiveJsonData" :items-per-page="itemPerPageRec" :sort-by="sortColumnDataBy" :fixed-header="true" class="custom-table">  
                                        
                                </v-data-table>

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
            <!-- This section is for Color Picket -->
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

        <div>
            <!-- This section is for Edit JSON Object -->
            <v-row justify="center">
                <v-dialog
                v-model="jsonEditdialog"
                persistent
                width="1024"
                >
                
                <v-card>
                    <v-card-title>
                    <span class="text-h5">Edit Item</span>
                    </v-card-title>
                    <v-card-text>
                    <v-container>
                        <v-textarea
                            v-model="jsonEditPerData"
                            label="JSON Data"
                            prepend-icon="mdi-json"
                            solo-inverted
                            rows="10"
                        ></v-textarea>
                    </v-container>
                    
                    </v-card-text>
                    <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue-darken-1" variant="text" @click="jsonEditdialog = false">Close</v-btn>
                    <v-btn color="blue-darken-1" variant="text" @click="saveEditJson">Save</v-btn>
                    </v-card-actions>
                </v-card>
                </v-dialog>
            </v-row>

        </div>

        <div>
            <!-- This section is for Delete Object Dailog box -->
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
        </div>

        <div id="toast"><v-icon id="img">{{ iconImage }}</v-icon><div id="desc"></div></div>
        
    </div>
    
</template>

<script>


/* eslint-disable */
import axios from 'axios';
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
            iconImage: "",
            colorDialog: false,
            colorcode: "black",
            itemPerPage:10,
            itemPerPageRec:3,
            sortBy: null,
            sortColumnDataBy: null,
            columnArrayObj: false,
            columnArrayArr: false,
            previewDialogVisible:false,
            dialog: false,
            jsonEditdialog:false,
            jsonEdit: false,
            dialogDelete: false,
            // formTitle: "New Item",
            headersData: [],
            editedIndex: -1,
            editedItem: {},
            defaultItem: {},
            file_name : "",
            file_type: "",
            jsonData: null,
            keyColumn: null,
            searchText: {},
            filteredData: [],
            formData: {},
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
            this.keys.push("Action")
            return this.keys
        },
        formTitle() {
            return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
        },
    },
    watch: {
        dialog(val) {
            val || this.close()
        },
        dialogDelete(val) {
            val || this.closeDelete()
        }
    },
    mounted() {
        document.title = "View";
        // Change the icon
        this.newIcon = "mdi-new-icon";
    },
    beforeUnmount() {

    },
    methods: {
        handleInputChange() {
            console.log('Input value changed:', this.searchInputValue);
            // Call your function here

            this.call_search(this.recursiveJsonData, this.searchInputValue)
            
        },
        call_search(data, input_value) {

            const requestBody = {
                "input_value": input_value,
                "data_search": data
            }

            axios.post(`${process.env.BASE_API_URL}search_data/`, requestBody)
                .then(response => {
                    // Handle API response data
                    var resp = response.data;
                    if (resp.status_code == 200) {
                        // this.filteredData = resp.data
                        this.handleButtonClick(resp.data, this.keyColumn)
                    } else {
                        createToast(JSON.stringify(resp.error),
                            {
                                showIcon: 'true',
                                hideProgressBar: 'false',
                                type: 'danger',
                                showCloseButton: 'true',
                                transition: 'slide',
                                position: 'bottom-center',
                            })
                    }
                })
                .catch(error => {
                    // Handle API error
                    createToast(JSON.stringify(error),
                        {
                            showIcon: 'true',
                            hideProgressBar: 'false',
                            type: 'danger',
                            showCloseButton: 'true',
                            transition: 'slide',
                            position: 'bottom-center',
                        })
                });
        },
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
                } else {
                    // Treat arr as a single object
                    this.recursiveHeadersData = Object.keys(arr);
                }
            } else {
                // Handle case when arr is empty or not an array
                this.recursiveHeadersData = [];
            }
            return this.recursiveHeadersData;
        },
        recursive_data_prep(data) {

            this.recursiveJsonData = data
            if (Array.isArray(this.recursiveJsonData)) {

                this.recursiveHeadersData = Object.keys(this.recursiveJsonData[0]).map(head => ({
                    title: head,
                    align: 'start',
                    sortable: true,
                    key: head,
                }));

            } else {
                this.recursiveHeadersData = Object.keys(this.recursiveJsonData).map(head => ({
                    title: head,
                    align: 'start',
                    sortable: true,
                    key: head,
                }));
                this.recursiveJsonData = Array(this.recursiveJsonData)
            }

            this.sortColumnDataBy = [{ key: Object.keys(this.recursiveJsonData[0])[0], order: 'asc' }]

        },
        handleButtonClick(columnArray, key) {
            this.keyColumn = key
            this.previewDialogVisible = true
            // Access and process the array data here

            let type_of_array = this.identifyArrayType(columnArray)
            console.log(type_of_array)

            if (type_of_array == 'Not an array' && (typeof columnArray == "object") && columnArray){
                this.recursive_data_prep(Array(columnArray))
                this.columnArrayObj = true
                this.columnArrayArr = false
                return
            }

            if (type_of_array == 'Array of objects'){
                // this.recursiveJsonData = columnArray
                // this.recursiveHeadersData = this.columnDataPopulate(columnArray)
                this.recursive_data_prep(columnArray)
                this.columnArrayObj = true
                this.columnArrayArr = false
            } else {
                this.recursiveJsonData = columnArray
                this.columnArrayArr = true
            }

            console.log(this.recursiveJsonData)
            console.log(this.recursiveHeadersData)
            
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
            this.headersData.push({ title: 'Actions', key: 'actions', sortable: false },)
            this.sortBy = [{ key: Object.keys(this.jsonData[0])[0], order: 'asc' }]

        },

        editItem(item) {
            this.jsonEditdialog = true
            this.jsonEditPerData = JSON.stringify(item, null, 4);
            this.editedIndex = this.findIndex(this.rawJsonData, item)
            
        },
        findIndex(array, item) {
            for (let i = 0; i < array.length; i++) {
                if (JSON.stringify(array[i]) === JSON.stringify(item)) {
                    return i;
                }
            }
            return -1; // Return -1 if item is not found
        },
        saveEditJson(){
            
            this.editedItem = Object.assign({}, JSON.parse(this.jsonEditPerData))
            console.log(this.editedItem)
            
            if (this.editedIndex != -1){
                this.rawJsonData[this.editedIndex] = this.editedItem;
                this.data_prep(this.rawJsonData)
                this.iconImage = "mdi-check-bold"
                this.launch_toast("The following item as been updated.", "#07d90e", "#07d90e")
                
            } else {
                
            }
            this.jsonEditdialog = false
        },

        deleteItem(item) {
            this.deletedIndex = this.findIndex(this.rawJsonData, item)
            this.deleteItemData = Object.assign({}, item)
            this.dialogDelete = true
        },

        deleteItemConfirm() {
            this.jsonData.splice(this.deletedIndex, 1)
            this.iconImage = "mdi-delete"
            this.launch_toast("The following item as been deletd.", "#fc1c03", "#fc1c03")
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
            console.log("Form Data:", this.formData);
            this.jsonData.push(this.formData);
            this.close()
        },
        launch_toast(msg, toastColor, iconColor) {
            var x = document.getElementById("toast")
            x.className = "show";
            x.style.backgroundColor = toastColor;
            
            var div = document.getElementById("desc")
            div.innerHTML = msg
            
            
            var imgIcon = document.getElementById("img")
            imgIcon.style.backgroundColor = iconColor;
            setTimeout(function () { x.className = x.className.replace("show", ""); }, 5000);
        }

    },
    created() {

        localStorage.setItem('jsonData', this.$route.query.data);

        this.rawJsonData = JSON.parse(this.$route.query.data);
        console.log(this.rawJsonData)
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

    #toast {
    visibility: hidden;
    max-width: 50px;
    height: 50px;
    /*margin-left: -125px;*/
    margin: auto;
    background-color: #333;
    color: #231f1f;
    text-align: center;
    border-radius: 2px;

    position: fixed;
    z-index: 1;
    left: 0;right:0;
    bottom: 30px;
    font-size: 17px;
    white-space: nowrap;
}
#toast #img{
	width: 50px;
	height: 50px;
    
    float: left;
    
    padding-top: 16px;
    padding-bottom: 16px;
    
    box-sizing: border-box;

    
    /* background-color: #111; */
    color: #1b1919;
}
#toast #desc{

    
    color: #1d1c1c;
   
    padding: 16px;
    
    overflow: hidden;
	white-space: nowrap;
}

#toast.show {
    visibility: visible;
    -webkit-animation: fadein 0.5s, expand 0.5s 0.5s,stay 3s 1s, shrink 0.5s 2s, fadeout 0.5s 2.5s;
    animation: fadein 0.5s, expand 0.5s 0.5s,stay 3s 1s, shrink 0.5s 4s, fadeout 0.5s 4.5s;
}

@-webkit-keyframes fadein {
    from {bottom: 0; opacity: 0;} 
    to {bottom: 30px; opacity: 1;}
}

@keyframes fadein {
    from {bottom: 0; opacity: 0;}
    to {bottom: 30px; opacity: 1;}
}

@-webkit-keyframes expand {
    from {min-width: 50px} 
    to {min-width: 350px}
}

@keyframes expand {
    from {min-width: 50px}
    to {min-width: 350px}
}
@-webkit-keyframes stay {
    from {min-width: 350px} 
    to {min-width: 350px}
}

@keyframes stay {
    from {min-width: 350px}
    to {min-width: 350px}
}
@-webkit-keyframes shrink {
    from {min-width: 350px;} 
    to {min-width: 50px;}
}

@keyframes shrink {
    from {min-width: 350px;} 
    to {min-width: 50px;}
}

@-webkit-keyframes fadeout {
    from {bottom: 30px; opacity: 1;} 
    to {bottom: 60px; opacity: 0;}
}

@keyframes fadeout {
    from {bottom: 30px; opacity: 1;}
    to {bottom: 60px; opacity: 0;}
}
</style>
