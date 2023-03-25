from flask import Flask, render_template, request
import chardet
app = Flask(__name__)

@app.route('/')
@app.route('/<filename>')
def display_file(filename='file1.txt'):
    start_line = request.args.get('start')
    end_line = request.args.get('end')

    try:
        with open(f'data/{filename}', 'rb') as f:
            data = f.read()
            encoding = chardet.detect(data)['encoding']
        
        with open(f'data/{filename}', 'r', encoding=encoding) as f:
            lines = f.readlines()
            if start_line and end_line:
                start = int(start_line) - 1
                end = int(end_line)
                lines = lines[start:end]
            elif start_line:
                start = int(start_line) - 1
                lines = lines[start:]
            elif end_line:
                end = int(end_line)
                lines = lines[:end]
            
            content = ''.join(lines)
            return render_template('file.html', content=content)

    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)

