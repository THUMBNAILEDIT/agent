from supabase import create_client, Client

url = "https://kblrsiucjbjucnyvftsz.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtibHJzaXVjamJqdWNueXZmdHN6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjc3MTAzMjAsImV4cCI6MjA0MzI4NjMyMH0.bVfKoXML0OObYzfgx36m7w6qtJooO5zg7zSWTFx89kM"
supabase: Client = create_client(url, key)


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    video_description = request.form['description']
    niche = request.form['niche']

    data = supabase.table('Video Data').insert({
        "video_description": video_description,
        "niche": niche
    }).execute()

    return render_template('submit.html', video_description=video_description, niche=niche)


if __name__ == '__main__':
    app.run(debug=True)
