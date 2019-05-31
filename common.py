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
        {'id':1, 'title':'新闻1', 'add_time':'2019-05-30 18:08:33', 'zhaiyao':'新闻摘要1','click':8},
        {'id':2, 'title':'新闻2', 'add_time':'2019-05-30 17:39:33', 'zhaiyao':'新闻摘要2','click':6},
        {'id':3, 'title':'新闻3', 'add_time':'2019-05-30 10:33:39', 'zhaiyao':'新闻摘要3','click':4},
    ]
}
response_newsinfo = {
    'status' : 0,
    'messages' : [
        {'id': 1, 'title': '猛龙胜勇士1-0', 'add_time': '2019-05-31', 'content': '  库里开局不久造成伦纳德投篮犯规，2罚全中，完成2019年总决赛首次得分，但猛龙很快由丹尼-格林三分还以颜色。双方一番缠斗后，小加利用勇士放空的机会，连续在外线投中三分，帮助猛龙18-11取得领先。'
                                                                            '  关键时刻，库里利用汤普森无球掩护，投中本场比赛第2个三分，这是他在总决赛投中的第100个三分，成为NBA历史上首个完成这个成就的球员。库里其后又在左侧底角投中三分，率队打出一个8-0攻击波，勇士19-18反超比分。'
                                                                            '  勇士第三节开局三分投得不错，库里和汤普森先后投中三分，帮助勇士61-67迫近比分。在随后的比赛中，西亚卡姆展现出出色的进攻天赋，里突外投不断得分，帮助猛龙79-68重新取得11分领先优势。'
                                                                            '  西亚卡姆第三节6投全中，单节得到14分，将个人得分提高到26分，伦纳德第三节5投2中，罚球6罚5中单节得到10分，将个人得分提高到18分。勇士这边，库里14投6中，三分8投4中得到26分3篮板2助攻。'
                                                                            '  第四节进行到7分32秒，猛龙再次发动快攻反击，西亚卡姆突破分球，助攻空位的丹尼-格林投中三分，猛龙100-88将领先优势扩大到12分。勇士请求暂停后连得4分，但伦纳德错位单打三分得手，猛龙重新取得10分以上的优势并拿下比赛。', 'click': 8},
        {'id': 2, 'title': '新闻2', 'add_time': '2019-05-30', 'content': '详细内容2', 'click': 4},
        {'id': 3, 'title': '新闻3', 'add_time': '2019-05-30', 'content': '详细内容3', 'click': 6},
    ]
}
response_comment_1 = {
  'messages' : [
    {'user_name' : '匿名用户', 'addtime': '2019-05-31 13:13:00', 'content': '评论一下'},
    {'user_name' : '匿名用户', 'addtime': '2019-05-31 13:14:00', 'content': '哈哈哈'},
    {'user_name' : '匿名用户', 'addtime': '2019-05-31 13:15:00', 'content': '你好'},
    {'user_name' : '匿名用户', 'addtime': '2019-05-31 13:16:00', 'content': '我的朋友'},
    {'user_name' : '匿名用户', 'addtime': '2019-05-31 13:19:00', 'content': '123'}
  ]
}
response_comment_2 = {
  'messages' : [
    {'user_name' : '匿名用户', 'addtime': '2019-05-31 13:13:00', 'content': '北京'},
    {'user_name' : '匿名用户', 'addtime': '2019-05-31 13:14:00', 'content': '上海'},
    {'user_name' : '匿名用户', 'addtime': '2019-05-31 13:15:00', 'content': '广州'},
    {'user_name' : '匿名用户', 'addtime': '2019-05-31 13:16:00', 'content': '深圳'},
    {'user_name' : '匿名用户', 'addtime': '2019-05-31 13:19:00', 'content': '456'}
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
    obj = response_newsinfo['messages'][newid - 1]
    resp = jsonify({'status':0, 'message':obj})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/api/getcomments/<int:pageIndex>', methods=['GET'])
def news_info(pageIndex):
    if pageIndex == 1:
      resp = jsonify(response_comment_1)
      resp.headers['Access-Control-Allow-Origin'] = '*'
      return resp
    if pageIndex == 2:
      resp = jsonify(response_comment_2)
      resp.headers['Access-Control-Allow-Origin'] = '*'
      return resp

if __name__ == '__main__':
    # 这样使得外网也可以访问
    # app.run(host='0.0.0.0')

    # 每次修改后不用重启，不能用于生产环境
    # app.run(debug=True)

    app.run()

















