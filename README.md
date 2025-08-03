
# **Project Nexus**

**Project Nexus** is a comprehensive backend e-commerce system built with **Python**, **Django**, and **Django REST Framework (DRF)**. It provides RESTful APIs for product management, user authentication, ordering, and payment processing. The project is backend-only, with no frontend implementation, and is documented using **Swagger** and **ReDoc**.

---

## **Features**
- **Product Management**: Create, retrieve, update, and delete products.
- **User Authentication**: Register, login, logout, and profile management using **JWT (JSON Web Tokens)**.
- **Order Management**: Place, retrieve, and cancel orders.
- **Payment Integration**: Initiate payments and check payment status.
- **Reviews and Ratings**: Add, update, and delete product reviews.
- **Wishlist**: Add and remove products from the user's wishlist.
- **Documentation**: APIs are documented using **Swagger** and **ReDoc**.

---

## **Technologies Used**
- **Backend**: Python, Django, Django REST Framework (DRF)
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: SQLite (for development), PostgreSQL (optional for production)
- **Documentation**: Swagger and ReDoc
- **Version Control**: Git
- **Testing**: Django Test Framework
- **Deployment**: Render (https://alx-project-nexus-89gl.onrender.com/)

---

## **Getting Started**

### **Prerequisites**
- Python 3.12 or higher
- Git
- Virtual environment (optional but recommended)

---

### **Cloning the Repository**
1. Open your terminal and run:
   ```bash
   https://github.com/BrianKimurgor/alx-project-nexus
   cd alx-project-nexus
   ```

---

### **Setting Up the Virtual Environment**
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

---

### **Installing Dependencies**
1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

---

### **Running Migrations**
1. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

---

### **Running the Application Locally**
1. Start the development server:
   ```bash
   python manage.py runserver
   ```
2. Open your browser and navigate to:
   - **Swagger Documentation**: http://127.0.0.1:8000/api/docs/
   - **ReDoc Documentation**: http://127.0.0.1:8000/api/redoc/

---

### **Testing the Application**
1. Run the test suite:
   ```bash
   python manage.py test
   ```

---

## **API Documentation**
The APIs are documented using **Swagger** and **ReDoc**. You can access the documentation at:
- **Swagger**: http://127.0.0.1:8000/api/docs/
- **ReDoc**: http://127.0.0.1:8000/api/redoc/

---

## **Deployment**
The project is deployed on **Render** and can be accessed at:
- **Live URL**: https://alx-project-nexus-89gl.onrender.com/

---

## **API Endpoints**
Here’s a quick overview of the available API endpoints:

### **Authentication**
- **Register**: `POST /api/auth/register/`
- **Login**: `POST /api/auth/login/`
- **Logout**: `POST /api/auth/logout/`
- **Profile**: `GET /api/auth/profile/`
- **Reset Password**: `POST /api/auth/reset-password/`

### **Products**
- **List Products**: `GET /api/products/`
- **Create Product**: `POST /api/products/`
- **Retrieve Product**: `GET /api/products/{id}/`
- **Update Product**: `PUT /api/products/{id}/`
- **Delete Product**: `DELETE /api/products/{id}/`

### **Orders**
- **List Orders**: `GET /api/orders/`
- **Create Order**: `POST /api/orders/`
- **Retrieve Order**: `GET /api/orders/{id}/`
- **Cancel Order**: `PUT /api/orders/{id}/cancel/`

### **Payments**
- **Initiate Payment**: `POST /api/payments/`
- **Check Payment Status**: `GET /api/payments/{id}/`

### **Reviews**
- **List Reviews**: `GET /api/reviews/{product_id}/`
- **Create Review**: `POST /api/reviews/`
- **Update Review**: `PUT /api/reviews/{id}/`
- **Delete Review**: `DELETE /api/reviews/{id}/`

### **Wishlist**
- **List Wishlist**: `GET /api/wishlist/`
- **Add to Wishlist**: `POST /api/wishlist/`
- **Remove from Wishlist**: `DELETE /api/wishlist/{id}/`

---

## **Contributing**
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**
- **Django REST Framework**: For building powerful and flexible APIs.
- **Render**: For hosting the application.
- **Swagger and ReDoc**: For API documentation.

---

## **Contact**
For questions or feedback, feel free to reach out:
- **Name**: Brian Kimurgor
- **Email**: kimurgorbrian20@gmail.com

---

Enjoy using **Project Nexus**! 🚀

---