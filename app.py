from flask import Flask, jsonify, render_template, request
from decouple import config
import requests

app = Flask(__name__)

UNSPLASH_API_URL = "https://api.unsplash.com"
UNSPLASH_ACCESS_KEY = config('UNSPLASH_ACCESS_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/images')
def get_images():
    page = request.args.get('page', 1, type=int)
    query = request.args.get('query', '')
    per_page = 20
    
    headers = {
        'Authorization': f'Client-ID {UNSPLASH_ACCESS_KEY}'
    }
    
    # Always use search endpoint for consistency
    endpoint = f"{UNSPLASH_API_URL}/search/photos"
    
    params = {
        'page': page,
        'per_page': per_page,
        'query': query or 'featured',  # Use 'featured' as fallback if no query
        'order_by': 'relevant'
    }
    
    response = requests.get(endpoint, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        formatted_images = [{
            'id': img['id'],
            'url': img['urls']['regular'],
            'thumb': img['urls']['thumb'],
            'alt': img['alt_description'] or f'Image of {query}',
            'width': img['width'],
            'height': img['height']
        } for img in data['results']]
        return jsonify(formatted_images)
    
    return jsonify({'error': 'Failed to fetch images'}), 500

if __name__ == '__main__':
    app.run(debug=True) 