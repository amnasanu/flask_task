from flask import Flask, render_template, request
import chardet
app = Flask(__name__)

@app.route('/')
@app.route('/<filename>')
def display_file(filename='file1.txt'):
    start_line = request.args.get('start')
    end_line = request.args.get('end')

    try:
        # Open the specified file in binary mode and read its content
        with open(f'data/{filename}', 'rb') as f:
            data = f.read()
            # Detect the encoding of the file
            encoding = chardet.detect(data)['encoding']

        # Re-open the file in text mode with the detected encoding and read its lines
        with open(f'data/{filename}', 'r', encoding=encoding) as f:
            lines = f.readlines()
            #If both start and end line are specified
            if start_line and end_line:
                start = int(start_line) - 1
                end = int(end_line)
                lines = lines[start:end]
            #If only start line is specified
            elif start_line:
                start = int(start_line) - 1
                lines = lines[start:]
            # If only end line is specified
            elif end_line:
                end = int(end_line)
                lines = lines[:end]
            # Join the lines into a single string
            content = ''.join(lines)
            # Render the file.html template with the content of the file
            return render_template('file.html', content=content)
        
    # If there was an error reading the file render the error.html template with the error message
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)

