# Gibberizer

A Flask-based application that generates gibberish text from local text files. The application is designed with modularity and extensibility in mind.

## Project Structure

```
gibberizer/
├── app/
│   ├── __init__.py
│   └── routes.py
├── data/
├── modules/
│   ├── __init__.py
│   ├── data_reader.py
│   └── gibberish_generator.py
├── tests/
│   ├── __init__.py
│   ├── test_data_reader.py
│   └── test_gibberish_generator.py
├── requirements.txt
└── README.md
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python -m flask run
```

## API Endpoints

- `GET /api/files` - List available text files
- `GET /api/content/<filename>` - Get content of a specific file
- `POST /api/gibberize` - Generate gibberish text from specified source

## Extending the Application

The application is designed for extensibility:

1. **Data Sources**: Add new data source adapters by implementing the data reader interface in `modules/data_reader.py`
2. **Text Processing**: Modify or extend gibberish generation algorithms in `modules/gibberish_generator.py`

## Testing

Run tests using pytest:
```bash
pytest
```
