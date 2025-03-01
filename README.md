```md
# Pal-Profile

Pal-Profile is a web application that allows users to manage a list of friends. It is built using a React frontend and a Flask backend, with SQLite as the database.

## Project Structure

```
backend/
	__pycache__/
		app.cpython-313.pyc
		extension.cpython-313.pyc
		models.cpython-313.pyc
		routes.cpython-313.pyc
	app.py
	extension.py
	instance/
		friends.db
	models.py
	routes.py
	tempCodeRunnerFile.py
frontend/
	.gitignore
	eslint.config.js
	index.html
	package.json
	public/
		explode.png
		flask.png
		python.png
		vite.svg
	README.md
	src/
		App.jsx
		components/
			CreateUserModal.jsx
			EditModal.jsx
			Navbar.jsx
			UserCard.jsx
			UserGrid.jsx
		dummy/
			dummy.js
		main.jsx
	vite.config.js
README.md
```

## Backend

The backend is a Flask application that provides a RESTful API for managing friends. It uses SQLAlchemy for database interactions and CORS to allow cross-origin requests.

### Files

- `app.py`: Creates and configures the Flask application.
- `extension.py`: Initializes the SQLAlchemy database instance.
- `models.py`: Defines the `Friend` model.
- `routes.py`: Defines the API routes for managing friends.

### Running the Backend

1. Navigate to the `backend` directory.
2. Install the required dependencies:
   ```sh
   pip install flask flask-cors flask-sqlalchemy
   ```
3. Run the Flask application:
   ```sh
   python app.py
   ```

## Frontend

The frontend is a React application built with Vite. It uses Chakra UI for styling and components.

### Files

- index.html: The main HTML file.
- main.jsx: The entry point for the React application.
- App.jsx: The main App component.
- `src/components/`: Contains the React components used in the application.
- vite.config.js: Configuration file for Vite.

### Running the Frontend

1. Navigate to the frontend directory.
2. Install the required dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm run dev
   ```

## API Endpoints

### Get All Friends

- **URL**: `/api/friends`
- **Method**: `GET`
- **Response**: A list of all friends.

### Create a Friend

- **URL**: `/api/friends`
- **Method**: `POST`
- **Request Body**: JSON object with `name`, `role`, `description`, and `gender` fields.
- **Response**: The created friend object.

### Update a Friend

- **URL**: `/api/friends/<id>`
- **Method**: `PATCH`
- **Request Body**: JSON object with `name`, `role`, `description`, and `gender` fields (optional).
- **Response**: The updated friend object.

### Delete a Friend

- **URL**: `/api/friends/<id>`
- **Method**: `DELETE`
- **Response**: A success message.
