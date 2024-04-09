import json
import re

HTML_TEMPLATE = '''
    <!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dynamic Table with Bootstrap</title>
  <!-- Include Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

  <style>
    /* Add custom styles here */
    .wrap-text {
      word-wrap: break-word;
    }
    .table-responsive {
      overflow-x: auto;
    }

    .table td {
      max-width: 300px; /* Example maximum width */
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      cursor: pointer;

    }

    .sort-icon {
      display: inline-block;
      width: 0;
      height: 0;
      vertical-align: middle;
      transition: transform 0.2s ease;
    }
    .asc {
      border-left: 5px solid transparent;
      border-right: 5px solid transparent;
      border-bottom: 5px solid;
    }
    .desc {
      border-left: 5px solid transparent;
      border-right: 5px solid transparent;
      border-top: 5px solid;
    }
  </style>

</head>

<body class="bg-light">
  <div class="container py-4">
    <!-- Search Bar -->
    <div class="mb-4">
      <input id="searchInput" type="text" placeholder="Search..." class="form-control">
    </div>
    <!-- Table Container -->
    <div id="tableContainer" class="bg-white rounded-md shadow-md overflow-x-auto table-responsive"></div>
  </div>

  <!-- Modal -->
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Column Name</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body" id="nestedTableContainer">
          <!-- <p id="modalContent">Content here...</p> -->
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>

  

  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"
    integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"
    integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>

  <!-- JavaScript -->
  <script>
    let currentSortColumn = null;
    let isAscending = true;
    
    // JSON data variable
    const jsonData = %JSON_DATA%

    function renderTable(jsonData) {
      const tableContainer = document.getElementById('tableContainer');
      tableContainer.innerHTML = '';

      try {
        const data = jsonData;
        const keys = Object.keys(data[0]);

        // Create table element
        const table = document.createElement('table');
        table.className = 'table table-bordered table-striped align-middle';

        // Create table header
        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        keys.forEach(key => {
          const th = document.createElement('th');
          th.textContent = key;
          th.className = "table-info"
          // Add sorting icons
          const icon = document.createElement('span');
          icon.className = 'sort-icon';

          th.appendChild(icon);
          headerRow.appendChild(th);
          th.addEventListener('click', () => {
            sortTable(key);
          });
        });
        thead.appendChild(headerRow);
        table.appendChild(thead);

        // Create table body
        const tbody = document.createElement('tbody');
        data.forEach(item => {
          const row = document.createElement('tr');
          keys.forEach(key => {
            const td = document.createElement('td');
            const content = typeof item[key] === 'string' ? item[key] : JSON.stringify(item[key]);
            td.textContent = content;
            // if (content.length > 50) {
            //   td.className = 'wrap-text'; // Apply wrap-text class for long content
            // }
            if (content.length > 50) {
              
              td.classList.add('wrap-text');
            }
            td.addEventListener('click', () => {
              handleClick(td, key); // Call the handleClick function on click
            });
            row.appendChild(td);
          });
          tbody.appendChild(row);
        });
        table.appendChild(tbody);

        // Append table to container
        tableContainer.appendChild(table);
      } catch (error) {
        tableContainer.textContent = 'No Record Found!!';
      }
    }

    // Initial render
    renderTable(jsonData);

    // Search functionality
    // Recursive function to search for a term in the data object
      function searchInData(data, term) {
        return Object.values(data).some(value => {
          if (typeof value === 'object' && value !== null) {
            // If value is an object or array, recursively search inside it
            return searchInData(value, term);
          } else if (typeof value === 'string' && value.toLowerCase().includes(term)) {
            // If value is a string and contains the search term, return true
            return true;
          }
          return false;
        });
      }

      // Update search input event listener
      searchInput.addEventListener('input', () => {
        const searchTerm = searchInput.value.trim().toLowerCase(); // Trim whitespace and convert to lowercase
        const filteredData = jsonData.filter(item => {
          // Check if any value in the item contains the search term
          return searchInData(item, searchTerm);
        });
        renderTable(filteredData);
      });
    
    //Identify Array
    function identifyArrayType(arr) {
        if (typeof arr === 'object' && arr !== null && !Array.isArray(arr)) {
          return "objects"
        }
        // Check if string
        if (typeof arr === 'string' && arr !== null && !Array.isArray(arr)) {
          return "string";
        }

        // Check if numbers
        if (typeof arr === 'number' && arr !== null && !Array.isArray(arr)) {
          return "numbers";
        }

        // Check if array is empty
        if (arr.length === 0) {
          return "Empty array";
        }

        // Check if array of arrays
        if (arr.every(innerArr => Array.isArray(innerArr))) {
          return "Array of arrays";
        }

        // Check if array of objects
        if (arr.every(item => typeof item === 'object' && item !== null && !Array.isArray(item))) {
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
      }

    
    // Function to handle text wrapping behavior
    function handleClick(td, columnKey) {
        const modalTitle = document.getElementById('exampleModalLabel');
        modalTitle.textContent = columnKey + " : "; // Set modal title to column key

        const modalContent = document.getElementById('nestedTableContainer');
        

        const content = td.textContent;

        let parsedContent;
        try {
            // Try parsing content as JSON
            parsedContent = JSON.parse(content);
        } catch (error) {
          // If parsing fails, assume content is a string
          parsedContent = content;
        }
        let value = identifyArrayType(parsedContent)
        
        if (value === "Array of objects" || value === "objects") {
          renderNestedTable(parsedContent, modalContent, value);
        }
        else {
          modalContent.textContent = td.textContent; // Set modal content to clicked cell content
        }
        
        const modal = new bootstrap.Modal(document.getElementById('exampleModal')); // Create modal instance
        modal.show(); // Show the modal
      }
    
    // Sorting function
    function sortTable(column) {
      if (currentSortColumn === column) {
        isAscending = !isAscending;
      } else {
        currentSortColumn = column;
        isAscending = true;
      }

      const sortedData = jsonData.slice().sort((a, b) => {
        const valueA = typeof a[column] === 'string' ? a[column].toLowerCase() : a[column];
        const valueB = typeof b[column] === 'string' ? b[column].toLowerCase() : b[column];

        if (isAscending) {
          return valueA > valueB ? 1 : -1;
        } else {
          return valueA < valueB ? 1 : -1;
        }
      });

      renderTable(sortedData);
      updateSortIcons(column);
    }

    // Update sort icons
    function updateSortIcons(column) {
      const headers = document.querySelectorAll('th');
      headers.forEach(th => {
        const icon = th.querySelector('.sort-icon');
        if (th.textContent === column) {
          icon.classList.remove('asc', 'desc');
          icon.classList.add(isAscending ? 'asc' : 'desc');
        } else {
          icon.classList.remove('asc', 'desc');
        }
      });
    }
    
    function renderNestedTable(data, modalContent, type) {
        const nestedData = type === "objects" ? [data] : data;
        modalContent.innerHTML = '';

        try {
          const nestedKeys = Object.keys(nestedData[0]);

          // Create table element
          const nestedTable = document.createElement('table');
          nestedTable.className = 'table table-bordered table-striped align-middle';

          // Create table header
          const nestedThead = document.createElement('thead');
          const nestedHeaderRow = document.createElement('tr');

          nestedKeys.forEach(key => {
            const nestedTh = document.createElement('th');
            nestedTh.textContent = key;
            nestedTh.className = "table-primary";

            nestedHeaderRow.appendChild(nestedTh);
          });
          nestedThead.appendChild(nestedHeaderRow);
          nestedTable.appendChild(nestedThead);

          // Create table body
          const nestedTbody = document.createElement('tbody');

          nestedData.forEach(item => {
            const nestedRow = document.createElement('tr');

            nestedKeys.forEach(key => {
              const nestedTd = document.createElement('td');

              let nestedContent = item[key];
              // Check if content is object or array
              if (typeof nestedContent === 'object') {
                nestedContent = JSON.stringify(nestedContent);
                // Add an onclick event to show modal
                nestedTd.classList.add('nested-data');
                nestedTd.addEventListener('click', () => {
                  handleClick(nestedTd, key);
                });
              }

              nestedTd.textContent = nestedContent;
              nestedRow.appendChild(nestedTd);
            });
            nestedTbody.appendChild(nestedRow);
          });
          nestedTable.appendChild(nestedTbody);

          // Append table to container
          modalContent.appendChild(nestedTable);
        } catch (error) {
          modalContent.textContent = 'No Record Found!!';
        }
      }


  </script>
</body>

</html>

'''

# Sample JSON data to replace in the HTML file
updated_json_data = [
    {"name": "Charlie", "age": 28},
    {"name": "David", "age": 35}
]

# Convert the JSON data to a string for HTML
json_data_str = json.dumps(updated_json_data)

# Replace the placeholder with the JSON data in the template content
final_html_content = HTML_TEMPLATE.replace('%JSON_DATA%', json_data_str)

# Path to the HTML file to create
file_path = "example.html"

# Open the file in write mode and write the HTML content
with open(file_path, "w") as file:
    file.write(final_html_content)

print(f"HTML file '{file_path}' has been created.")