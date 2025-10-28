from flask import Flask, render_template, abort

app = Flask(__name__)

OPENINGS_DB = {
    'inazuma-eleven': {
        'page_title': 'Inazuma Eleven',
        'openings': {
            'opening1': {
                'title': 'Inazuma Eleven - Opening 1',
                'youtube_id': 'y-vmhUs-iNw'
            },
            'opening2': {
                'title': 'Inazuma Eleven - Opening 2',
                'youtube_id': 'R94KxPsXRCY'
            },
            'opening3': {
                'title': 'Inazuma Eleven - Opening 3',
                'youtube_id': '4NLIHAEtaKM'
            },
            'opening4': {
                'title': 'Inazuma Eleven - Opening 4',
                'youtube_id': 'HEtc3K1BPTs'
            },
            'opening5': {
                'title': 'Inazuma Eleven - Opening 5',
                'youtube_id': 'fCKHThOTvbE'
            },
            'opening6': {
                'title': 'Inazuma Eleven - Opening 6',
                'youtube_id': '-gBkSun0knc'
            }
        }
    },
    'inazuma-go': {
        'page_title': 'Inazuma Eleven GO',
        'openings': {
            'opening1': {'title': 'Inazuma Eleven GO - Opening 1', 'youtube_id': 'LQCTkOF3OuY'},
            'opening2': {'title': 'Inazuma Eleven GO - Opening 2', 'youtube_id': 'v-cGWF1Q-rI'},
            # ... etc.
        }
    },
    # ...Otras temporadas (chrono-stones, galaxy) irían aquí
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inazuma-eleven')
def inazuma_eleven():
    return render_template('inazuma_eleven.html')

@app.route('/inazuma-go')
def inazuma_go():
    return render_template('inazuma_go.html')

@app.route('/inazuma-go-chrono-stones')
def inazuma_go_chrono_stones():
    return render_template('inazuma_go_chrono_stones.html')

@app.route('/inazuma-go-galaxy')
def inazuma_go_galaxy():
    return render_template('inazuma_go_galaxy.html')

@app.route('/<string:season_slug>/<string:opening_id>')
def show_opening(season_slug, opening_id):
    
    season_data = OPENINGS_DB.get(season_slug)
    
    if not season_data:
        abort(404)
        
    opening_data = season_data['openings'].get(opening_id)
    
    if not opening_data:
        abort(404)
        
    return render_template('opening_video.html', 
                           video_title=opening_data['title'], 
                           youtube_id=opening_data['youtube_id'],
                           season_slug=season_slug
                          )




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)