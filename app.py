from flask import Flask, render_template, request, redirect, url_for
from bio import parse_pdb, create_3d_plot
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    files = request.files.getlist('pdb_files')
    plots = []

    for file in files:
        if file and file.filename.endswith('.pdb'):
            file_content = io.StringIO(file.stream.read().decode("utf-8"))
            backbone_atoms, sidechain_atoms = parse_pdb(file_content)
            plot_html = create_3d_plot(backbone_atoms, sidechain_atoms)
            plots.append((file.filename, plot_html))

    return render_template('index.html', plots=plots)

if __name__ == '__main__':
    app.run(debug=True)
