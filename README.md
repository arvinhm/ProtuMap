# ProtuMap
ProtuMap: Protein Expression Map

ProtuMap is a software tool that uses the Human Protein Atlas IHC-based database to explore protein level expression in different tissues. It involves a robust number of proteins, more than 13,000, providing a comprehensive view of protein expression across various tissues.

## Features

- Search for gene expression levels in different tissues.
- Visualize gene expression levels using bar charts.

## Installation

Follow these steps to set up the environment and run the software:

1. **Create the Conda environment**:
    ```sh
    conda env create -f environment.yml
    ```

2. **Activate the Conda environment**:
    ```sh
    conda activate gene_expression_env
    ```

3. **Clone the GitHub repository**:
    ```sh
    git clone https://github.com/arvinhm/ProtuMap.git
    ```

4. **Navigate to the project directory**:
    ```sh
    cd ProtuMap
    ```

## Usage

1. **Change the gene name in `main_script.py`**:
    Edit the `main_script.py` file and replace `YOUR_GENE_NAME_HERE` with the gene name you want to search for.

2. **Run the code**:
    ```sh
    python main_script.py
    ```
![Diagram](figures/RCOR1.png)

