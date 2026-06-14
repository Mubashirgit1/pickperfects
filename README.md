# Pick Perfect

Pick Perfect is a full-featured eCommerce platform designed to help users find the ideal gift for any occasion and recipient. Built with Django and PostgreSQL, the platform integrates secure payments via Stripe, scalable storage with Amazon S3, and is deployed on Heroku for reliability. It offers complete eCommerce functionality, enhanced by an AI-powered recommendation agent that assists users in selecting thoughtful gifts based on their needs—creating a smart and personalized gift-shopping experience.


![Pick Perfect shown on a range of devices](/docs/mockup/mockup-all-framed.png)

[View Pick Perfect on Heroku](https://pickperfect-2e4acff925d2.herokuapp.com/)

![GitHub last commit](https://img.shields.io/github/last-commit/Mubashirgit1/pickperfects?color=red)
![GitHub contributors](https://img.shields.io/github/contributors/Mubashirgit1/pickperfects?color=orange)
![GitHub language count](https://img.shields.io/github/languages/count/Mubashirgit1/pickperfects?color=yellow)
![GitHub top language](https://img.shields.io/github/languages/top/Mubashirgit1/pickperfects?color=green)
![W3C Validation](https://img.shields.io/w3c-validation/html?color=blueviolet&targetUrl=https%3A%2F%2Fpick-perfect-0b51f0f8267b.herokuapp.com%2F)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)
![Heroku](https://img.shields.io/badge/Deployed-Heroku-purple)



![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.0-success)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightblue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)

---

## CONTENTS

- [User Experience](#user-experience-ux)
  - [Initial Discussion](#initial-discussion)
  - [User Goals](#-user-goals)
  - [User Stories](#-user-stories)
    - [Product Search & Browsing](#-product-search--browsing)
    - [Product Management](#-product-management)
    - [Cart & Checkout](#-cart--checkout)
    - [User Account](#-user-account)
    - [About & Contact](#️-about--contact)

- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Wireframes](#wireframes)
  - [Favicon](#favicon)
  - [Navigation](#navigation)
  - [Footer](#Footer)
  - [Entity Relationship Diagram](#Entity-Relationship-Diagram)
  - [Flowchart](#flowchart)

- [Main Features](#-main-features)
  - [Homepage](#-homepage)
  - [Advanced Product Search](#-advanced-product-search)
  - [Shopping Features](#-shopping-features)
  - [Filtering & Sorting](#️-filtering--sorting)
  - [Product Features](#-product-features)
  - [UI/UX Components](#-uiux-components)
  - [Shopping Bag / Cart](#-shopping-bag--cart)
  - [Checkout System](#-checkout-system)
  - [Orders](#-orders)
  - [User Authentication](#-user-authentication)
  - [Contact Us](#-contact-us)
  - [Admin Features](#-admin-features)
  - [Responsive Design](#-responsive-design)
  - [Performance & UX Features](#-performance--ux-features)
  - [Security Features](#-security-features)
  - [Future Improvements](#-future-improvements)
  - [Conclusion](#-conclusion)

- [Tech Stack](#️-tech-stack)
  - [Backend](#backend)
  - [Frontend](#frontend)
  - [Additional Tools](#additional-tools)

- [Installation](#-installation)
  - [Prerequisites](#prerequisites)
  - [Step-by-Step Setup](#step-by-step-setup)

- [Usage](#-usage)
  - [For Users](#for-users)
  - [For Admins](#for-admins)

- [Project Structure](#-project-structure)

- [Key Components](#-key-components)
  - [Models](#models)
  - [Views](#views)

- [API Endpoints](#-api-endpoints)

- [Future Enhancements](#-future-enhancements)

- [Testing](#testing)
    [Testing File] (#testing)
  - [Manual Testing](#manual-testing)
  - [Automate Testing](#automate-testing)

- [Troubleshooting](#-troubleshooting)

- [Credits](#-credits)
  - [Technologies & Libraries](#technologies--libraries)
  - [Resources](#resources)
  - [Contributors](#contributors)
  - [Code Used](#code-used)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)
  
- [License](#-license)

- [Contact & Support](#-contact--support)
                    

---

## User Experience (UX)

### Initial Discussion

As an online shopper,  
I want to search, compare, and save products easily,  
so that I can quickly find the best items for my needs and revisit them later without repeating searches.

---

### 👤 User Goals

- Quickly search and compare products by category, keyword, SKU, price, recipient, or occasion
- Save favorite products for future purchases
- Access previous orders and account details easily
- Enjoy a fast, interactive, and visually appealing shopping experience
- Filter and sort products efficiently
- Manage cart, quantities, colors, and sizes smoothly
- Complete secure and user-friendly checkout processes

---

### 🧾 User Stories

### 🔍 Product Search & Browsing

#### As a customer,
I want to search products by name, SKU, or keywords,  
so that I can quickly find relevant products.

#### As a shopper,
I want to filter products by category, price, recipient, occasion, color, and size,  
so that I can narrow down products that match my preferences.

#### As a user,
I want to sort products by price, popularity, rating, and newest arrivals,  
so that I can easily compare products.

---

### 🛍️ Product Management

#### As a customer,
I want to view detailed product pages,  
so that I can see product descriptions, images, prices, sizes, colors, and availability.

#### As a shopper,
I want to select product quantity, color, and size,  
so that I can customize my purchase before checkout.

#### As a user,
I want to save products to my wishlist,  
so that I can revisit them later.

---

### 🛒 Cart & Checkout

#### As a customer,
I want to add products to my bag/cart,  
so that I can purchase multiple items together.

#### As a user,
I want to update quantities or remove products from my cart,  
so that I can manage my order easily.

#### As a shopper,
I want a secure checkout process,  
so that I can safely complete my purchase.

#### As a customer,
I want to receive order confirmations and notifications,  
so that I know my order was placed successfully.

---

### 👤 User Account

### As a user,
I want to create an account and log in securely,  
so that I can manage my orders and personal information.

### As a returning customer,
I want to view my previous orders,  
so that I can track purchases and reorder products easily.

### As a customer,
I want to update my shipping and billing details,  
so that my checkout process is faster.

---

### ℹ️ About & Contact

### As a visitor,
I want to learn about PickPerfect’s mission and story,  
so that I can trust the platform.

### As a customer,
I want to contact support through a form,  
so that I can get assistance quickly.

### As a business partner,
I want to access company contact details and social links,  
so that I can connect for collaborations.

---

## Design

### Colour Scheme

Here is the color scheme for the project:
- **Scarlet Fire**: `#F92400`
- **Carrot Orange**: `#E5901F`
- **Apricot Cream**: `#E6C594`
- **White Smoke**: `#F4F3F3`
- **White**: `#FFFFFF`
- **Iron Grey**: `#474747`
 
![Pickperfect](docs/colorscheme/pickperfect.png)
Resource
https://coolors.co/user/palettes/6a02438c17faa8000f3973a8


### Typography


PickPerfect uses a system-optimized and web-safe font stack to ensure a consistent, readable, and fast-loading user interface across all devices and platforms.

### Font Stack

font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif,
             "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";


### Explanation of the stack:

1. -apple-system & BlinkMacSystemFont → Use the native system font on macOS/iOS and Chrome/Chromium browsers.

2. "Segoe UI" → Default system font for Windows.

3. Roboto → Popular font for Android and Google platforms.

4. "Helvetica Neue" & Arial → Standard web-safe fallback fonts for older systems.

5. sans-serif → Generic fallback if none of the above are available.

6. Emoji support: "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji" ensures emojis render properly across platforms.


### Imagery

PickPerfect uses a combination of custom designs and free stock images to create an attractive, user-friendly, and consistent interface.

1. Hero & Homepage Images

Main carousel Images:

The main carousel images and hamper product visuals represent the overall style and identity of the website, showcasing gift collections in an attractive and engaging way to create a warm and premium shopping experience for users.

2. Products Images

All product images used on the website were sourced from free image platforms such as Unsplash, Pixabay, and Pexels to help complete the product catalogue. All images were optimized and resized using Bulk Resize Photos to improve website performance and maintain consistent image dimensions across the platform.

3. Branding Assets

Logo:

The logo features bold typography in a carrot-orange shade, paired with a small shopping bag icon in a Scarlet Fire tone.

Favicon:

Designed in Canva for display in browser tabs and bookmarks.

Purpose: Establish a strong, consistent brand identity throughout the app.

4. Image Sources & Licensing

Canva: For custom graphics, logos, and favicon.

Unsplash: Free, royalty-free images used for gallery and hero visuals.

5. Purpose & UX Benefits

Enhance visual appeal and engagement.

Provide users with a sense of travel inspiration and discovery.

Ensure all assets are optimized for fast web performance.

Maintain a consistent visual identity across all pages.


### Wireframes

🖌️ Wireframes & UI/UX Design

The initial design and layout of this project were conceptualized using Balsamiq.
These wireframes served as the foundation for the UI/UX structure, ensuring a clear visual direction before development began.

📐 Tool used: [canva](https://www.canva.com/)

🎯 Purpose: Define layout, content hierarchy, and user flow across key pages and components.


**Home Page**
![Pick Perfect Website Main Page](docs/wireframes/main-page.png)
**Shop Page**
![Pick Perfect Website Shop ](docs/wireframes/shop-page.png)
**Shopping Cart**
![Pick Perfect Website shopping cart](docs/wireframes/shopping-bag.png)
**Checkout**
![Pick Perfect Website Checkout](docs/wireframes/checkout.png)

### Favicon

- A favicon in the browser tab.

  ![favicon](docs/favicon/favicon.ico)

  - The navigation of the site at the top of every page. link to all pages each other click on logo back to home page.

### Navigation

![home-nav](docs/website/nav.png)

- Navigation of All Other pages same have login register and Search, Categories and contact deatils.


### 🧭 Footer

Showing Address and Phone numbers:  

`Address` · `Mail Us` · `Contact Us` · `Telephone` · `Register` · `pickperfect.com`

Submit for newsLetter Cutomer Service Information and extras for customer satisfaction

![Footer](docs/website/footer.png)

---

### Entity Relationship Diagram (ERD)

The Entity Relationship Diagram (ERD) for this eCommerce website provides a clear visual representation of the database structure and relationships between different entities such as users, products, orders, categories, and payments. It helps illustrate how data is organized and connected within the system, ensuring better understanding of the backend architecture. The ERD is included in this repository to support developers in understanding data flow, maintaining consistency, and simplifying future enhancements or debugging of the database design.

![ERD](docs/erd-diagram/diagram.png)

### Flowchart

The flowchart illustrates the overall workflow of the eCommerce system, showing how users interact with the platform from browsing products to placing orders and completing payments. It maps out each step of the process, including user registration/login, product selection, cart management, checkout, and order confirmation. This visual representation helps in understanding the system logic and user journey, making it easier to analyze, develop, and improve the application flow.

![Flowchart](docs/flowchart/flow-chart.png)

## 🚀 Main Features

### 🏠 Homepage

- Hero carousel/banner slider
- Featured products section
- Top-selling products
- Latest arrivals
- Category highlights
- Promotional offers and discounts
- Newsletter subscription
- Responsive product grid

---

### 🔍 Advanced Product Search

Users can search products using:

- Product name
- Product description
- SKU
- Tags
- Keywords
- Recipient
- Occasion

---

### 🛍️ Shopping Features
- Browse 20+ product categories (mugs, puzzles, speakers, tea gift boxes, etc.)
- Dynamic product filtering (New, Featured, Sale, Top-Rated)
- Advanced search functionality
- Product detail pages with ratings and reviews
- Shopping cart with persistent storage
- Real-time cart updates
- Checkout with order confirmation

---

### ⚙️ Filtering & Sorting

### Filters
- Categories
- Price range
- Colors
- Sizes
- Occasion
- Recipient
- Availability

### Sorting
- Price low to high
- Price high to low
- Best selling
- Highest rated
- Newest products

---

### 🛍️ Product Features

- Product image gallery
- Product variants (size, color)
- Quantity selector
- SKU display
- Stock availability
- Ratings and reviews
- Related products

---

### 🎨 UI/UX Components
-  Interactive product carousels (Owl Carousel)
-  Tabbed product navigation
-  Responsive Bootstrap grid layouts
-  Star rating system
-  Sale discount badges
-  Mobile-optimized design

---

### 🛒 Shopping Bag / Cart

- Add to cart
- Update quantities
- Remove products
- Cart subtotal and total
- Shipping calculations
- Responsive mini-cart

---

### 💳 Checkout System

- Secure payment integration
- Stripe payment support
- Billing and shipping forms
- Order summary
- Validation and error handling
- Success notifications

---

### 📦 Orders

- Order history
- Order confirmation page
- Previous orders dashboard
- Email for new order place
---

### 👤 User Authentication

- User registration
- Login/logout
- Password reset
- Profile management
- Saved addresses
- Email Confirmation for register

---

### 📞 Contact Us

- Contact form
- Customer support details
- Social media links
- Business inquiry support

---

### 📊 Admin Features
- Product management (CRUD)
- Category organization
- Order tracking
- User management
- Sales analytics

---

### 📱 Responsive Design

PickPerfect is fully optimized for:

- Mobile devices
- Tablets
- Desktop screens

The platform uses responsive layouts and modern UI components to ensure a seamless shopping experience across all devices.

---

### ⚡ Performance & UX Features

- Fast-loading pages
- Optimized images
- Real-time notifications
- SweetAlert2 alerts
- Accessible forms and navigation
- Interactive product cards
- Loading indicators
- SEO-friendly structure

---

### 🔐 Security Features

- CSRF protection
- Secure authentication
- Secure payment handling
- Form validation
- Protected user data

---

### 📊 Future Improvements

- Product reviews & ratings
- AI product recommendations
- Multi-vendor support
- Live chat support
- Email notifications
- Discount coupon system
- Inventory analytics dashboard

---

### ✅ Conclusion

PickPerfect aims to provide a modern, user-friendly, and scalable e-commerce solution that delivers excellent shopping experiences through advanced search, filtering, responsive design, and secure checkout functionality.

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

## Testing

Please refer to the [TESTING.md](/docs/testing.md)
file for a detailed breakdown of all testing carried out for this project.

### Automated and Manual Testing

The Pick Perfect eCommerce website has been thoroughly tested to ensure all features work correctly, provide a smooth user experience, and handle both valid and invalid inputs effectively. Testing was carried out across different devices and browsers to ensure responsiveness, performance, and reliability.

### Manual Testing

Manual testing was performed to verify that all core functionalities behave as expected from a user’s perspective. This includes testing user registration and login, product browsing, adding items to the cart, updating quantities, checkout process, and order confirmation. Form validation was also checked to ensure proper error handling for invalid or missing inputs. In addition, navigation links, search functionality, and UI elements were tested to ensure a smooth and consistent user experience across the platform.

### Automated Testing

Automated testing was used to validate key backend logic and ensure system reliability. This includes testing API endpoints, authentication processes, database operations, and cart/order calculations. Automated tests help ensure that core functionalities remain stable during updates and future development.

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
- pixbay https://pixabay.com/
- colors https://coolors.co/
- bulkresizephotos https://bulkresizephotos.com/
- aws amazon https://aws.amazon.com/s3
- unsplash https://unsplash.com/
- https://www.pexels.com/
- https://heroku.com
- https://chatgpt.com/

### Contributors
- **Developer**: Muabshir Hussain
- **Designer**: Mubashir Hussain
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
