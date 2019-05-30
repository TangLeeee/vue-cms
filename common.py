from flask import Flask,jsonify
app = Flask(__name__)

response_index = {
    'status' : 0,
    'messages' : [
        {'id':1, 'img':'https://uploadbeta.com/api/pictures/random/'},
        {'id':2, 'img':'https://uploadbeta.com/api/pictures/random/?key=BingEverydayWallpaperPicture'},
        {'id':3, 'img':'http://acg.bakayun.cn/randbg.php?Type=&t=&https='},
    ]
}
response_newslist = {
    'status' : 0,
    'messages' : [
        {'id':1, 'title':'新闻1', 'add_time':'2019-05-30', 'zhaiyao':'新闻摘要1','click':8},
        {'id':2, 'title':'新闻2', 'add_time':'2019-05-30', 'zhaiyao':'新闻摘要2','click':6},
        {'id':3, 'title':'新闻3', 'add_time':'2019-05-30', 'zhaiyao':'新闻摘要3','click':4},
    ]
}
response_newsinfo = {
    'status' : 0,
    'messages' : [
        {'id': 1, 'title': '新闻1', 'add_time': '2019-05-30', 'content': '详细内容1', 'click': 8},
        {'id': 2, 'title': '新闻2', 'add_time': '2019-05-30', 'content': '详细内容2', 'click': 4},
        {'id': 3, 'title': '新闻3', 'add_time': '2019-05-30', 'content': '详细内容3', 'click': 6},
    ]
}
@app.route('/', methods=['GET'])
def data():
    resp = jsonify(response_index)
    # set response heades to avoid being blocked by CORS policy
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/api/getnewslist', methods=['GET'])
def data_news():
    resp = jsonify(response_newslist)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/api/getnew/<int:newid>', methods=['GET'])
def data_info(newid):
    obj = response_newsinfo['messages'][newid-1]
    resp = jsonify({'status':0, 'message':obj})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run()


















