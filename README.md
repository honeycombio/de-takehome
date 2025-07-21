# DE Takehome - Dockerized Flask API

A dockerized Flask application with 3 interrelated endpoints that return data about products, suppliers, and consumers in JSON format. The application includes a PostgreSQL database and a Python script to collect and store data.

## Features

- **Flask API** with 3 main endpoints for products, suppliers, and consumers
- **Large dataset** with over 25,000 data points
- **Seeded data generation** for reproducible results
- **PostgreSQL database** for data persistence
- **Docker containerization** for easy deployment
- **Data collector script** that hits the API endpoints and stores data in PostgreSQL

## API Endpoints

### Base URL: `http://localhost:5000`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information and available endpoints |
| `/products` | GET | Get all products (12,010 records) |
| `/suppliers` | GET | Get all suppliers (5,005 records) |
| `/consumers` | GET | Get all consumers (8,005 records) |
| `/products/<id>` | GET | Get specific product with supplier info |
| `/suppliers/<id>/products` | GET | Get products by supplier |
| `/consumers/<id>/recommendations` | GET | Get product recommendations for consumer |

## API Examples

### 1. Get API Information
```bash
curl http://localhost:5000/
```

**Response:**
```json
{
  "message": "Product Management API",
  "version": "1.0.0",
  "endpoints": {
    "/products": "Get all products",
    "/suppliers": "Get all suppliers",
    "/consumers": "Get all consumers",
    "/products/<id>": "Get specific product with supplier info",
    "/suppliers/<id>/products": "Get products by supplier",
    "/consumers/<id>/recommendations": "Get product recommendations for consumer"
  },
  "seed": 42,
  "dataset_info": {
    "total_products": 12010,
    "total_suppliers": 5005,
    "total_consumers": 8005,
    "note": "Large dataset with seeded data generation"
  }
}
```

### 2. Get All Products
```bash
curl http://localhost:5000/products
```

**Response:**
```json
{
  "products": [
    {
      "id": 1,
      "name": "Smartphone X1",
      "category": "electronics",
      "price": 799.99,
      "supplier_id": 1,
      "in_stock": true,
      "rating": 4.6
    },
    {
      "id": 2,
      "name": "Gaming Laptop Pro",
      "category": "electronics",
      "price": 1299.99,
      "supplier_id": 2,
      "in_stock": true,
      "rating": 4.8
    },
    {
      "id": 1234,
      "name": "Smart Electronics Pro",
      "category": "electronics",
      "price": 9999.99,
      "supplier_id": 456,
      "in_stock": false,
      "rating": 5.5
    }
  ],
  "count": 12010,
  "seed": 42
}
```

### 3. Get All Suppliers
```bash
curl http://localhost:5000/suppliers
```

**Response:**
```json
{
  "suppliers": [
    {
      "id": 1,
      "name": "TechCorp Industries",
      "location": "San Francisco, CA",
      "rating": 4.8,
      "established": 2010
    },
    {
      "id": 2,
      "name": "Global Electronics Ltd",
      "location": "New York, NY",
      "rating": 4.5,
      "established": 2008
    },
    {
      "id": 1234,
      "name": "TechCorp 1234",
      "location": "Dallas, TX",
      "rating": 6.0,
      "established": 2015
    }
  ],
  "count": 5005,
  "seed": 42
}
```

### 4. Get All Consumers
```bash
curl http://localhost:5000/consumers
```

**Response:**
```json
{
  "consumers": [
    {
      "id": 1,
      "name": "John Smith",
      "email": "john.smith@email.com",
      "location": "Los Angeles, CA",
      "preferences": ["electronics", "gaming"]
    },
    {
      "id": 2,
      "name": "Sarah Johnson",
      "email": "sarah.j@email.com",
      "location": "Chicago, IL",
      "preferences": ["home", "kitchen"]
    },
    {
      "id": 1234,
      "name": "John John",
      "email": "consumer1234@invalid",
      "location": "Miami, FL",
      "preferences": []
    }
  ],
  "count": 8005,
  "seed": 42
}
```

### 5. Get Specific Product with Supplier
```bash
curl http://localhost:5000/products/1
```

**Response:**
```json
{
  "product": {
    "id": 1,
    "name": "Smartphone X1",
    "category": "electronics",
    "price": 799.99,
    "supplier_id": 1,
    "in_stock": true,
    "rating": 4.6
  },
  "supplier": {
    "id": 1,
    "name": "TechCorp Industries",
    "location": "San Francisco, CA",
    "rating": 4.8,
    "established": 2010
  },
  "seed": 42
}
```

### 6. Get Products by Supplier
```bash
curl http://localhost:5000/suppliers/1/products
```

**Response:**
```json
{
  "supplier": {
    "id": 1,
    "name": "TechCorp Industries",
    "location": "San Francisco, CA",
    "rating": 4.8,
    "established": 2010
  },
  "products": [
    {
      "id": 1,
      "name": "Smartphone X1",
      "category": "electronics",
      "price": 799.99,
      "supplier_id": 1,
      "in_stock": true,
      "rating": 4.6
    },
    {
      "id": 6,
      "name": "Coffee Maker Deluxe",
      "category": "kitchen",
      "price": 89.99,
      "supplier_id": 1,
      "in_stock": true,
      "rating": 4.3
    }
  ],
  "product_count": 2,
  "seed": 42
}
```

### 7. Get Consumer Recommendations
```bash
curl http://localhost:5000/consumers/1/recommendations
```

**Response:**
```json
{
  "consumer": {
    "id": 1,
    "name": "John Smith",
    "email": "john.smith@email.com",
    "location": "Los Angeles, CA",
    "preferences": ["electronics", "gaming"]
  },
  "recommendations": [
    {
      "id": 1,
      "name": "Smartphone X1",
      "category": "electronics",
      "price": 799.99,
      "supplier_id": 1,
      "in_stock": true,
      "rating": 4.6
    },
    {
      "id": 2,
      "name": "Gaming Laptop Pro",
      "category": "electronics",
      "price": 1299.99,
      "supplier_id": 2,
      "in_stock": true,
      "rating": 4.8
    },
    {
      "id": 9,
      "name": "Smart Watch",
      "category": "electronics",
      "price": 399.99,
      "supplier_id": 4,
      "in_stock": false,
      "rating": 4.9
    }
  ],
  "recommendation_count": 3,
  "seed": 42
}
```

## Quick Start

### 1. Build and Run with Docker Compose

```bash
# Build and start the services
docker-compose up --build

# The Flask app will be available at http://localhost:5000
# PostgreSQL will be available at localhost:5432
```

### 2. Test the API

```bash
# Get API information
curl http://localhost:5000/

# Get all products
curl http://localhost:5000/products

# Get all suppliers
curl http://localhost:5000/suppliers

# Get all consumers
curl http://localhost:5000/consumers

# Get specific product with supplier info
curl http://localhost:5000/products/1

# Get products by supplier
curl http://localhost:5000/suppliers/1/products

# Get recommendations for consumer
curl http://localhost:5000/consumers/1/recommendations
```

### 3. Run the Data Collector

```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the data collector script
python data_collector.py
```

## PostgreSQL Credentials

When using Docker Compose, the PostgreSQL database is automatically configured with the following credentials:

- **Host**: `localhost` (or `db` when connecting from within Docker network)
- **Port**: `5432`
- **Database**: `productdb`
- **Username**: `postgres`
- **Password**: `password`

### Connection Examples

**From host machine:**
```bash
psql -h localhost -p 5432 -U postgres -d productdb
# Password: password
```

**From within Docker container:**
```bash
psql -h db -p 5432 -U postgres -d productdb
# Password: password
```

**Connection string:**
```
postgresql://postgres:password@localhost:5432/productdb
```

It's important to remember that this postgres instance is deleted when docker is stopped. Please materialize any DDL and queries in code so that it can be reproduced. The emphasis is more on extracting value from the data in postgres and less on building a fancy data pipeline to get from the api endpoint to postgres.

## Data Structure

### Products
- `id`: Unique identifier
- `name`: Product name
- `category`: Product category (electronics, home, kitchen, fitness, etc.)
- `price`: Product price
- `supplier_id`: Reference to supplier
- `in_stock`: Boolean indicating availability
- `rating`: Product rating (1-5)

### Suppliers
- `id`: Unique identifier
- `name`: Supplier name
- `location`: Supplier location
- `rating`: Supplier rating (1-5)
- `established`: Year established

### Consumers
- `id`: Unique identifier
- `name`: Consumer name
- `email`: Email address
- `location`: Consumer location
- `preferences`: Array of preference categories

## Database Schema

The application creates three main tables:

```sql
-- Suppliers table
CREATE TABLE suppliers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    rating DECIMAL(3,2),
    established INTEGER
);

-- Consumers table
CREATE TABLE consumers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    location VARCHAR(255),
    preferences JSONB
);

-- Products table
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10,2),
    supplier_id INTEGER REFERENCES suppliers(id),
    in_stock BOOLEAN,
    rating DECIMAL(3,2)
);
```



## Data Generation

The application uses a seed (42) for reproducible data generation. The data includes:

- **12,010 products** with various categories and prices
- **5,005 suppliers** with ratings and establishment years
- **8,005 consumers** with preferences and locations

The data is interrelated:
- Products reference suppliers via `supplier_id`
- Consumer recommendations are based on preference matching
- All data is consistently generated using the same seed

## Troubleshooting

1. **Port already in use**: Change the port mapping in `docker-compose.yml`
2. **Database connection issues**: Ensure PostgreSQL container is running
3. **Data collector errors**: Check that the Flask app is running and accessible

## Testing Scripts

### Quick Test
```bash
python quick_test.py
```

### Full API Explorer
```bash
python api_explorer.py
```

### Database Verification
```bash
python verify_db.py
```
