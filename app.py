from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# تحميل القنوات من ملف JSON
def load_channels():
    if os.path.exists('channels.json'):
        with open('channels.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return [
        {"name": "Al-Hurra Iraq", "url": "https://mbnvvideoingest-i.akamaihd.net/hls/live/1004674/MBNV_ALHURRA_IRAQ/playlist.m3u8", "category": "أخبار"},
        {"name": "Al-Hurra", "url": "https://mbnvvideoingest-i.akamaihd.net/hls/live/1004673/MBNV_ALHURRA_MAIN/playlist.m3u8", "category": "أخبار"},
        {"name": "Al-Iraqiya", "url": "https://cdn.catiacast.video/abr/8d2ffb0aba244e8d9101a9488a7daa05/playlist.m3u8", "category": "أخبار"},
        {"name": "Al-Rafidain", "url": "https://cdg8.edge.technocdn.com/arrafidaintv/abr_live/playlist.m3u8", "category": "أخبار"},
        {"name": "Al-Rasheed", "url": "https://media1.livaat.com/AL-RASHEED-HD/tracks-v1a1/playlist.m3u8", "category": "ترفيه"},
        {"name": "Al-Sharqiya News", "url": "https://5d94523502c2d.streamlock.net/alsharqiyalive/mystream/playlist.m3u8", "category": "أخبار"},
        {"name": "Al-Sharqiya", "url": "https://5d94523502c2d.streamlock.net/home/mystream/playlist.m3u8", "category": "ترفيه"},
        {"name": "Dijlah Tarab", "url": "https://ghaasiflu.online/tarab/tracks-v1a1/playlist.m3u8", "category": "ترفيه"},
        {"name": "Dijlah TV", "url": "https://ghaasiflu.online/Dijlah/tracks-v1a1/playlist.m3u8", "category": "أخبار"},
        {"name": "iNEWS", "url": "https://svs.itworkscdn.net/inewsiqlive/inewsiq.smil/playlist.m3u8", "category": "أخبار"},
        {"name": "Iraq Future Ⓢ", "url": "https://streaming.viewmedia.tv/viewsatstream40/viewsatstream40.smil/playlist.m3u8", "category": "أخبار"},
        {"name": "Turkmeneli TV", "url": "https://137840.global.ssl.fastly.net/edge/live_6b7c6e205afb11ebb010f5a331abaf98/playlist.m3u8", "category": "أخبار"},
        {"name": "Zagros TV", "url": "https://5a3ed7a72ed4b.streamlock.net/zagrostv/SMIL:myStream.smil/playlist.m3u8", "category": "أخبار"},
    ]

# حفظ القنوات في ملف JSON
def save_channels(channels):
    with open('channels.json', 'w', encoding='utf-8') as f:
        json.dump(channels, f, ensure_ascii=False, indent=4)

# تحميل القنوات عند بدء التشغيل
channels = load_channels()

# الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html', channels=channels)

# صفحة الفئة
@app.route('/category/<category>')
def category(category):
    filtered_channels = [channel for channel in channels if channel['category'] == category]
    return render_template('index.html', channels=filtered_channels)

# إضافة قناة جديدة
@app.route('/add_channel', methods=['GET', 'POST'])
def add_channel():
    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        category = request.form['category']
        channels.append({"name": name, "url": url, "category": category})
        save_channels(channels)
        flash('تمت إضافة القناة بنجاح!', 'success')
        return redirect(url_for('index'))
    return render_template('add_channel.html')

if __name__ == '__main__':
    app.run(debug=True)
