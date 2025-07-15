from fastapi import HTTPException,status
import httpx

async def spotify_request(method: str, url: str, **kwargs) -> httpx.Response:
    """
    Wraps httpx calls to handle timeouts & transport errors uniformly.
    """
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.request(method, url, **kwargs)
    except httpx.ConnectTimeout:
        raise HTTPException(status_code=status.HTTP_504_GATEWAY_TIMEOUT, detail="Failed to connect to Spotify (timeout).")
    except httpx.ReadTimeout:
        raise HTTPException(status_code=status.HTTP_504_GATEWAY_TIMEOUT, detail="Spotify did not respond in time.")
    except httpx.TransportError as exc:
        # catch-all for other network issues
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=f"Network error contacting Spotify: {str(exc)}")
    
    if resp.status_code==204:
        return {}
    
    data=resp.json() 

    if 200 <= resp.status_code < 300:
        return data

    # auth errors (token expired / revoked) , your dependency could auto‑refresh or force re‑login
    if resp.status_code == 401:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Spotify access token invalid or expired.")

    # Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won't help here.
    if resp.status_code == 403:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Spotify Premium required or BadOAuth request.")
    
    if resp.status_code == 429:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Rate limit exceeded.")

    
    raise HTTPException(resp.status_code, detail=data.get("error", data))

    
