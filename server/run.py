from flask import Flask, request, jsonify
from e_genomic.pipeline_data_class import Pipeline
from e_genomic.batch_loader_class import BatchLoader

app = Flask(__name__)


@app.route('/pipeline', methods=['POST'])
def pipeline():
    if request.method == 'POST':
        result = Pipeline().run()
        if result['status'] == 'success':
            return jsonify(result), 200
        else:
            return jsonify(result), 500


@app.route('/batch', methods=['POST'])
def bacther_loader():
    if request.method == 'POST':
        result = BatchLoader().run()
        if result['status'] == 'success':
            return jsonify(result), 200
        else:
            return jsonify(result), 500


def run_server():
    app.run(port=5000)


if __name__ == '__main__':
    run_server()
