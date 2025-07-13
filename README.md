# Spotify API Integration (FastAPI Wrapper)

This project is a lightweight API wrapper built on top of the Spotify Web API. It enables you to:

* Get your Top 10 tracks
* View the currently playing song
* Pause playback
* Start playing any track from your Top 10 list
* Refresh your Spotify access token using a stored refresh token

## ✅ Setup Instructions

### 1. Environment Variables

Create a `.env` file and add the following:

```env
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REFRESH_TOKEN=your_refresh_token  # optional for now
```

### 2. Authorize and Get Initial Code

Open this URL in your browser to authorize access to your Spotify account:

```
https://accounts.spotify.com/authorize?client_id=YOUR_CLIENT_ID&response_type=code&redirect_uri=http://127.0.0.1:8000/spotify/callback&scope=user-top-read%20user-read-playback-state%20user-read-currently-playing%20user-modify-playback-state
```

After authorizing, Spotify will redirect you to:

```
http://127.0.0.1:8000/spotify/callback?code=AUTHORIZATION_CODE
```

Copy that code from the URL.

### 3. Exchange Code for Access + Refresh Token

Use this `curl` request:

```bash
curl -X POST https://accounts.spotify.com/api/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d grant_type=authorization_code \
  -d code=PASTE_CODE_HERE \
  -d redirect_uri=http://127.0.0.1:8000/spotify/callback \
  -d client_id=YOUR_CLIENT_ID \
  -d client_secret=YOUR_CLIENT_SECRET
```

You’ll get back an `access_token` and a `refresh_token`. Save the refresh token to your `.env` file.

## 🎧 Endpoints

All endpoints are prefixed with `/spotify`.

### 1. Get a New Access Token (via refresh token)

```http
POST /spotify/refresh
```

**Response:**

```json
{
  "access_token": "..."
}
```

### 2. Get Top 10 Tracks

```http
GET /spotify/top_tracks
```

**Response:**

```json
{
  "top_tracks": [
    {
      "name": "Track Name",
      "artists": ["Artist"],
      "album": "Album Name",
      "uri": "spotify:track:xxx",
      "url": "https://open.spotify.com/track/xxx"
    },
    ...
  ]
}
```

### 3. Get Currently Playing Song

```http
GET /spotify/now_playing
```

**Response:**

```json
{
  "now_playing": {
    "item": {
      "name": "...",
      "uri": "spotify:track:...",
      "artists": [...],
      ...
    }
  }
}
```

### 4. Pause Playback

```http
POST /spotify/pause
```

**Response:**

```json
{
  "status": "paused"
}
```

### 5. Start Playing a Track from Your Top 10

```http
PUT /spotify/play/{track_id}
```

* Only works for track IDs present in your current Top 10.
* Fails with 400 if the track ID isn’t allowed.

**Example:**

```http
PUT /spotify/play/2n71gzCwkR6411Dt3dIydf
```

**Response:**

```json
{
  "status": "playing",
  "track_id": "2n71gzCwkR6411Dt3dIydf"
}
```

## 🛡️ Notes

* `access_token`s expire after 1 hour. Always use the `/refresh` endpoint to get a new one before calling others.
* All endpoints internally fetch a new access token if needed.
* Auth is currently via `.env` stored `refresh_token`. Can later extend this to support user-specific storage with JWT authentication.
