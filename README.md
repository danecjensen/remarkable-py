# Pinterest-Style Image Gallery

A responsive masonry layout image gallery with infinite scroll, built with Flask and the Unsplash API.

## Features

- Responsive masonry grid layout
- Infinite scroll loading
- Progressive image loading (thumbnails first, then high quality)
- Smooth animations and hover effects
- "Scroll to top" button
- Optimized performance with lazy loading

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your Unsplash API key:
   ```
   UNSPLASH_ACCESS_KEY=your_unsplash_access_key_here
   FLASK_ENV=development
   FLASK_DEBUG=1
   ```
   Get your API key from [Unsplash Developers](https://unsplash.com/developers)

5. Run the application:
   ```bash
   python app.py
   ```
6. Open http://localhost:5000 in your browser

## Performance Considerations

- Images are loaded progressively (thumbnail first, then high quality)
- Lazy loading is implemented for images
- Infinite scroll loads images in batches of 20
- Debounced scroll event handling
- Optimized CSS animations

## Technologies Used

- Backend: Flask
- Frontend: Vanilla JavaScript
- API: Unsplash
- Styling: CSS Grid and Flexbox 