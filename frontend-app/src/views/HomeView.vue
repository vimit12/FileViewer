<template>
    <v-row justify="space-around">

            <v-col cols="auto">
              <v-dialog v-model="dialogVisible" transition="dialog-top-transition" width="auto">
                
                <template v-slot:default="{ isActive }">
                  <v-card>
                    <v-toolbar v-bind:color="colorcode" title="Choose Action : "></v-toolbar>
                    <v-card-text>
                      <div class="">
                            <v-row justify="center">

                            <v-col cols="6">
                                <v-btn block rounded="xl" size="x-large" style="width: 15em; height: 5em;"><v-icon icon="mdi-data-matrix-scan" />Create Data</v-btn>
                            </v-col>

                            <v-col cols="6" >
                                <v-btn block rounded="xl" size="x-large" style="width: 15em; height: 5em;" @click="view_data"><v-icon icon="mdi-view-dashboard-variant" />View Data</v-btn>
                            </v-col>
                            </v-row>
                      </div>
                    </v-card-text>
                    <v-card-actions class="justify-end">
                      <v-btn variant="text" @click="isActive.value = false">Close</v-btn>
                    </v-card-actions>
                  </v-card>
                </template>
              </v-dialog>
            </v-col>

            <v-col cols="auto">
              <v-dialog v-model="viewDialog" transition="dialog-top-transition" width="auto">
            
                <template v-slot:default="{ isActive }">
                  <v-card>
                    <v-toolbar v-bind:color="colorcode" title="File Upload : "></v-toolbar>
                    <v-card-text>
                            <v-row justify="center">

                            <v-col cols="12">
                                <v-file-input id="file_input" show-size label="File input" style="width: 30em; margin: 0 1rem 0 1rem;"></v-file-input>
                            </v-col>

                            </v-row>
                    </v-card-text>
                    <v-card-actions class="justify-end">
                      <v-btn  variant="text" @click="isActive.value = false">Close</v-btn>
                      <v-btn  variant="text" @click="local_view()">View</v-btn>
                    </v-card-actions>
                  </v-card>
                </template>
              </v-dialog>
            </v-col>
    </v-row>

      
</template>

<script>
/* eslint-disable */
import axios from 'axios';
import { createToast } from "mosha-vue-toastify";

export default {
    name: 'HomeView',
    components: {
        
    },
    data() {
        return {
            dialogVisible: true,
            viewDialog: false,
            colorcode: "black"
        }
    },
    mounted() {
        document.title = "Action";
        const colorcode = localStorage.getItem('colorcode');
        if (colorcode){
          this.colorcode = colorcode
        }
        
    },
    beforeUnmount() {
        
    },
    methods: {
        view_data(){
            this.dialogVisible = false
            this.viewDialog = true;
        },
        
        // local_view(){
            
        //     const fileInput = document.getElementById('file_input');
        //     const file = fileInput.files[0];

        //     if (!file) {
        //         console.error('No file selected');
        //         return;
        //     }

        //     const formData = new FormData();
        //     formData.append('file', file);

            
        //     axios.post(`${process.env.BASE_API_URL}upload/`, formData)
        //         .then(response => {
        //             // Handle API response data
        //             var resp = response.data;
        //             if (resp.status_code == 200) {
        //                 if (resp.file_type == 'json' || resp.file_type == 'xlsx'){
        //                     this.$router.push(
        //                       { name: 'json' , 
        //                         query: 
        //                         {
        //                           data: resp.data,
        //                           file_name: resp.file_name,
        //                           file_type: resp.file_type
        //                         }
        //                       })
        //                 } else {

        //                 }
        //             } else {
        //                 createToast(JSON.stringify(resp.error),
        //                     {
        //                         showIcon: 'true',
        //                         hideProgressBar: 'false',
        //                         type: 'danger',
        //                         showCloseButton: 'true',
        //                         transition: 'slide',
        //                         position: 'bottom-center',
        //                     })
        //             }
        //         })
        //         .catch(error => {
        //             // alert(JSON.stringify(error))

        //             createToast(JSON.stringify(error),
        //                 {
        //                     showIcon: 'true',
        //                     hideProgressBar: 'false',
        //                     type: 'danger',
        //                     showCloseButton: 'true',
        //                     transition: 'slide',
        //                     position: 'bottom-center',
        //                 })
        //         });

        // },
          
        // local_view() {
        //   //this function is without API call just to view file details.
        //     const fileInput = document.getElementById('file_input');
        //     const file = fileInput.files[0];
        //     if (file) {
        //         const fileName = file.name; // Extract file name
        //         const fileType = file.type; // Extract file type
        //         const reader = new FileReader();

        //         reader.onload = (event) => {
        //             const fileContent = event.target.result; // Extract file content
        //             // Now you have fileName, fileType, and fileContent available for further processing
        //             console.log('File Name:', fileName);
        //             console.log('File Type:', fileType);
        //             console.log('File Content:', fileContent);
                    
        //             // Check if file type is JSON
        //             if (fileType === 'application/json') {
        //                 // Parse JSON content
        //                 try {
        //                     const jsonData = JSON.parse(fileContent);
        //                     console.log('JSON Data:', jsonData);
        //                     // You can now use jsonData for further processing
        //                     this.$router.push({
        //                         name: 'json',
        //                         query: {
        //                             data: fileContent,
        //                             file_name: fileName,
        //                             file_type: fileType
        //                         }
        //                     });
        //                 } catch (error) {
        //                     console.error('Error parsing JSON:', error);
        //                 }
        //             }
        //         };

        //         reader.readAsText(file); // Read file as text
        //     }
        // }


        local_view() {
        const fileInput = document.getElementById('file_input');
        const file = fileInput.files[0];
        if (file) {
            const fileName = file.name; // Extract file name
            const fileType = file.type; // Extract file type
            const chunkSize = 1024 * 1024; // 1 MB chunk size
            let offset = 0;
            let fileContent = ''; // Initialize file content

            const reader = new FileReader();

            reader.onload = (event) => {
                // Process chunk
                const chunk = event.target.result;
                fileContent += chunk; // Append chunk to fileContent

                // Update offset
                offset += chunk.length;

                // Read the next chunk
                if (offset < file.size) {
                    readNextChunk();
                } else {
                    // Finished reading the entire file
                    console.log('File processing completed.');
                    // Check if file type is JSON
                    if (fileType === 'application/json') {
                        // Parse JSON content
                        try {
                            const jsonData = JSON.parse(fileContent);
                            console.log('JSON Data:', jsonData);
                            // You can now use jsonData for further processing
                            this.$router.push({
                                name: 'json',
                                query: {
                                    data: fileContent,
                                    file_name: fileName,
                                    file_type: fileType
                                }
                            });
                        } catch (error) {
                            console.error('Error parsing JSON:', error);
                        }
                    }
                }
            };

            reader.onerror = (event) => {
                console.error('Error reading file:', event.target.error);
            };

            const readNextChunk = () => {
                const blob = file.slice(offset, offset + chunkSize);
                reader.readAsText(blob);
            };

            // Start reading the first chunk
            readNextChunk();
        }
    }


    }
}
</script>

<style>
/* Add your scoped styles here */
</style>
