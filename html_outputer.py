"""
网页解析结果输出
"""
class HtmlOutputer():

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w',  encoding='utf-8')
        fout.write("<html>")
        fout.write("<head>")
        fout.write(r'<meta content="text/html"; charset="utf-8">')
        fout.write("<title>Spider爬虫</title>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")

            fout.write("<td>%s</td>" % data['url'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['title']) #.encode('utf-8')
            fout.write("<td>%s</td>" % data['summary']) #.encode('utf-8')

            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
