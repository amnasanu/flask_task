Url Routes

Home Page
URL : '/'
Method : get

Specific File Page
URL  : /<filename>
Method : get


Example URLs
http://localhost:5000/ - Displays the content of the default file (file1.txt by default)
http://localhost:5000/?start=1&end=5 - Displays the first 5 lines of the default file.
http://localhost:5000/?start=10 - Displays lines 10 to the end of the default file.
http://localhost:5000/?end=20 - Displays the first 20 lines of the default file
http://localhost:5000/file2.txt - Displays the content of file2.txt.
http://localhost:5000/file3.txt?start=5&end=10 - Displays lines 5 to 10 of file3.txt
