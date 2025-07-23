from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

from chart_analyzer import ChartAnalyzer

analyzer = ChartAnalyzer()

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'chart-screenshot' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['chart-screenshot']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)

        analysis = analyzer.analyze_chart(filepath)
        if analysis:
            # In a real implementation, we would generate a recommendation based on the analysis
            recommendation = {
                "direction": "LONG/SHORT",
                "entry_point": 62350.75,
                "stop_loss": 61800.30,
                "take_profit": [63500.50, 64200.00],
                "confidence_score": 0.98
            }
            return jsonify(recommendation)
        else:
            return jsonify({'error': 'Failed to analyze chart'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
