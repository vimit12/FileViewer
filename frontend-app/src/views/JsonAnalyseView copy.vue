<template>

    <div>

        <v-card>
            <v-layout>
                <v-list nav style="background-color: black; color: aliceblue;">
                    <v-list-item prepend-icon="mdi-home" title="Home" @click="go_back()"></v-list-item>

                    <template v-for="(value, key) in data_type">

                        <template v-if="value === 'string' ||  value === 'number'">
                            <v-list-item :key="key" :prepend-icon="getIcon(key)" :title="key"
                                :value="key"></v-list-item>
                        </template>
                        <template v-else-if="value === 'object' || value ==='array'">
                            <v-list-group :key="key" :value="key">
                                <template v-slot:activator="{ props }">
                                    <v-list-item v-bind="props" :prepend-icon="getIcon(key)" :title="key"></v-list-item>
                                </template>


                                <!-- <v-list-group :value="key">
                                    <template v-slot:activator="{ props }">
                                        <v-list-item v-bind="props" v-for="(subKey, subIndex) in findKeyLevelOne(key)  "
                                            :key="subIndex" :title="subKey" :prepend-icon="getIcon(subKey)">
                                        </v-list-item>
                                    </template>
                                </v-list-group> -->


                                <!-- <v-list-group :value="key">
                                    <template v-slot:activator="{ props }">
                                        <v-list-item v-bind="props" v-for="(subKey, subIndex) in findKeyLevelOne(key) "
                                            :key="subIndex" :title="subKey" :prepend-icon="getIcon(subKey)"> -->
                                            <!-- Conditionally render different content based on the type of subKey -->
                                            <!-- <template v-if="secondLevelResult[subKey] === 'array'"> -->
                                                <!-- Render content for array type -->
                                                <!-- <v-list-item v-for="(item, idx) in extractKeysFromNestedData(key, subKey)" :key="idx"
                                                    :title="item" >
                                                </v-list-item>
                                            </template>
                                            <template v-else-if="secondLevelResult[subKey] === 'object'"> -->
                                                <!-- Render content for object type -->
                                                <!-- <v-list-item> -->
                                                    <!-- Your content for object type -->
                                                <!-- </v-list-item> -->
                                            <!-- </template>
                                            <template v-else> -->
                                                <!-- Render content for string or number type -->
                                                <!-- {{ subKey }} -->
                                            <!-- </template>
                                        </v-list-item>
                                    </template>
                                </v-list-group> -->




                                <v-list-item v-for="(subKey, subIndex) in findKeyLevelOne(key) " :key="subIndex"
                                    :title="subKey" :prepend-icon="getIcon(subKey)">
                                </v-list-item>

                                <!-- Add content for array or object here -->
                            </v-list-group>
                        </template>
                    </template>
                </v-list>

                <!-- </v-navigation-drawer> -->

                <v-main class="main-container">
                    <v-container>
                        <v-row>
                            <v-col cols="12" md="4">
                                <v-card>
                                    <v-card-title class="bold-title">{{ title1 }}</v-card-title>
                                    <v-card-text>
                                        {{ content1 }}
                                    </v-card-text>
                                </v-card>
                            </v-col>
                            <v-col cols="12" md="4">
                                <v-card>
                                    <v-card-title class="bold-title">{{ title2 }}</v-card-title>
                                    <v-card-text>
                                        {{ content2 }}
                                    </v-card-text>
                                </v-card>
                            </v-col>
                            <v-col cols="12" md="4">
                                <v-card>
                                    <v-card-title class="bold-title">{{ title3 }}</v-card-title>
                                    <v-card-text>
                                        {{ content3 }}
                                    </v-card-text>
                                </v-card>
                            </v-col>
                        </v-row>

                        <v-row>
                            <v-col cols="12">
                                <v-card>
                                    <v-card-title>Full-width Card</v-card-title>
                                    <v-card-text>
                                        Content for Full-width Card
                                    </v-card-text>
                                </v-card>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-main>
            </v-layout>
        </v-card>

        <!-- <div>
            <apexchart width="500" type="bar" :options="options" :series="series"></apexchart>

        </div> -->
    </div>
</template>

<script>


/* eslint-disable */
import axios from 'axios';

export default {
    name: 'JsonAnalyseView',
    components: {
        
    },
    data() {
        return {
            title1: "Card 1",
            content1: "Content of Card 1",
            title2: "Card 2",
            content2: "Content of Card 2",
            title3: "Card 3",
            content3: "Content of Card 3",
            result: [],
            firstLevelResult: [],
            secondLevelResult: null,
            
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
        go_back(){
            this.$router.push(
                {
                    name: 'home'
                })
        },
        getIcon(key) {
            // Define mappings from key to icon here
            const iconMap = {
                "Back":'mdi-backburger',
                "Account ID": 'mdi-bank-outline',
                "AWS Region": 'mdi-map-marker',
                "Stack Name": 'mdi-stack-exchange',
                "Drift Status":'mdi-valve',
                "Resources": 'mdi-semantic-web',
                "ResourceType":'mdi-resistor-nodes',
                "LogicalResourceId":'mdi-abacus',
                "PhysicalResourceId":'mdi-align-horizontal-center',
                "StackResourceDriftStatus":'mdi-octagram-outline',
                "ExpectedProperties":'mdi-receipt',
                "ActualProperties":'mdi-fire',
                "PropertyDifferences":'mdi-arrow-decision',
                "Message":'mdi-message'
                // Add more mappings as needed
            };
            return iconMap[key] || 'mdi-information'; // Default icon if key not found in the map
        },
        findDataTypes(json) {
            let dataTypes = [];

            function traverse(obj) {
                for (let key in obj) {
                    let value = obj[key];
                    let type = typeof value;

                    if (type === 'object' && Array.isArray(value)) {
                        type = 'array';
                        if (value.length > 0) {
                            traverse(value[0]);
                        }
                    } else if (type === 'object') {
                        traverse(value);
                    }

                    if (!dataTypes.includes(type)) {
                        dataTypes.push(type);
                    }
                }
            }

            traverse(json);
            return dataTypes;
        },
        analyzeDataTypes(data) {
            const result = {};

            // Iterate over each object in the array
            data.forEach(obj => {
                // Iterate over each key in the object
                Object.keys(obj).forEach(key => {
                    // Check if the value is a string, array, or object
                    if (typeof obj[key] === 'string') {
                        // If the value is a string, set its data type as 'string'
                        result[key] = 'string';
                    } else if (Array.isArray(obj[key])) {
                        // If the value is an array, set its data type as 'array'
                        result[key] = 'array';
                    } else if (typeof obj[key] === 'object') {
                        // If the value is an object, set its data type as 'object'
                        result[key] = 'object';
                    } else if (typeof obj[key] === 'number') {
                        result[key] = 'number';
                    }
                });
            });

            return result;
        },
        analyzeValueTypes(value) {
            if (value === null){
                return 'null'
            }
            else if (typeof value === 'string') {
                return 'string';
            } else if (Array.isArray(value)) {
                return 'array';
            } else if (typeof value === 'object' && value !== null) {
                // If value is an object, analyze its properties recursively
                const nestedResult = {};
                Object.keys(value).forEach(key => {
                    nestedResult[key] = analyzeValueTypes(value[key]);
                });
                return nestedResult;
            } else if (typeof value === 'number') {
                return 'number';
            } else {
                return typeof value; // Handle other data types as-is
            }
        },
        analyzeRecursiveDataTypes(data) {
            const result = {};

            // Iterate over each key in the object
            Object.keys(data).forEach(key => {
                // Analyze data types of values recursively
                result[key] = this.analyzeValueTypes(data[key]);
            });

            return result;
        },
        findKeyLevelOne(key) {
            console.log("key is ==>", key)
            let firstLevelResult = [];
            this.rawJsonData.forEach(obj => {
                for (let k in obj[key]) {
                    this.secondLevelResult = this.analyzeRecursiveDataTypes(obj[key][k]);
                    firstLevelResult.push(...Object.keys(obj[key][k]));
                }
            });

            // Convert the array to a Set to remove duplicates, then convert it back to an array
            firstLevelResult = Array.from(new Set(firstLevelResult));
            // console.log(firstLevelResult);
            return firstLevelResult;
        },
        extractKeysFromNestedData(outerKey, innerKey) {
            const keysSet = new Set(); // Using Set to store unique keys

            // Iterate through each object in the data
            this.rawJsonData.forEach(obj => {
                if (obj.hasOwnProperty(outerKey)) {
                    obj[outerKey].forEach(item => {
                        if (item.hasOwnProperty(innerKey)) {
                            item[innerKey].forEach(diff => {
                                // Add keys from the current difference object to the set
                                Object.keys(diff).forEach(key => {
                                    keysSet.add(key);
                                });
                            });
                        }
                    });
                }
            });

            // Convert Set to array and return unique keys
            return Array.from(keysSet);
        }
        
    },
    created() {
        const colorcode = localStorage.getItem('colorcode');
        if (colorcode) {
            this.colorcode = colorcode
        }

        this.rawJsonData = JSON.parse(this.$route.query.data);

        
        this.file_name = this.$route.query.file_name;
        this.file_type = this.$route.query.file_type;

        this.keys = Object.keys(this.rawJsonData[0]).map(head => (head));
        this.data_type = this.analyzeDataTypes(this.rawJsonData)

        this.title1 = "File : "
        this.content1 = this.file_name

        this.title2 = "Total Data Length : "
        this.content2 = this.rawJsonData.length

        this.title3 = "Type of Data : "
        this.content3 = this.findDataTypes(this.rawJsonData)
        

    }
}
</script>

<style>
        .main-container {
            height: 100vh;
            /* Set height to 100% of viewport height */
            overflow-y: auto;
            /* Add vertical scroll if content overflows */
        }

        .bold-title {
            font-weight: bold;
        }
</style>
