from flask import Flask, render_template

app = Flask(__name__)

# قائمة القنوات
channels = [
    {"name": "Al-Hurra Iraq", "url": "https://mbnvvideoingest-i.akamaihd.net/hls/live/1004674/MBNV_ALHURRA_IRAQ/playlist.m3u8"},
    {"name": "Al-Hurra", "url": "https://mbnvvideoingest-i.akamaihd.net/hls/live/1004673/MBNV_ALHURRA_MAIN/playlist.m3u8"},
    {"name": "Al-Iraqiya", "url": "https://cdn.catiacast.video/abr/8d2ffb0aba244e8d9101a9488a7daa05/playlist.m3u8"},
    {"name": "Al-Rafidain", "url": "https://cdg8.edge.technocdn.com/arrafidaintv/abr_live/playlist.m3u8"},
    {"name": "Al-Rasheed", "url": "https://media1.livaat.com/AL-RASHEED-HD/tracks-v1a1/playlist.m3u8"},
    {"name": "Al-Sharqiya News", "url": "https://5d94523502c2d.streamlock.net/alsharqiyalive/mystream/playlist.m3u8"},
    {"name": "Al-Sharqiya", "url": "https://5d94523502c2d.streamlock.net/home/mystream/playlist.m3u8"},
    {"name": "Dijlah Tarab", "url": "https://ghaasiflu.online/tarab/tracks-v1a1/playlist.m3u8"},
    {"name": "Dijlah TV", "url": "https://ghaasiflu.online/Dijlah/tracks-v1a1/playlist.m3u8"},
    {"name": "iNEWS", "url": "https://svs.itworkscdn.net/inewsiqlive/inewsiq.smil/playlist.m3u8"},
    {"name": "Iraq Future Ⓢ", "url": "https://streaming.viewmedia.tv/viewsatstream40/viewsatstream40.smil/playlist.m3u8"},
    {"name": "Turkmeneli TV", "url": "https://137840.global.ssl.fastly.net/edge/live_6b7c6e205afb11ebb010f5a331abaf98/playlist.m3u8"},
    {"name": "Zagros TV", "url": "https://5a3ed7a72ed4b.streamlock.net/zagrostv/SMIL:myStream.smil/playlist.m3u8"},
]

# الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html', channels=channels)

if __name__ == '__main__':
    app.run(debug=True)
