import pandas as pd
import matplotlib.pyplot as plt

def load_expression_data():
    not_detected_file = r'source/not_detected_genes_by_tissue_normal.csv'
    high_file = r'source/high_genes_by_tissue.csv'
    medium_file = r'source/medium_genes_by_tissue.csv'
    low_file = r'source/low_genes_by_tissue.csv'

    not_detected_df = pd.read_csv(not_detected_file)
    high_df = pd.read_csv(high_file)
    medium_df = pd.read_csv(medium_file)
    low_df = pd.read_csv(low_file)
    
    return not_detected_df, high_df, medium_df, low_df


def search_gene_expression(gene):
    not_detected_df, high_df, medium_df, low_df = load_expression_data()
    
    # Initialize dictionaries to store tissues for each expression level
    not_detected_tissues = []
    high_tissues = []
    medium_tissues = []
    low_tissues = []

    # Search for the gene in each DataFrame
    for col in not_detected_df.columns:
        if gene in not_detected_df[col].values:
            not_detected_tissues.append(col)
    
    for col in high_df.columns:
        if gene in high_df[col].values:
            high_tissues.append(col)
    
    for col in medium_df.columns:
        if gene in medium_df[col].values:
            medium_tissues.append(col)
    
    for col in low_df.columns:
        if gene in low_df[col].values:
            low_tissues.append(col)
    
    # Print the results
    print(f"Gene: {gene}")
    if not_detected_tissues:
        print(f"Not detected in: {', '.join(not_detected_tissues)}")
    else:
        print("Not detected in: None")
    
    if high_tissues:
        print(f"High expression in: {', '.join(high_tissues)}")
    else:
        print("High expression in: None")
    
    if medium_tissues:
        print(f"Medium expression in: {', '.join(medium_tissues)}")
    else:
        print("Medium expression in: None")
    
    if low_tissues:
        print(f"Low expression in: {', '.join(low_tissues)}")
    else:
        print("Low expression in: None")
    
    generate_expression_visualization(gene, high_tissues, medium_tissues, low_tissues, not_detected_tissues)

def generate_expression_visualization(gene, high_tissues, medium_tissues, low_tissues, not_detected_tissues):
    # Count the number of tissues in each expression level
    counts = {
        'High': len(high_tissues),
        'Medium': len(medium_tissues),
        'Low': len(low_tissues),
        'Not detected': len(not_detected_tissues)
    }
    
    levels = list(counts.keys())
    values = list(counts.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(levels, values, color=['blue', 'orange', 'green', 'red'])
    plt.xlabel('Expression Level')
    plt.ylabel('Number of Tissues')
    plt.title(f'Expression Levels of {gene} Across Tissues')
    plt.show()
