# Block Crusher Game

A Django-based block crusher game built with HTML5 Canvas and JavaScript.

## Features

- Interactive block crushing gameplay
- Web-based interface using Django
- HTML5 Canvas for game rendering
- Responsive design

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Priyanshu1561/Block_Crusher.git
cd Block_Crusher
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Open your browser and navigate to `http://127.0.0.1:8000/`

## Project Structure

```
block_crusher_project/
├── block_crusher/          # Main app
│   ├── templates/          # HTML templates
│   ├── views.py           # View functions
│   ├── urls.py            # URL patterns
│   └── models.py          # Database models
├── static/                # Static files (CSS, JS)
│   ├── css/
│   └── js/
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## How to Play

- Use your mouse to control the paddle
- Break all the blocks to win
- Don't let the ball fall off the screen!

## Technologies Used

- Django (Python web framework)
- HTML5 Canvas
- JavaScript
- CSS3

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).
