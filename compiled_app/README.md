
## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose installed
- Ports 5000 and 5433 available on your system

### Running the Application

```bash
# Clone or download this repository
cd compiled_app

# Build and start the application
docker-compose up --build

# The API will be available at http://localhost:5000
# PostgreSQL will be available on port 5433
```

### Verifying the Setup

```bash
# Test the API is running
curl http://localhost:5000/

# Check container status
docker-compose ps
```

## 📊 Dataset Overview

The application generates a large dataset for analysis:

- **Products**: 12,010 records
- **Suppliers**: 5,005 records  
- **Consumers**: 8,005 records
- **Seeded randomness** for reproducible results

### Data Characteristics
- Seeded random generation for reproducible results
- Realistic business data structure
- JSON API responses
- Database integration ready

## 🔌 API Endpoints

### Core Endpoints
- `GET /` - API information and dataset stats
- `GET /products` - Get all products (12,010 records)
- `GET /suppliers` - Get all suppliers (5,005 records)
- `GET /consumers` - Get all consumers (8,005 records)

### Relationship Endpoints
- `GET /products/<id>` - Get specific product with supplier info
- `GET /suppliers/<id>/products` - Get products by supplier
- `GET /consumers/<id>/recommendations` - Get product recommendations based on preferences

### Example Usage
```bash
# Get API info
curl http://localhost:5000/

# Get first 5 products
curl http://localhost:5000/products | jq '.products[0:5]'

# Get supplier details
curl http://localhost:5000/suppliers/1

# Get recommendations for consumer
curl http://localhost:5000/consumers/1/recommendations
```

## 🗄️ PostgreSQL Database

### Connection Details
- **Host**: `localhost` (or `db` from within Docker)
- **Port**: `5432` (mapped to `5433` on host)
- **Database**: `productdb`
- **Username**: `postgres`
- **Password**: `password`

### Database Schema
The database includes pre-created tables:
- `products` - Product catalog with pricing and ratings
- `suppliers` - Supplier information and ratings
- `consumers` - Consumer profiles and preferences

### Connecting to Database
```bash
# From host machine
psql -h localhost -p 5433 -U postgres -d productdb

# From within Docker container
docker exec -it compiled_app-flask-app-1 psql -h db -U postgres -d productdb
```

## 🔍 What to Expect

### For Data Analysis
- Large dataset suitable for performance testing
- Realistic business data structure
- Seeded randomness for reproducible results
- Database integration for complex queries

### For API Development
- RESTful API endpoints
- JSON responses
- Relationship queries between entities

## 🛠️ Development Notes

### Container Architecture
- **Flask App**: Python 3.10 with compiled bytecode
- **PostgreSQL**: Database with pre-initialized schema
- **Network**: Internal Docker network for service communication

## 🚨 Troubleshooting

### Common Issues
1. **Port conflicts**: Ensure ports 5000 and 5433 are available
2. **Docker not running**: Start Docker Desktop
3. **Build failures**: Run `docker-compose down` and rebuild

### Useful Commands
```bash
# View logs
docker-compose logs flask-app
docker-compose logs db

# Restart services
docker-compose restart

# Clean rebuild
docker-compose down
docker-compose up --build

# Access container shell
docker exec -it compiled_app-flask-app-1 bash
```