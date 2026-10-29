# E-Commerce Platform with AI-Based Product Recommendations

A full-stack Django e-commerce web application that personalises the shopping experience with machine learning. It recommends products to each customer based on their purchase and browsing history, predicts product prices, and provides an admin dashboard with sentiment analysis of customer reviews.

## Features

**Storefront**
- Product catalogue with paginated listings and detailed product pages
- Shopping cart and checkout flow
- Product reviews and ratings (1–5)
- Personalised product recommendations generated from each user's orders and browsing history

**Machine Learning**
- **Recommendation engine:** K-Nearest Neighbours model over encoded product attributes (gender, category, sub-category, article type, season, price), returning similar items for each product a user has interacted with
- **Price prediction:** Regression model that estimates a product's price from its attributes and title embeddings (Word2Vec)
- **Sentiment analysis:** Hugging Face Transformers pipeline that scores customer reviews and reports positive/negative percentages on the admin dashboard

**Accounts and Administration**
- Custom user model with email-based authentication
- JWT-based API authentication (`djangorestframework-simplejwt`)
- Admin dashboard for managing products, orders, and users

**Platform**
- RESTful API built with Django REST Framework
- Cross-origin resource sharing (CORS) configuration for a separate frontend
- Static files served with WhiteNoise; product media stored on AWS S3
- Environment-driven configuration (12-factor style)
- Docker and Heroku/Railway-compatible deployment (`Procfile`, `Dockerfile`)

## Tech Stack

| Layer | Technologies |
|---|---|
| Backend | Python 3.9, Django 4.2, Django REST Framework |
| Machine learning | scikit-learn, gensim (Word2Vec), Hugging Face Transformers, joblib |
| Database | PostgreSQL (via `DATABASE_URL`) |
| Storage | AWS S3 (`django-storages`, `boto3`) |
| Auth | Django auth with custom user model, SimpleJWT |
| Frontend | Django templates, Bootstrap, custom CSS/JavaScript |
| Deployment | Gunicorn, WhiteNoise, Docker, Procfile |

## Project Structure

```
.
├── Eshop/              # Project settings, root URL configuration, WSGI/ASGI entry points
├── authentication/     # Custom user model, registration, login, and profile
├── products/           # Product catalogue, cart, orders, reviews, and recommendation views
├── adminpanel/         # Admin dashboard, product/order/user management, sentiment analysis
├── model/              # Serialised ML artefacts (KNN model, encoders, Word2Vec, price model)
├── manage.py
├── requirements.txt
├── Dockerfile
└── Procfile
```

## Getting Started

### Prerequisites

- Python 3.9 (see `runtime.txt`)
- PostgreSQL database
- (Optional) AWS S3 bucket for media storage
- (Optional) Docker

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/Ecommerce-App-With-AI-Based-Recommendation.git
   cd Ecommerce-App-With-AI-Based-Recommendation
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3.9 -m venv venv
   source venv/bin/activate          # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file or export the following variables:

   | Variable | Description |
   |---|---|
   | `DJANGO_SECRET_KEY` | Django secret key |
   | `DJANGO_DEBUG` | Set to `True` for local development; leave unset in production |
   | `DJANGO_ENV` | Set to `production` to enable production-only settings |
   | `DATABASE_URL` | PostgreSQL connection string, e.g. `postgres://user:password@localhost:5432/eshop` |
   | `AWS_ACCESS_KEY_ID` | AWS access key (for S3 media storage) |
   | `AWS_SECRET_ACCESS_KEY` | AWS secret key (for S3 media storage) |
   | `AWS_STORAGE_BUCKET_NAME` | S3 bucket name (for S3 media storage) |

5. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create an admin user**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   The application is available at `http://localhost:8000`.

### Running with Docker

```bash
docker build -t eshop-recommender .
docker run -p 8000:8000 --env-file .env eshop-recommender
```

## API Overview

| Endpoint | Method | Description |
|---|---|---|
| `/products/` | GET, POST | List or create products |
| `/products/<id>/` | GET, PUT, PATCH, DELETE | Retrieve, update, or delete a product |
| `/products/retrieve/<pk>` | GET | Render the product detail page |
| `/products/recommended/products/<user_id>` | GET | Personalised recommendations for a user |
| `/products/predict/` | GET, POST | Predict a product's price |
| `/products/listing/` | POST | Create an order |
| `/products/history` | POST | Record a user's product view |
| `/products/review` | POST | Submit a product review |
| `/products/carts/` | GET, POST | Manage shopping cart items |
| `/auth/` | — | Registration, login, and profile routes |
| `/admin/` | — | Custom admin dashboard |

## Machine Learning Models

The trained artefacts live in the `model/` directory and are loaded at application start-up:

| File | Purpose |
|---|---|
| `knn_model_features_base.pkl` | K-Nearest Neighbours model used for recommendations |
| `encoders_features_base.pkl`, `label_encoders.pkl` | Label encoders for categorical product features |
| `Y_train.pkl` | Product ID lookup aligned with the KNN training data |
| `product_price_predictions_model.pkl` | Price prediction model |
| `word2vec_model.bin` | Word2Vec embeddings for product titles |

## Contributing

Contributions are welcome. Please open an issue to discuss significant changes before submitting a pull request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request
