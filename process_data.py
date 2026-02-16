import pandas as pd
import os

def process_soul_foods_data():
    # Path folder 
    data_path = './data'
    output_filename = 'formatted_data.csv'
    
    # 1. READ AND COMBINE
    dfs = []
    for file in os.listdir(data_path):
        if file.endswith('.csv'):
            file_path = os.path.join(data_path, file)
            dfs.append(pd.read_csv(file_path))
    
    # 2. C0MBINED INTO 1 DATAFRAME
    df = pd.concat(dfs, ignore_index=True)
    
    # Filter: ONLY TAKE LINES WITH "Pink Morsel"
    # USES .strip() dan .lower() to make filter more accurate
    df = df[df['product'].str.strip().str.lower() == 'pink morsel']
    
    # 3. Transformation: Count Sales (quantity * price)
    # Clean symbol of '$' in price column ?
    if df['price'].dtype == 'object':
        df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
    
    df['sales'] = df['quantity'] * df['price']
    
    # 4. Column Selection: ONLY SALES, DATE, AND REGION
    final_df = df[['sales', 'date', 'region']]
    
    # 5. EXPORT FINAL OUTPUT TO CSV !!
    final_df.to_csv(output_filename, index=False)
    print(f"Success! '{output_filename}' has been generated.")

if __name__ == "__main__":
    process_soul_foods_data()