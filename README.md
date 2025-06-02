Django Blog Practice  

A simple blog website built with Django as a practice project while learning web development. This application allows users to post blogs, register and log in, and access basic blog functionalities.

Features
- User registration and authentication
- Create, edit, and delete blog posts
- View list of all blog posts
- Basic CSS styling for a clean UI
- 
Tech Stack
- Python 3.13**
- Django 5.1.7
- HTML & CSS

Installation

To run this project locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/yourusername/django-blog-practice.git](https://github.com/ItsMeDarpan/Blog_Website_using_Django.git

# Navigate into the project directory
cd project_blog

# (Optional) Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
