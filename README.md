# Ecommerce Medicine Store - Flask Application

## Introduction

Welcome to our Ecommerce Medicine Store application! This web application is built using the Flask framework and is designed to facilitate the online sale of medicines. It provides a user-friendly interface for customers to browse, search, and purchase medicines conveniently from the comfort of their homes.

## Features

- **User Authentication:** Users can create accounts, log in, and manage their profiles.
- **Product Catalog:** Browse a wide range of medicines with detailed information.
- **Search Functionality:** Easily find specific medicines using the search bar.
- **Shopping Cart:** Add medicines to the cart for a seamless shopping experience.
- **Order Management:** Track and manage your orders through the user dashboard.
- **Admin Panel:** Admins can add, edit, and remove products from the catalog.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/medicine-store.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd medicine-store
   ```

3. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```
   - For Unix or MacOS:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Configure the Database:**
   - Update the database URI in `config.py` or set it as an environment variable.

7. **Run the Application:**
   ```bash
   python app.py
   ```

8. **Access the Application:**
   Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

## Configuration

- Update configuration settings in `config.py` as needed, such as database URI, secret key, and other application settings.

## Admin Access

To access the admin panel, you need to create an admin account. Use the Flask shell to set the admin role for your account:

```bash
flask shell
```

Inside the shell, run the following commands:

```python
from app import db, create_app
from app.models import User, Role

app = create_app()
app.app_context().push()

# Replace 'your_username' with your actual username
user = User.query.filter_by(username='your_username').first()
user.role = Role.query.filter_by(name='admin').first()
db.session.commit()
```

## Contributing

If you'd like to contribute to the development of this application, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/your-username/medicine-store/issues) on our GitHub repository.

Thank you for using our Ecommerce Medicine Store application! Happy shopping!
