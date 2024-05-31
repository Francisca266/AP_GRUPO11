from flask import Flask, render_template, request, url_for, jsonify
import pandas as pd

app = Flask(__name__)

dataset_path = 'results_medical.csv'
df = pd.read_csv(dataset_path)

audio_files = df['file'].tolist()
pred_texts = df['pred_text'].tolist()
original_texts = df['sentence'].tolist()


app.jinja_env.globals.update(enumerate=enumerate)

def highlight_differences(original_text, predicted_text):
    original_words = original_text.split(' ')
    predicted_words = predicted_text.split(' ')

    original_highlighted = []
    predicted_highlighted = []

    original_length = len(original_words)
    predicted_length = len(predicted_words)

    i, j = 0, 0

    while i < original_length and j < predicted_length:
        if original_words[i] == predicted_words[j]:
            original_highlighted.append(original_words[i])
            predicted_highlighted.append(predicted_words[j])
            i += 1
            j += 1
        else:
            original_highlighted.append(f'<span class="highlight-green">{original_words[i]}</span>')
            predicted_highlighted.append(f'<span class="highlight-red">{predicted_words[j]}</span>')

            i += 1
            j += 1
            if i < (original_length - 1) and original_words[i + 1] == predicted_words[j]:
                original_highlighted.append(f'<span class="highlight-green">{original_words[i]}</span>')
                i += 1
                
    return ' '.join(original_highlighted), ' '.join(predicted_highlighted)


@app.route('/')
def index():
    original_highlighted, predicted_highlighted = highlight_differences(original_texts[0], pred_texts[0])
    return render_template('index.html', 
                           audio_files=audio_files, 
                           pred_texts=pred_texts, 
                           audio=audio_files[0], 
                           pred_text=predicted_highlighted, 
                           original_text=original_highlighted)


@app.route('/audio', methods=['POST'])
def index_p():
    file_index = int(request.form['file_index'])
    return jsonify({'url': url_for('static', filename=df.iloc[file_index]['file']), 'original': df.iloc[file_index]['sentence'], 'predicted': df.iloc[file_index]['pred_text']})


if __name__ == '__main__':
    app.run(debug=True)
