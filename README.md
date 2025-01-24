**Cu Extraction and Leaching Process Analysis**
This repository contains scripts and data for analyzing the extraction of copper (Cu) using various Fe(II) and (III) solutions under different conditions. 

The project includes:
  Data analysis and visualization
  Calculation of reaction orders
  Interpolation for smoother curves
  Optimization of feed amount in the leaching process

**Table of Contents**
  
  1) Project Overview
  
  2) Data Description
  
  3) Installation
  
  4) Usage
  
  5) Project Structure
  
  6) Dependencies
  
  7) Results
  
  8) Contributing
  
  9) License

**** Description

1) Project Overview: 

The purpose of this project is to optimize the copper extraction process using various leaching reagents, focusing on three different Fe(II) and (III) solution ratios. 

The project is divided into three parts:
  
  i. Optimization of leaching reagent concentration:
    Compare the Cu extraction efficiency with different Fe(II) and Fe(III) solutions.
  
  ii. Reaction order calculation: 
    Fit the experimental data to calculate the reaction order for the optimal leaching solution.
  
  iii. Maximizing e-waste amount as feed: 
    Analyze the effect of increasing PCB feed on Cu extraction.

2) Data Description:

The dataset used in this project contains:
  
  - Duration of extraction
  - Copper extraction percentages for different Fe(II) and Fe(III) solution ratios (25:75, 50:50, 75:25)
  - Copper extraction with the 50:50 Fe solution for different PCB amounts.

The data is stored in a CSV format.

3) Installation:
   
To set up the project locally, follow these steps:

Step 1. Clone the repository:
  
  bash
  Copy code git clone https://github.com/kfatema10/E-wasteRecycle.git
  cd cu-extraction-leaching-process

Step 2. Install the required Python libraries:
  
  bash
  Copy code
  pip install -r requirements.txt

4) Usage:
   
To visualize the copper extraction process with different Fe(II) and Fe(III) solutions, run:
 
  bash
  Copy code
  python analyze_extraction.py

This script-
  
  - Extracts data from the CSV file.
  - Plots Cu extraction over time for different Fe solutions.
  - Calculates the reaction order for the optimal solution (50:50 Fe ratio).
  - Reaction Order Calculation

To calculate and visualize the reaction orders for the 50:50 Fe solution, run:
  
  bash
  Copy code
  python reaction_order.py

This script:

  - Fits curves to the data for zeroth, first, and second reaction orders.
  - Computes the R² values for each order.
  - Visualizes the reaction order graphs.
  - Feed Optimization

To analyze and optimize the PCB feed amount for maximizing Cu extraction, run:
  
  bash
  Copy code
  python optimize_feed.py
  
This script:

  - Interpolates Cu extraction data based on PCB feed amount.
  - Plots the smooth interpolation curve for further analysis.

5) Project Structure:

bash
Copy code
cu-extraction-leaching-process/

─ data.csv                   # Dataset containing extraction information
─ analyze_extraction.py      # Script for visualizing copper extraction process
─ reaction_order.py          # Script for reaction order calculations
─ optimize_feed.py           # Script for optimizing PCB feed amount
─ requirements.txt           # Dependencies required for the project
─ README.md                  # Project documentation

6) Dependencies:

The project uses the following Python libraries:

  i. numpy
  ii. pandas
  iii. matplotlib
  iv. scipy
  v. sklearn

You can install these libraries by running:
  
  bash
  Copy code
  pip install -r requirements.txt

7) Results:

Key Findings
  - Optimum Cu extraction is achieved with a 50:50 Fe(II):(III) solution ratio, yielding 52.34 wt% after 5 days.
  - Reaction order analysis indicates that the reaction follows a first-order mechanism based on the highest R² value.
  - Feed optimization suggests the maximum Cu extraction occurs at an intermediate PCB feed amount.

8) Contributing:

Contributions are welcome! If you would like to contribute to this project, feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

9) Citation:

[(https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4912284) ](https://www.cell.com/heliyon/fulltext/S2405-8440(24)17484-1?uuid=uuid%3A93bf2673-120f-48f1-8981-2a8f9dd0b7fd)
