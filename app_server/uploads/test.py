import json
import pandas as pd

def main():
    # Load JSON data
    with open('output_15th.json') as f:
        json_data = json.load(f)

    HEADERS = ['Account ID', 'AWS Region', 'Stack Name', 'Drift Status', 'Resource Type', 'Stack Resource Drift Status',
               'Property Differences']

    HEADER_FORMAT = {'bold': True, 'align': 'center', 'valign': 'vcenter', 'bg_color': '#B5D38D', 'border': 1}
    CELL_FORMAT = {'align': 'center', 'valign': 'vcenter', 'border': 1, 'text_wrap': True}
    property_counter = 3

    # Create DataFrame
    df = pd.DataFrame(columns=HEADERS)
    cell_id = None
    # Write the DataFrame to an Excel file without the extra header row
    excel_filename = "data.xlsx"
    with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

        # Set custom widths for header columns
        column_widths = [15, 15, 15, 15, 15, 30, 20, 20, 20, 20, 20]  # Adjust widths as needed
        worksheet = writer.sheets['Sheet1']
        for i, width in enumerate(column_widths):
            worksheet.set_column(i, i, width)

        for index, i in enumerate(HEADERS[:6]):
            cell_merge = f"{chr(65+index)}1:{chr(65+index)}2"
            worksheet.merge_range(cell_merge, i, writer.book.add_format(HEADER_FORMAT))
        # else:
        #     worksheet.merge_range('K1:K2', 'Message', writer.book.add_format(HEADER_FORMAT))

        # Add the extra header row below 'Property Differences' and merge the cell
        worksheet.merge_range('G1:J1', 'Property Differences', writer.book.add_format(HEADER_FORMAT))
        extra_headers = ['Property', 'Difference', 'Expected value', 'Actual value']
        for i, header in enumerate(extra_headers):
            worksheet.write(1, i + 6, header, writer.book.add_format(HEADER_FORMAT))

        for index, i in enumerate(json_data):
            start_j_index = property_counter
            # data for merging and single data
            for j_index, j in enumerate(i["Resources"]):
                resource_flag = 0
                start_index = property_counter
                # data for merging and merged data data
                if j["PropertyDifferences"]:
                    for k_index, k in enumerate(j["PropertyDifferences"]):
                        resource_flag += 1
                        cell_id = property_counter
                        worksheet.write(f"G{cell_id}", k.get("Property Path"), writer.book.add_format(CELL_FORMAT))
                        worksheet.write(f"H{cell_id}", k.get("Difference Type"), writer.book.add_format(CELL_FORMAT))
                        worksheet.write(f"I{cell_id}", k.get("Expected value"), writer.book.add_format(CELL_FORMAT))
                        worksheet.write(f"J{cell_id}", k.get("Actual value"), writer.book.add_format(CELL_FORMAT))
                        property_counter += 1
                    else:
                        end_index = cell_id
                        if end_index == start_index:
                            e_cell = f'E{start_index}'
                            f_cell = f'F{start_index}'
                            worksheet.write(e_cell, j.get("ResourceType"), writer.book.add_format(CELL_FORMAT))
                            worksheet.write(f_cell, j.get("StackResourceDriftStatus"), writer.book.add_format(CELL_FORMAT))
                        else:
                            e_cell = f'E{start_index}:E{end_index}'
                            f_cell = f'F{start_index}:F{end_index}'
                            worksheet.merge_range(e_cell, j.get("ResourceType"),
                                                  writer.book.add_format(CELL_FORMAT))
                            worksheet.merge_range(f_cell, j.get("StackResourceDriftStatus"),
                                                  writer.book.add_format(CELL_FORMAT))
                else:
                    cell_id = property_counter
                    worksheet.write(f"G{cell_id}", "-", writer.book.add_format(CELL_FORMAT))
                    worksheet.write(f"H{cell_id}", "-", writer.book.add_format(CELL_FORMAT))
                    worksheet.write(f"I{cell_id}", "-", writer.book.add_format(CELL_FORMAT))
                    worksheet.write(f"J{cell_id}", "-", writer.book.add_format(CELL_FORMAT))

                    e_cell = f'E{start_index}'
                    f_cell = f'F{start_index}'
                    worksheet.write(e_cell, j.get("ResourceType"), writer.book.add_format(CELL_FORMAT))
                    worksheet.write(f_cell, j.get("StackResourceDriftStatus"), writer.book.add_format(CELL_FORMAT))
                    property_counter += 1
            print("property_counter ==>", property_counter)
            print("start_j_index ==>", start_j_index)
            print("cell_id ==>",cell_id)
            if start_j_index != property_counter:
                end_j_index = property_counter - 1
                if start_j_index == end_j_index:
                    a_cell = f'A{start_j_index}'
                    b_cell = f'B{start_j_index}'
                    c_cell = f'C{start_j_index}'
                    d_cell = f'D{start_j_index}'
                    worksheet.write(a_cell, i.get("Account ID"), writer.book.add_format(CELL_FORMAT))
                    worksheet.write(b_cell, i.get("AWS Region"), writer.book.add_format(CELL_FORMAT))
                    worksheet.write(c_cell, i.get("Stack Name"), writer.book.add_format(CELL_FORMAT))
                    worksheet.write(d_cell, i.get("Drift Status"), writer.book.add_format(CELL_FORMAT))
                else:
                    a_cell = f'A{start_j_index}:A{end_j_index}'
                    b_cell = f'B{start_j_index}:B{end_j_index}'
                    c_cell = f'C{start_j_index}:C{end_j_index}'
                    d_cell = f'D{start_j_index}:D{end_j_index}'
                    worksheet.merge_range(a_cell, i.get("Account ID"), writer.book.add_format(CELL_FORMAT))
                    worksheet.merge_range(b_cell, i.get("AWS Region"), writer.book.add_format(CELL_FORMAT))
                    worksheet.merge_range(c_cell, i.get("Stack Name"), writer.book.add_format(CELL_FORMAT))
                    worksheet.merge_range(d_cell, i.get("Drift Status"), writer.book.add_format(CELL_FORMAT))
            else:
                a_cell = f'A{start_j_index}'
                b_cell = f'B{start_j_index}'
                c_cell = f'C{start_j_index}'
                d_cell = f'D{start_j_index}'
                worksheet.write(a_cell, i.get("Account ID"), writer.book.add_format(CELL_FORMAT))
                worksheet.write(b_cell, i.get("AWS Region"), writer.book.add_format(CELL_FORMAT))
                worksheet.write(c_cell, i.get("Stack Name"), writer.book.add_format(CELL_FORMAT))
                worksheet.write(d_cell, i.get("Drift Status"), writer.book.add_format(CELL_FORMAT))
            print("*"*100)

    print("SUCCESS")

if __name__ == '__main__':
    main()