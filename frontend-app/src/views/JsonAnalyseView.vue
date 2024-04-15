<template>

    <div>

        <v-card>
            <v-layout>
                <v-list nav style="background-color: black; color: aliceblue;">
                    <v-list-item prepend-icon="mdi-home" title="Home" @click="go_back()"></v-list-item>

                    <template v-for="(value, key) in data_type">

                        <template v-if="value === 'string' ||  value === 'number'">
                            <v-list-item :key="key" :prepend-icon="getIcon(key)" :title="key" :value="key"
                                @click="evaluate_key(key)"></v-list-item>
                        </template>
                        <template v-else-if="value === 'object' || value ==='array'">
                            <v-list-group :key="key" :value="key">
                                <template v-slot:activator="{ props }">
                                    <v-list-item v-bind="props" :prepend-icon="getIcon(key)" :title="key"
                                        :value="key"></v-list-item>
                                </template>

                                <v-list-item v-for="(subKey, subIndex) in findKeyLevelOne(key) " :key="subIndex"
                                    :title="subKey" :prepend-icon="getIcon(subKey)" @click="evaluate_key(key)">
                                </v-list-item>

                            </v-list-group>
                        </template>
                    </template>
                </v-list>

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
                            <v-col cols="12" md="12">
                                <v-card elevation="16">

                                    <v-card-text elevation="24">
                                        <v-radio-group inline label="Change View : " v-model="selectedView">
                                            <v-radio label="Tabular View" value="table" color="red-darken-3">
                                                <template v-slot:label>
                                                    <div><strong class="text-success">Tabular View</strong></div>
                                                </template>
                                            </v-radio>
                                            <v-radio label="Bar Chart" value="bar" color="red-darken-3">
                                                <template v-slot:label>
                                                    <div><strong class="text-success">Bar Chart View</strong></div>
                                                </template>
                                            </v-radio>
                                            <v-radio label="Pie Chart" value="pie" color="red-darken-3">
                                                <template v-slot:label>
                                                    <div><strong class="text-success">Pie Chart View</strong></div>
                                                </template>
                                            </v-radio>
                                        </v-radio-group>
                                    </v-card-text>
                                </v-card>
                            </v-col>

                        </v-row>

                        <v-row v-if="selectedView === 'table'">
                            <v-col v-for="(key, index) in Object.keys(this.data_type)" :key="index" cols="6">
                                <v-card :hover="true" :variant="outline">
                                    <v-card-title>{{ key }}</v-card-title>
                                    <v-card-text>
                                        <v-table height="300px" fixed-header>
                                            <thead>
                                                <tr>
                                                    <th class="text-left">
                                                        {{ key }}
                                                    </th>
                                                    <th class="text-left">
                                                        Count
                                                    </th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr v-for="(count, value) in countsObj[key]" :key="value">
                                                    <td>{{ truncateString(value, 50) }}</td>
                                                    <td>{{ count }}</td>
                                                </tr>
                                            </tbody>
                                        </v-table>
                                    </v-card-text>
                                </v-card>
                            </v-col>
                        </v-row>
                        <v-row v-else-if="selectedView === 'bar'">
                            <v-col v-for="(key, index) in Object.keys(this.data_type) " :key="index" cols="6">
                                <v-card :hover="true" :variant="outline">
                                    <v-card-title>{{ key }}</v-card-title>
                                    <v-card-text v-if="changeoptions(key,'bar').flag == false">
                                        <apexchart width="500" type="bar" :options="changeoptions(key, 'bar').options"
                                            :series="changeoptions(key, 'bar').series"></apexchart>
                                    </v-card-text>
                                    <v-card-text v-else>
                                        Data too cuttered to be plotted...
                                    </v-card-text>

                                </v-card>
                            </v-col>
                        </v-row>
                        <v-row v-else-if="selectedView === 'pie'">
                            <v-col v-for="(key, index) in Object.keys(this.data_type)  " :key="index" cols="6">
                                <v-card :hover="true" :variant="outline">
                                    <v-card-title>{{ key }}</v-card-title>
                                    <v-card-text v-if="changeoptions(key, 'bar').flag == false">
                                        <apexchart width="500" type="pie" :options="changeoptions(key, 'pie').options"
                                            :series="changeoptions(key, 'pie').series">
                                        </apexchart>
                                    </v-card-text>
                                    <v-card-text v-else>
                                        Data too cuttered to be plotted...
                                    </v-card-text>
                                </v-card>
                            </v-col>
                        </v-row>


                    </v-container>
                </v-main>
            </v-layout>
        </v-card>

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
            selectedView: 'table', 
            mdiIcons : [
                'mdi-account',
                'mdi-account-group',
                'mdi-home',
                'mdi-settings',
                'mdi-bell',
                'mdi-email',
                'mdi-calendar',
                'mdi-clock',
                'mdi-folder',
                'mdi-file-document',
                'mdi-star',
                'mdi-heart',
                'mdi-comment',
                'mdi-chat',
                'mdi-camera',
                'mdi-image',
                'mdi-video',
                'mdi-music',
                'mdi-play',
                'mdi-pause',
                'mdi-stop',
                'mdi-fast-forward',
                'mdi-fast-rewind',
                'mdi-volume-high',
                'mdi-volume-medium',
                'mdi-volume-low',
                'mdi-volume-off',
                'mdi-wifi',
                'mdi-battery',
                'mdi-lock',
                // Add more icons as needed
            ],
            title1: "Card 1",
            content1: "Content of Card 1",
            title2: "Card 2",
            content2: "Content of Card 2",
            title3: "Card 3",
            content3: "Content of Card 3",
            result: [],
            firstLevelResult: [],
            secondLevelResult: null,
            allKeys: [],
            countsObj: {},
        
            
        }
    },
    computed: {
        trimmedCounts() {
            const trimmed = {};
            for (const [value, count] of Object.entries(this.countsObj[this.key])) {
                trimmed[this.truncateString(value, 50)] = count;
            }
            return trimmed;
        },
    },
    watch: {
        selectedView(newVal, oldVal) {
            console.log(`View changed from ${oldVal} to ${newVal}`);
            // Add logic here to handle view changes
        },
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
        changeoptions(key, type) {
            let flag = false;
            const value = this.countsObj[key];
            const keysArray = Object.keys(value);
            const valuesArray = Object.values(value);

            if (type === 'bar') {
                const options = {
                    chart: {
                        id: 'Bar Chart'
                    },
                    xaxis: {
                        categories: keysArray
                    },
                    plotOptions: {
                        bar: {
                            distributed: true
                        }
                    }
                };
                const series = [{
                    name: 'count',
                    data: valuesArray
                }];

                if (options.xaxis.categories.length > 20 || series[0].data.length > 20) {
                    flag = true;
                }

                return { options: options, series: series, flag: flag };
            } else {
                if (keysArray.length > 20 || valuesArray.length > 20) {
                    flag = true;
                }
                const chartOptions = {
                    chart: {
                        type: 'donut',
                    },
                    labels: keysArray,
                    dataLabels: {
                        enabled: true
                    },
                    plotOptions: {
                        pie: {
                            customScale: 0.8,
                            expandOnClick: true,
                        }
                    },
                    pie: {
                        donut: {
                            size: '65%'
                        }
                    }
                };
                const series = valuesArray;

                return { options: chartOptions, series: series, flag: flag };
            }
        },

        handleViewChange() {
            // This method will be called when the view changes
            console.log('View changed:', this.selectedView);
            // You can add more logic here if needed
        },
        truncateString(str, num) {
            if (str.length <= num) {
                return str;
            }
            return str.slice(0, num) + '...';
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
            return iconMap[key] || this.mdiIcons[Math.floor(Math.random() * this.mdiIcons.length)];
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
            // //console.log("key is ==>", key)
            let firstLevelResult = [];
            this.rawJsonData.forEach(obj => {
                for (let k in obj[key]) {
                    this.secondLevelResult = this.analyzeRecursiveDataTypes(obj[key][k]);
                    firstLevelResult.push(...Object.keys(obj[key][k]));
                }
            });

            // Convert the array to a Set to remove duplicates, then convert it back to an array
            firstLevelResult = Array.from(new Set(firstLevelResult));
            // //console.log(firstLevelResult);
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
        },
        evaluate_key(key){
            // alert(key);
        },
        extractAllKeys(data) {
            const keys = [];

            const traverse = (obj) => {
                for (const prop in obj) {
                    if (obj.hasOwnProperty(prop)) {
                        if (typeof obj[prop] === 'object') {
                            traverse(obj[prop]);
                        } else {
                            keys.push(prop);
                        }
                    }
                }
            };

            data.forEach(obj => {
                traverse(obj);
            });

            return Array.from(new Set(keys));
        },
        countValuesForKey(key) {
            const counts = {};

            this.rawJsonData.forEach(item => {
                let keyValue;

                if (typeof item[key] === 'object') {
                    keyValue = JSON.stringify(item[key]);
                } else {
                    keyValue = item[key];
                }

                counts[keyValue] = (counts[keyValue] || 0) + 1;
            });

            return counts;
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
        this.allKeys = this.extractAllKeys(this.rawJsonData);
        
        // Assuming this.allKeys is an array of key names
        Object.keys(this.data_type).forEach(key => {
            //console.log(this.findKeyLevelOne(key))
            // Calculate counts for the current key
            const counts = this.countValuesForKey(key);

            // Store the counts in the countsObj using keyname + '_count' as the property name
            this.countsObj[key] = counts;
        });

        // Now countsObj contains counts for each key in a dynamically named property
        //console.log(this.countsObj);

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
