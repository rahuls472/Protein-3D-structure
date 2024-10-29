from Bio.PDB import PDBParser
import plotly.graph_objs as go

def parse_pdb(file_content):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('protein', file_content)
    backbone_atoms = []
    sidechain_atoms = []

    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    # Check if the atom is a backbone atom
                    if atom.name in ['N', 'CA', 'C', 'O']:
                        backbone_atoms.append(atom.coord)
                    else:
                        sidechain_atoms.append(atom.coord)

    return backbone_atoms, sidechain_atoms

def create_3d_plot(backbone_atoms, sidechain_atoms):
    # Handle case with no atoms
    if not backbone_atoms and not sidechain_atoms:
        return None

    # Prepare backbone and side chain coordinates
    x_back, y_back, z_back = zip(*backbone_atoms) if backbone_atoms else ([], [], [])
    x_side, y_side, z_side = zip(*sidechain_atoms) if sidechain_atoms else ([], [], [])

    # Create the backbone trace
    backbone_trace = go.Scatter3d(
        x=x_back,
        y=y_back,
        z=z_back,
        mode='lines',
        line=dict(
            width=4,
            color='blue'  # Color for the backbone
        ),
        name='Backbone'
    )

    # Create the side chain trace
    sidechain_trace = go.Scatter3d(
        x=x_side,
        y=y_side,
        z=z_side,
        mode='markers',
        marker=dict(
            size=5,
            color='orange',  # Color for the side chains
            opacity=0.8
        ),
        name='Side Chains'
    )

    # Layout for the plot
    layout = go.Layout(
        title="3D Protein Structure",
        scene=dict(
            xaxis=dict(title='X'),
            yaxis=dict(title='Y'),
            zaxis=dict(title='Z')
        )
    )

    # Create figure with both traces
    fig = go.Figure(data=[backbone_trace, sidechain_trace], layout=layout)
    return fig.to_html(full_html=False)
