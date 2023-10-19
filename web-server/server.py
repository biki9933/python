#-*- coding:utf-8 -*-
import sys,os
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    '''处理请求并返回页面'''

    # 页面模板
    Page= '''\
    <html>
    <body>
    <table>
    <tr> <td>Header</td>    <td>Value</td>      </tr>
    <tr> <td>Date and time</td> <td>{date_time}</td>  </tr>
    <tr> <td>Client host</td>  <td>{client_host}</td> </tr>
    <tr> <td>Client port</td> <td>{client_port}</td> </tr>
    <tr> <td>Command</td>   <td>{command}</td>     </tr>
    <tr> <td>Path</td> <td>{path}</td> </tr>
    </table>
    </body>
    </html>
    '''


    # Page = '''\
    #     <html>
    #     <body>
    #     <p>Hello, web!</p>
    #     </body>
    #     </html>
    # '''

    # 处理一个GET请求
    # def do_GET(self):
    #     self.send_response(200)
    #     self.send_header("Content-Type","text/html")
    #     self.send_header("Content-Length",str(len(self.Page)))
    #     self.end_headers()
    #     self.wfile.write(self.Page.encode('utf-8'))
    #
    # def do_GET(self):
    #     page = self.create_page()
    #     self.send_content(page)

    def do_GET(self):
        try:
            # 文件完整路径
            full_path = os.getcwd() + self.path

            #如果该路径不存在...
            if not os.path.exists(full_path):
                raise ServerException("'{0}' not found".format(self.path))
                #抛出异常：文件未找到






        #



    def create_page(self):
        values = {
            'date_time': self.date_time_string(),
            'client_host': self.client_address[0],
            'client_port': self.client_address[1],
            'command': self.command,
            'path': self.path
        }
        page = self.Page.format(**values)
        return page

    def send_content(self, page):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page.encode('utf-8'))

    class ServerException(Exception):
        '''服务器内部错误'''
        pass


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
