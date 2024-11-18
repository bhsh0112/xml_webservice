from flask import request, Flask, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)

# 允许所有域名跨域访问
CORS(app)

# 模拟存储用户的学习时长数据
study_time_data = {
    'daily': 2,
    'weekly': 0
}

# 定义北京航空航天大学新主楼的经纬度范围
bounding_box = {
    'north': 39.990489,
    'south': 39.990120,
    'east': 116.34357,
    'west': 116.34306
}

@app.route('/webservice/timer', methods=['POST'])
def timer():
    data = request.get_json()  # 解析JSON格式的数据
    latitude = data['latitude']
    longitude = data['longitude']

    # 检查用户是否在指定区域内
    if is_within_bounding_box(latitude, longitude):
        # 用户在区域内，更新学习时长
        study_time_data['daily'] += 1
        study_time_data['weekly'] += 1

    return jsonify({
        'dailyTime': study_time_data['daily'],
        'weeklyTime': study_time_data['weekly']
    })

def is_within_bounding_box(lat, lon):
    return (bounding_box['south'] <= lat <= bounding_box['north']) and (bounding_box['west'] <= lon <= bounding_box['east'])

if __name__ == '__main__':
    app.run(debug=True)