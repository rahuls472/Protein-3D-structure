3D Protein Structure Visualization
This project is a Flask-based web application that allows users to upload PDB files to visualize 3D protein structures. The application leverages BioPython to parse PDB files and Plotly to render interactive 3D structures, displaying both the protein backbone and side chains for enhanced visualization.

Features
Upload PDB Files: Supports uploading of one or multiple PDB files.
3D Visualization: Renders protein structures in 3D, showing both backbone and side chains.
Interactive View: Allows rotation and zooming of 3D structures for detailed examination.

Usage
Upload one or more PDB files by selecting them in the file input.
Click the Generate 3D Structures button to visualize.
Scroll down to view each file’s 3D structure, with color-coded atoms and backbone.


Installation
1. Clone the Repository
   ```bash
     git clone https://github.com/your-username/3d-protein-structure-visualization.git
     cd 3d-protein-structure-visualization
  
2. Create a Virtual Environment
    ```bash
     python3 -m venv venv
     source venv/bin/activate  # For Linux/macOS
     venv\Scripts\activate     # For Windows

3. Install Dependencies Install Flask, BioPython, and Plotly:
   ```bash
     pip install Flask BioPython Plotly

4. Run the Application:
   ```bash
     python app.py

![Screenshot From 2024-10-29 14-33-39](https://github.com/user-attachments/assets/879f470b-0217-4beb-82b3-7ea1a11a608f)
![Screenshot From 2024-10-29 14-33-22](https://github.com/user-attachments/assets/02f2efff-71c2-4936-9875-eaa3ad8b17ff)

