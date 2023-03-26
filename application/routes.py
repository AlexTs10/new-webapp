from flask import render_template, request, redirect, url_for 
from flask import jsonify
from application import app, db 
from application.models import DailyTemperature
from datetime import date, datetime 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store_temperature', methods=['POST'])
def store_temperature():
    data = request.get_json()
    minute_temp = DailyTemperature(timestamp=datetime.utcnow().replace(second=0, microsecond=0), temperature=data['temperature'])
    db.session.add(minute_temp)
    db.session.commit()

    return {'result': 'success'}

@app.route('/get_temperature/<string:timestamp_str>', methods=["GET"])
def get_temperature(timestamp_str):
    try:
        timestamp_obj = datetime.strptime(timestamp_str, "%Y-%m-%d-%H-%M")
    except ValueError:
        return {'error': 'Invalid timestamp format.'}, 400

    minute_temp = DailyTemperature.query.filter_by(timestamp=timestamp_obj).first()

    if minute_temp:
        return jsonify({'timestamp': timestamp_str, 'temperature': minute_temp.temperature})
    else:
        return {'error': f'No temp data found for {timestamp_str}'}, 404 
    
@app.route('/get_all_temperatures', methods=["GET"])
def get_all_temperatures():
    all_temps = DailyTemperature.query.all()

    # Convert the records to a JSON serializable format
    all_temps_json = [
        {'id': temp.id, 'timestamp': temp.timestamp.strftime('%Y-%m-%d-%H-%M'), 'temperature': temp.temperature}
        for temp in all_temps
    ]

    return jsonify(all_temps_json)

# other routes

