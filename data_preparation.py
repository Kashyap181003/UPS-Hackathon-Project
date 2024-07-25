import pandas as pd
import re
from multiprocessing import Pool, Process, cpu_count

# Function to check HTS code format
def is_valid_hts_code(code):
    code = str(code)
    if len(code) == 13:
        data_str = f"{code:013}"
        data_str = f'{data_str[:4]}.{data_str[5:7]}.{data_str[8:10]}.{data_str[11:]}'
        pattern = re.compile(r'^\d{4}\.\d{2}\.\d{2}\.\d{2}$')
        if pattern.match(data_str):
            return True
    return False

# Function to get description by HTS code
def get_description_by_hts_code(hts_code, df):
    filtered_row = df[df['HTS Number'] == hts_code]
    if not filtered_row.empty:
        return filtered_row.iloc[0]['Description']
    else:
        return ""

# Function to get other items' descriptions
def get_other_items(start, end, df):
    indent_levels = list(range(0, df.loc[end, 'Indent'] + 1))
    indent_values = df.loc[start:end, 'Indent']
    reversed_indents = indent_values.iloc[::-1].reset_index(drop=True)
    rev_dict = reversed_indents.to_dict()

    first_occurrences = {}
    for i, indent in rev_dict.items():
        if indent not in first_occurrences:
            first_occurrences[indent] = end - i

    full_desc = []
    for indent_level in indent_levels:
        if indent_level in first_occurrences:
            row_index = first_occurrences[indent_level]
            description = df.loc[row_index, 'Description']
            full_desc.append(description)

    return full_desc

# Function to process each chunk
def process_chunk(chunk):
    df_entries = pd.DataFrame(columns=['HTS Number', 'Description'])
    for index, row in chunk.iterrows():
        hts_number = row['HTS Number']
        if is_valid_hts_code(hts_number):
            main_desc = get_description_by_hts_code(hts_number, chunk)
            cell_indices_m = chunk.isin([hts_number])
            row_indices_m = cell_indices_m.where(cell_indices_m).dropna(how='all').dropna(axis=1, how='all').stack().index.tolist()
            end = row_indices_m[0][0]

            parent1 = hts_number[:4]
            cell_indices = chunk.isin([parent1])
            row_indices = cell_indices.where(cell_indices).dropna(how='all').dropna(axis=1, how='all').stack().index.tolist()
            if row_indices:
                start = row_indices[0][0]
                total_desc = get_other_items(start, end, chunk)
                df_entries.loc[len(df_entries)] = [hts_number, total_desc]

    return df_entries

# Main function to read and process the CSV in chunks using multiprocessing
def collect(file_path, output_path, chunk_size=1000):
    df_entries = pd.DataFrame(columns=['HTS Number', 'Description'])
    pool = Pool(cpu_count())
    reader = pd.read_csv(file_path, chunksize=chunk_size)

    # Process chunks in parallel
    results = pool.map(process_chunk, reader)

    # Concatenate all results
    df_entries = pd.concat(results, ignore_index=True)

    # Save the results to CSV
    df_entries.to_csv(output_path, index=False)

# Define file paths
file_path = 'htsdata.csv'
output_path = 'out.csv'

# Run the main function
# collect(file_path, output_path)

if __name__ == '__main__':
    p = Process(target=collect, args=('htsdata.csv','out.csv'))
    p.start()
    p.join()
