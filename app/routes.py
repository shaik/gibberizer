"""
API routes for the Gibberizer application.
"""
from flask import Blueprint, jsonify, request, current_app, render_template
from pathlib import Path
from modules.data_reader import get_reader
from modules.gibberish_generator import create_generator


bp = Blueprint("api", __name__)


@bp.route("/files", methods=["GET"])
def list_files():
    """List available text files in the data directory."""
    try:
        reader = get_reader(data_dir=str(Path(current_app.root_path).parent / "data"))
        files = reader.list_sources()
        return jsonify({"files": files})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/content/<filename>", methods=["GET"])
def get_content(filename):
    """Get content of a specific text file."""
    try:
        reader = get_reader(data_dir=str(Path(current_app.root_path).parent / "data"))
        content = reader.read_text(filename)
        return jsonify({"content": content})
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/gibberize", methods=["POST"])
def gibberize():
    """Generate gibberish text from specified source."""
    try:
        data = request.get_json()
        if not data or "source" not in data:
            return jsonify({"error": "Missing source parameter"}), 400
        
        # Get source text
        reader = get_reader(data_dir=str(Path(current_app.root_path).parent / "data"))
        text = reader.read_text(data["source"])
        
        # Create generator with optional parameters
        generator_params = {
            k: v for k, v in data.items()
            if k in ["min_chunk_size", "max_chunk_size"]
        }
        generator = create_generator(**generator_params)
        
        # Generate gibberish with optional randomness parameter
        randomness = data.get("randomness", 0.7)
        result = generator.generate(text, randomness=randomness)
        
        return jsonify({"result": result})
    except FileNotFoundError:
        return jsonify({"error": "Source file not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/", methods=["GET"])
def index():
    data_dir = Path(current_app.root_path).parent / "data"
    files = [f.name for f in data_dir.glob("*.txt")]
    return render_template("index.html", files=files)


@bp.route("/generate", methods=["POST"])
def generate():
    selected_file = request.form["file"]
    word_count = int(request.form["word_count"])
    word_count = min(word_count, 1000)
    min_chunk_size = int(request.form.get("min_chunk_size", 3))
    max_chunk_size = int(request.form.get("max_chunk_size", 3))

    if min_chunk_size > max_chunk_size:
        min_chunk_size, max_chunk_size = max_chunk_size, min_chunk_size

    reader = get_reader(data_dir=str(Path(current_app.root_path).parent / "data"))
    text = reader.read_text(selected_file)
    generator = create_generator(min_chunk_size=min_chunk_size, max_chunk_size=max_chunk_size)
    gibberish = generator.generate(text)

    words = gibberish.split()
    if len(words) > word_count:
        gibberish = " ".join(words[:word_count])

    data_dir = Path(current_app.root_path).parent / "data"
    files = [f.name for f in data_dir.glob("*.txt")]
    return render_template("index.html", files=files, gibberish=gibberish, selected_file=selected_file, word_count=word_count, min_chunk_size=min_chunk_size, max_chunk_size=max_chunk_size)
