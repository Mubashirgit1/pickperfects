# Pick Perfect

Pick Perfect is a full-featured eCommerce platform designed to help users find the ideal gift for any occasion and recipient. Built with Django and PostgreSQL, the platform integrates secure payments via Stripe, scalable storage with Amazon S3, and is deployed on Heroku for reliability. It offers complete eCommerce functionality, enhanced by an AI-powered recommendation agent that assists users in selecting thoughtful gifts based on their needs—creating a smart and personalized gift-shopping experience.


![Pick Perfect shown on a range of devices](/docs/mockup/mockup-all-framed.png)

[View Pick Perfect on Heroku](https://pick-perfect-0b51f0f8267b.herokuapp.com/)

![GitHub last commit](https://img.shields.io/github/last-commit/Mubashirgit1/pickperfects?color=red)
![GitHub contributors](https://img.shields.io/github/contributors/Mubashirgit1/pickperfects?color=orange)
![GitHub language count](https://img.shields.io/github/languages/count/Mubashirgit1/pickperfects?color=yellow)
![GitHub top language](https://img.shields.io/github/languages/top/Mubashirgit1/pickperfects?color=green)
![W3C Validation](https://img.shields.io/w3c-validation/html?color=blueviolet&targetUrl=https%3A%2F%2Fpick-perfect-0b51f0f8267b.herokuapp.com%2F)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.0-success)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)
![Heroku](https://img.shields.io/badge/Deployed-Heroku-purple)



![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.0-success)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightblue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)

---

## CONTENTS

- [User Experience](#user-experience-ux)

  - [User Stories](#user-stories)

- [Design](#design)

  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Wireframes](#wireframes)

- [Features](#features)

  - [General Features on Each Page](#general-features-on-each-page)
  - [Future Implementations](#future-implementations)
  - [Accessibility](#accessibility)

- [Technologies Used](#technologies-used)

  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

- [Deployment & Local Development](#deployment--local-development)

  - [Deployment](#deployment)
  - [Local Development](#local-development)
    - [How to Fork](#how-to-fork)
    - [How to Clone](#how-to-clone)

- [Testing](#testing)
    [Testing File] (#testing)
  - [Manual Testing](#manual-testing)
  - [Automate Testing](#automate-testing)
  
- [Credits](#credits)
  - [Code Used](#code-used)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)

---

## 🎯 Overview

**Pick Perfect** simplifies the gift-giving experience by providing:
- A diverse catalog of 20+ product categories
- Dynamic product discovery with intelligent filtering
- Seamless shopping cart and checkout
- Responsive design for mobile and desktop
- Secure order management

The platform bridges the gap between gift-givers and recipients with an intuitive, user-friendly interface.

---

## ✨ Features

### 🛍️ Shopping Features
- ✅ Browse 20+ product categories (mugs, puzzles, speakers, tea gift boxes, etc.)
- ✅ Dynamic product filtering (New, Featured, Sale, Top-Rated)
- ✅ Advanced search functionality
- ✅ Product detail pages with ratings and reviews
- ✅ Shopping cart with persistent storage
- ✅ Real-time cart updates
- ✅ Checkout with order confirmation

### 👤 User Management
- ✅ User authentication (register, login, logout)
- ✅ User profiles with order history
- ✅ Address management
- ✅ Saved preferences

### 🎨 UI/UX Components
- ✅ Interactive product carousels (Owl Carousel)
- ✅ Tabbed product navigation
- ✅ Responsive Bootstrap grid layouts
- ✅ Star rating system
- ✅ Sale discount badges
- ✅ Mobile-optimized design

### 📊 Admin Features
- ✅ Product management (CRUD)
- ✅ Category organization
- ✅ Order tracking
- ✅ User management
- ✅ Sales analytics

---

## 🛠️ Tech Stack

### Backend
| Technology | Version | Purpose |
|-----------|---------|---------|
| Python | 3.11+ | Programming language |
| Django | 5.0 | Web framework |
| SQLite | Latest | Default database |
| PostgreSQL | 12+ | Production database |
| django-allauth | - | Authentication system |

### Frontend
| Technology | Version | Purpose |
|-----------|---------|---------|
| HTML5 | - | Markup |
| CSS3 | - | Styling |
| Bootstrap | 5 | Responsive framework |
| jQuery | 3.6+ | JavaScript library |
| Owl Carousel | 2 | Product carousels |
| Font Awesome | 6 | Icons |

### Additional Tools
| Tool | Purpose |
|------|---------|
| Pillow | Image processing |
| Gunicorn | WSGI server (production) |
| python-dotenv | Environment variables |

---

## 📦 Installation

### Prerequisites
```bash
- Python 3.11 or higher
- pip package manager
- Git version control
- Virtual environment support
```

### Step-by-Step Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/pickperfect.git
cd pickperfect
```

#### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\Activate.ps1

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure Environment Variables
Create `.env` file in project root:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

#### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 6. Load Sample Data (Optional)
```bash
python manage.py loaddata products/fixtures/categories.json
python manage.py loaddata products/fixtures/products.json
python manage.py loaddata products/fixtures/handmade-product.json
```

#### 7. Create Superuser
```bash
python manage.py createsuperuser
```

#### 8. Start Development Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

---

## 🚀 Usage

### For Users
1. **Browse Products**: Navigate to the homepage to explore featured products
2. **Search/Filter**: Use tabs (All, New, Featured, Top Selling) to filter products
3. **View Details**: Click on products for detailed information
4. **Add to Cart**: Select quantity and add items to shopping bag
5. **Checkout**: Complete purchase with delivery information
6. **Track Orders**: View order history in user profile

### For Admins
1. **Login**: Access `/admin/` with superuser credentials
2. **Manage Products**: Add, edit, or delete products
3. **Manage Orders**: View and process customer orders
4. **Manage Users**: Handle user accounts and permissions
5. **View Analytics**: Monitor sales and user activity

---

## 📁 Project Structure

```
pickperfect/
├── home/                      # Homepage app
│   ├── templates/home/
│   │   ├── index.html        # Main homepage
│   │   ├── contact.html      # Contact page
│   ├── views.py              # Homepage & contact views
│   ├── forms.py              # Contact form
│   ├── models.py             # Contact message model
│   └── urls.py
│
├── products/                  # Product catalog app
│   ├── templates/products/
│   │   ├── products.html     # Product listing
│   │   ├── product_detail.html
│   ├── models.py             # Product, Category models
│   ├── views.py              # Product views
│   ├── widgets.py            # Custom widgets
│   ├── fixtures/             # Sample data
│   │   ├── categories.json
│   │   ├── products.json
│   │   └── handmade-product.json
│   └── urls.py
│
├── bag/                       # Shopping cart app
│   ├── templates/bag/
│   │   └── bag.html          # Cart page
│   ├── contexts.py           # Cart context processor
│   ├── views.py              # Cart operations
│   ├── templatetags/
│   │   └── bag_tools.py      # Cart template tags
│   └── urls.py
│
├── checkout/                  # Order processing app
│   ├── templates/checkout/
│   │   ├── checkout.html
│   │   ├── checkout_success.html
│   ├── models.py             # Order, OrderItem models
│   ├── views.py              # Checkout flow
│   ├── signals.py            # Order signals
│   ├── forms.py              # Checkout form
│   └── urls.py
│
├── profiles/                  # User profiles app
│   ├── templates/profiles/
│   ├── models.py             # UserProfile model
│   ├── views.py              # Profile management
│   └── urls.py
│
├── static/                    # Static files
│   ├── css/
│   │   ├── bootstrap.min.css
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   ├── lib/                   # Third-party libraries
│   │   ├── animate/
│   │   ├── owlcarousel/
│   │   ├── lightbox/
│   │   └── wow/
│   └── img/
│
├── media/                     # Product images
│   ├── bagpack/
│   ├── candles/
│   ├── chocolate/
│   └── [20+ categories]/
│
├── templates/                 # Base templates
│   ├── base.html             # Main template
│   ├── allauth/               # Authentication templates
│   └── includes/
│       ├── navbar.html
│       ├── footer.html
│       ├── breadcrumbs.html
│       ├── searchbar.html
│       ├── service.html
│       ├── topbar.html
│       └── toasts/
│
├── pickperfect/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   ├── context_processors.py
│   └── env.py
│
├── manage.py
├── requirements.txt
├── Procfile                  # Heroku deployment
├── db.sqlite3               # SQLite database
└── README.md
```

---

## 🔑 Key Components

### Models

#### Product Model
```python
Product:
  - name (CharField)
  - description (TextField)
  - price (DecimalField)
  - image (ImageField)
  - category (ForeignKey → Category)
  - rating (FloatField)
  - sku (CharField)
  - tags (JSONField) → ["new", "featured", "sale"]
  - created_at (DateTimeField)
  - has_sizes (BooleanField)
  - created_by (ForeignKey → User)
  
Methods:
  - get_sale_percentage()
  - get_discounted_price()
```

#### Order Model
```python
Order:
  - order_number (CharField)
  - user_profile (ForeignKey → UserProfile)
  - full_name (CharField)
  - email (EmailField)
  - phone_number (CharField)
  - address fields (CharField)
  - country (CountryField)
  - postcode (CharField)
  - date (DateTimeField)
  - delivery_cost (DecimalField)
  - order_total (DecimalField)
  - grand_total (DecimalField)
  
Methods:
  - calculate_totals()
  - save_order_number()
```

### Views

**Homepage** (`home/views.py`)
- Returns 11 random products
- 4 new products (filtered by "new" tag)
- 4 featured products (filtered by "featured" tag)
- 4 top-rated products (sorted by rating)
- 5 sale products (filtered by "sale" tag)

**Product Listing** (`products/views.py`)
- Display all products with pagination
- Filter by category
- Search functionality
- Sort by price/rating/date

**Shopping Bag** (`bag/views.py`)
- Add items to cart
- Update quantities
- Remove items
- Display cart total

---

## 📡 API Endpoints

### Products
```
GET  /products/                    # List all products
GET  /products/<id>/               # Product detail
POST /products/add/<id>/           # Add to cart
```

### Cart
```
GET  /bag/                         # View cart
POST /bag/add/<id>/                # Add item
POST /bag/adjust/<id>/             # Update quantity
POST /bag/remove/<id>/             # Remove item
```

### Orders
```
GET  /checkout/                    # Checkout page
POST /checkout/                    # Process order
GET  /checkout_success/<order_id>/ # Order confirmation
```

### User
```
GET  /profile/                     # User profile
POST /profile/update/              # Update profile
```

---

## 🔮 Future Enhancements

### High Priority
- [ ] Email notifications for orders
- [ ] Payment gateway integration (Stripe)
- [ ] Advanced product filtering
- [ ] Wishlist functionality
- [ ] Product reviews & ratings from users

### Medium Priority
- [ ] Inventory management system
- [ ] Gift wrapping options
- [ ] Subscription box feature
- [ ] Admin dashboard analytics
- [ ] SMS notifications

### Low Priority
- [ ] AI recommendation engine
- [ ] Social media integration
- [ ] Live chat support
- [ ] Augmented reality preview
- [ ] Multi-language support

---

## 🐛 Troubleshooting

### Issue: Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### Issue: Database Migration Errors
```bash
python manage.py migrate --fake-initial
python manage.py migrate
```

### Issue: Port Already in Use
```bash
python manage.py runserver 8001
```

### Issue: Module Import Errors
```bash
pip install --upgrade -r requirements.txt
pip cache purge
```

---

## 📝 Credits

### Technologies & Libraries
- [Django](https://www.djangoproject.com/) - Web framework
- [Bootstrap 5](https://getbootstrap.com/) - CSS framework
- [Owl Carousel 2](https://owlcarousel2.github.io/OwlCarousel2/) - Carousel plugin
- [Font Awesome](https://fontawesome.com/) - Icon library
- [django-allauth](https://django-allauth.readthedocs.io/) - Authentication

### Resources
- Django Official Documentation
- Bootstrap Documentation
- Stack Overflow Community
- GitHub Community

### Contributors
- **Developer**: Your Name
- **Designer**: Your Design Team
- **Contributors**: Community Contributors

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 📧 Contact & Support

For questions, issues, or suggestions:
- **Email**: support@pickperfect.com
- **GitHub Issues**: [Report a bug](https://github.com/yourusername/pickperfect/issues)
- **Contact Form**: Available on the website

---

**Made with ❤️ for thoughtful gift-givers everywhere**

Last Updated: April 28, 2026
