# It Depends - Chat Application

This is a simple Flask-based web application that serves a chat interface. The application responds to user messages with a randomly selected response from a predefined list of "It depends" phrases.

## Features

- **Chat Interface**: A web-based interface where users can send messages.
- **Random Responses**: The application always responds with a variation of "It depends."
- **Flask Backend**: Built using the Flask web framework for simplicity and ease of development.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/it_depends.git
   cd it_depends
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000/`.

## File Structure

- **app.py**: The main application file containing the Flask routes and logic.
- **templates/index.html**: The HTML file for the chat interface (not included in this repository yet).
- **static/**: A directory for static assets like CSS and JavaScript (if needed).

## API Endpoints

### `GET /`
Serves the main HTML page for the chat interface.

### `POST /chat`
Handles incoming chat messages and responds with a random "It depends" phrase.

- **Request Body**:
  ```json
  {
    "message": "Your message here"
  }
  ```

- **Response**:
  ```json
  {
    "response": "It depends on the context."
  }
  ```

## Development Notes

- The application is intended for development purposes and uses Flask's built-in server. For production, consider deploying with a WSGI server like Gunicorn or uWSGI.
- Ensure that `index.html` is properly set up in the `templates` directory for the chat interface to work.

## Contributing

Feel free to submit issues or pull requests to improve the application. Contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.