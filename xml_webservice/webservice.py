from flask import Flask, request, jsonify
import requests
import xmltodict

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.data
    # 将XML转换为Python字典
    data_dict = xmltodict.parse(data)
    
    # 构造调用生成式大模型API所需的请求
    api_request = {
        'prompt': data_dict['question'],
        # 其他必要的字段
    }
    
    # 调用生成式大模型API
    response = requests.post('https://kimi.moonshot.cn/', json=api_request)
    
    # 将API的JSON响应转换为XML
    xml_response = '<?xml version="1.0" encoding="UTF-8"?><response>{}</response>'.format(response.json()['answer'])
    
    return xml_response, 200

if __name__ == '__main__':
    app.run(debug=True)