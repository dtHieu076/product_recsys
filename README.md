# Triển Khai Hệ Thống Gợi Ý Sản Phẩm (Product Recommendation System)

## 1. Tổng Quan
- **Mục tiêu**: Xây dựng ứng dụng web full-stack demo e-commerce với:
  - Theo dõi hành vi người dùng (view, cart, purchase) lưu vào PostgreSQL.
  - Gợi ý sản phẩm cá nhân hóa sử dụng mô hình ALS (Alternating Least Squares) từ thư mục `model`.
  - Backend Python (FastAPI) xử lý API, tích hợp DB và model.
  - Frontend React + TailwindCSS: Giao diện sản phẩm, giỏ hàng, trang cá nhân với recs.
- **Tech Stack**:
  | Component | Technologies |
  |-----------|--------------|
  | Backend | FastAPI, SQLAlchemy (async), asyncpg, Surprise (ALS model), Pydantic |
  | Frontend | React 18, TailwindCSS, Axios (API calls), React Router |
  | Database | PostgreSQL (Neon provided) |
  | Model | Surprise ALS (train/update từ events data) |
  | Other | Docker (optional), CORS |
- **Giả định**:
  - Dataset Kaggle sẽ được load/populate thêm vào DB (products, categories).
  - Model `model/` chứa `als_model.pkl` (pre-trained hoặc train on-the-fly từ events).
  - Demo với 2 users mẫu; mở rộng sau.
- **User Flow**:
  1. Login (users mẫu).
  2. Browse sản phẩm → track 'view'.
  3. Add to cart → track 'cart'.
  4. Purchase → track 'purchase'.
  5. Xem recommendations dựa trên hành vi.

## 2. Cấu Trúc Dự Án
```
product_recsys/
├── backend/                 # Python FastAPI
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI app
│   │   ├── database.py      # DB connection
│   │   ├── models/          # Pydantic/SQLAlchemy models
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── routers/
│   │   ├── services/
│   │   └── core/            # Config, security
│   ├── model/               # ALS model files
│   ├── requirements.txt
│   └── .env                 # DB_URL
├── frontend/                # React app
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── index.js
│   ├── tailwind.config.js
│   ├── package.json
│   └── vite.config.js
├── docker-compose.yml
├── README.md
└── .gitignore
```

## 3. Kế Hoạch Backend (FastAPI)
- **Setup**: `requirements.txt`, `.env`.
- **Endpoints**: /auth/login, /products/, /products/{pid}/[view/cart/purchase], /users/me/recs.
- **DB**: SQLAlchemy async.
- **Model**: Load/train ALS từ Surprise.

## 4. Kế Hoạch Frontend (React + Tailwind)
- **Setup**: Vite + Tailwind.
- **Pages**: Login, Home/Products, Cart, Profile (recs).

## 5. Tích Hợp Model ALS
- `model/train.py`: Train từ DB events.

## 6. Các Bước Triển Khai
1. Setup structure.
2. Backend.
3. Model.
4. Frontend.
5. Testing.
6. Populate & Train.
7. Demo.

## Chạy Dự Án
- Backend: `cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload`
- Frontend: `cd frontend && npm install && npm run dev`

