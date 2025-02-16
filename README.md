# Gibberizer

Gibberizer is a fun and experimental web application that generates gibberish text from a given source file. The app uses a unique approach to randomly chunk and shuffle text segments, resulting in playful, semi-coherent gibberish that can entertain and inspire creative thinking.

## Motivation

The project was conceived as an exploration of text processing and randomization techniques. It provides an engaging way to experiment with language by:
- Extracting n-grams or random-length word chunks from a source text.
- Reordering these chunks based on a user-specified randomness factor.
- Displaying the resulting gibberish text in a user-friendly interface.

This creative tool is perfect for developers and language enthusiasts alike who are curious about the intersection of algorithmic manipulation and natural language.

## How It Works

1. **User Interface:**  
   The frontend (built with HTML, CSS, and Flask templates) offers a form where users can:
   - Select a source text file.
   - Set the number of words to generate (up to 1000).
   - Specify the minimum and maximum chunk sizes (between 2 and 10) to control the random segmentation of text.
  
2. **Backend Processing:**  
   - The Flask backend reads the selected text file from a designated data directory.
   - The text is split into chunks of random length between the specified minimum and maximum sizes.
   - Some of these chunks are randomly reordered (based on a randomness parameter) to create the final gibberish text.
   - The generated text is then truncated to the specified word count and sent back to the frontend.

3. **Deployment:**  
   The app is containerized and deployed on Heroku. A `Procfile` and Gunicorn are used to run the application in a production environment.

## Project Structure

- **app/**  
  Contains the Flask application code, including:
  - `__init__.py`: Application factory.
  - `routes.py`: API endpoints and view routes.
  - `templates/`: HTML templates (e.g., `index.html`).
  - `static/`: Static assets like CSS.
  
- **modules/**  
  Contains supporting modules for:
  - Text reading and data handling (`data_reader.py`).
  - Gibberish generation logic (`gibberish_generator.py`).
  
- **tests/**  
  Unit tests to verify the functionality of the gibberish generator.

- **Procfile & requirements.txt:**  
  Configuration files for deployment on Heroku.

## How It Was Built

This project was developed using prompt engineering techniques. Detailed instructions were provided to an AI LLM (ChatGPT) and guided by Windsurf to generate the code and structure for this application. The collaboration between human insight and AI assistance resulted in a clean, modular, and efficient codebase.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Gunicorn (for deployment)
- Heroku CLI (for deployment)

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gibberizer.git
   cd gibberizer
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Set the necessary environment variables (e.g., FLASK_APP, FLASK_ENV).
4. Run the application locally:
   ```bash
   flask run
   ```

### Deployment to Heroku

1. Ensure you have a `Procfile` and that all dependencies (including Gunicorn) are listed in `requirements.txt`.
2. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```
3. Push your code to Heroku:
   ```bash
   git push heroku master
   ```
4. Monitor the logs:
   ```bash
   heroku logs --tail
   ```
5. Open your deployed app:
   ```bash
   heroku open
   ```

## Future Enhancements

- Add client-side validation to the form inputs.
- Expand the text processing options for more advanced gibberish generation.
- Implement user authentication and custom file uploads.

## Acknowledgements

- Built with Flask, Gunicorn, and other open-source libraries.
- Developed with the assistance of detailed prompts provided to an AI LLM (ChatGPT) and guided by Windsurf.
- Special thanks to the community for continuous support and contributions.