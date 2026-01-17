from fastapi import Request, HTTPException
import time
from collections import defaultdict

# Simple In-memory store (Replace with Redis for Production/Clustered Environment)
request_history = defaultdict(list)

async def portfolio_access_limiter(request: Request):
    """
    Prevents AI Scraping and bulk IP theft by limiting 
    asset access per IP/User.
    """
    client_ip = request.client.host
    current_time = time.time()
    
    # Allow 60 asset views per minute
    request_history[client_ip] = [t for t in request_history[client_ip] if current_time - t < 60]
    
    if len(request_history[client_ip]) > 60:
        raise HTTPException(
            status_code=429, 
            detail="Too many requests. Portfolios are protected against automated scraping."
        )
    
    request_history[client_ip].append(current_time)
    return True