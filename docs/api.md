# Cerion API Documentation  

Welcome to the **Cerion API**, your gateway to real-time crypto market insights, memecoin analytics, and AI-powered trading intelligence.  

---

## 1️⃣ API Overview  

Cerion provides a RESTful API to access live market data, token analysis, and AI-driven insights.  

**Base URL:**  
```
https://api.cerion.ai/v1/
```

**Authentication:**  
Cerion uses API keys for authentication. To obtain an API key, register on the **Cerion Dashboard**.  

**Header Example:**  
```sh
Authorization: Bearer YOUR_API_KEY
```

---

## 2️⃣ Endpoints  

### **A. Market Data**  

#### **🔹 Get Live Price**  
Returns the latest price of a given cryptocurrency.  

**Endpoint:**  
```
GET /market/price/{symbol}
```
**Example Request:**  
```sh
curl -H "Authorization: Bearer YOUR_API_KEY" \
     https://api.cerion.ai/v1/market/price/SOL
```
**Response:**  
```json
{
  "symbol": "SOL",
  "price": 102.43,
  "timestamp": 1709832456
}
```

---

### **B. Token Analytics**  

#### **🔹 Get Memecoin Metrics**  
Fetches key performance indicators for a given memecoin.  

**Endpoint:**  
```
GET /token/metrics/{contract_address}
```
**Example Request:**  
```sh
curl -H "Authorization: Bearer YOUR_API_KEY" \
     https://api.cerion.ai/v1/token/metrics/0x123456789abcdef
```
**Response:**  
```json
{
  "name": "Dogecoin",
  "symbol": "DOGE",
  "market_cap": 15000000000,
  "holders": 1200000,
  "liquidity": 4500000
}
```

---

### **C. AI Trading Insights**  

#### **🔹 Predict Market Trends**  
Uses AI models to predict short-term price movements.  

**Endpoint:**  
```
GET /ai/predict/{symbol}
```
**Example Request:**  
```sh
curl -H "Authorization: Bearer YOUR_API_KEY" \
     https://api.cerion.ai/v1/ai/predict/SOL
```
**Response:**  
```json
{
  "symbol": "SOL",
  "prediction": "Bullish",
  "confidence": 87.5,
  "timeframe": "24h"
}
```

---

## 3️⃣ WebSocket for Live Updates  

For real-time price updates, connect via WebSocket:  

**URL:**  
```
wss://api.cerion.ai/ws
```
**Example Subscription:**  
```json
{
  "action": "subscribe",
  "channel": "price",
  "symbol": "SOL"
}
```
**Response Example:**  
```json
{
  "symbol": "SOL",
  "price": 102.50,
  "timestamp": 1709832890
}
```

---

## 4️⃣ Rate Limits  

- **Free Tier:** 60 requests/min  
- **Pro Tier:** 600 requests/min  
- **Enterprise:** Custom  

Rate limits reset every minute. Exceeding limits will result in a `429 Too Many Requests` error.  

---

## 5️⃣ Error Codes  

| Code  | Message                  | Description |
|-------|--------------------------|-------------|
| 400   | Bad Request              | Invalid request format. |
| 401   | Unauthorized             | Invalid API key. |
| 403   | Forbidden                | Insufficient permissions. |
| 404   | Not Found                | Requested data not available. |
| 429   | Too Many Requests        | Rate limit exceeded. |
| 500   | Internal Server Error    | Unexpected server issue. |

---

## 6️⃣ Getting Started  

1. **Sign up** on the **Cerion Dashboard**.  
2. **Generate an API key** in your account settings.  
3. **Start making requests** using the examples above.  

For support, visit our **[Developer Docs](https://docs.cerion.ai)** or join our **Discord community**. 🚀  

