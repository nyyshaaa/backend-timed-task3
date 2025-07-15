[
    {
        "name": "Into the Pieces(电视剧《白色橄榄树》插曲)",
        "artists": [
            "DOROTHY"
        ],
        "album": "白色橄榄树OST",
        "uri": "spotify:track:09yqW0E3KY8jMVBNYAp54k",
        "url": "https://open.spotify.com/track/09yqW0E3KY8jMVBNYAp54k"
    },
    {
        "name": "Skydream",
        "artists": [
            "Radush"
        ],
        "album": "Skydream",
        "uri": "spotify:track:2n71gzCwkR6411Dt3dIydf",
        "url": "https://open.spotify.com/track/2n71gzCwkR6411Dt3dIydf"
    },
    {
        "name": "I'll Be Fine",
        "artists": [
            "fwd/slash",
            "Stridon",
            "Rik Weber"
        ],
        "album": "I’ll Be Fine",
        "uri": "spotify:track:3BsTZdumXj13kA6evuDybG",
        "url": "https://open.spotify.com/track/3BsTZdumXj13kA6evuDybG"
    },
    {
        "name": "Insignificance",
        "artists": [
            "Hebe Tien"
        ],
        "album": "Insignificance",
        "uri": "spotify:track:6HfomODkY1fsoJRgvIHVeE",
        "url": "https://open.spotify.com/track/6HfomODkY1fsoJRgvIHVeE"
    },
    {
        "name": "Skydream - Extended Mix",
        "artists": [
            "Radush"
        ],
        "album": "Skydream",
        "uri": "spotify:track:7I2qkGoICqGb8cIQOqrWYC",
        "url": "https://open.spotify.com/track/7I2qkGoICqGb8cIQOqrWYC"
    },
    {
        "name": "Sonic Serenity",
        "artists": [
            "fwd/slash"
        ],
        "album": "Sonic Serenity",
        "uri": "spotify:track:1QSATY0asrdgRYwiAFUKDX",
        "url": "https://open.spotify.com/track/1QSATY0asrdgRYwiAFUKDX"
    },
    {
        "name": "Celestial",
        "artists": [
            "Nora Van Elken"
        ],
        "album": "Celestial",
        "uri": "spotify:track:2kMd68JKQBkywKtPuLqm2m",
        "url": "https://open.spotify.com/track/2kMd68JKQBkywKtPuLqm2m"
    },
    {
        "name": "Voulez-Vous",
        "artists": [
            "Syzz",
            "Nora Van Elken"
        ],
        "album": "Voulez-Vous",
        "uri": "spotify:track:3uSfyoohZIynHcmOReUrQE",
        "url": "https://open.spotify.com/track/3uSfyoohZIynHcmOReUrQE"
    },
    {
        "name": "Illume - fwd/slash Edit",
        "artists": [
            "Louis Mercier",
            "fwd/slash"
        ],
        "album": "Illume (fwd/slash Edit)",
        "uri": "spotify:track:6NwhgMxC0eYoveYzfhXDyK",
        "url": "https://open.spotify.com/track/6NwhgMxC0eYoveYzfhXDyK"
    },
    {
        "name": "Don't Wanna Let You Go",
        "artists": [
            "fwd/slash"
        ],
        "album": "Don't Wanna Let You Go",
        "uri": "spotify:track:6UZPpeLO9Clo8YCCwwmuP9",
        "url": "https://open.spotify.com/track/6UZPpeLO9Clo8YCCwwmuP9"
    }
]


{
    "name": "Khwahish",
    "artists": [
        {
            "external_urls": {
                "spotify": "https://open.spotify.com/artist/3iGhlvzpXc0UHBQ7klAItX"
            },
            "href": "https://api.spotify.com/v1/artists/3iGhlvzpXc0UHBQ7klAItX",
            "id": "3iGhlvzpXc0UHBQ7klAItX",
            "name": "Mitraz",
            "type": "artist",
            "uri": "spotify:artist:3iGhlvzpXc0UHBQ7klAItX"
        },
        {
            "external_urls": {
                "spotify": "https://open.spotify.com/artist/3E9wPDeQ4FoB8okbcGF0Q7"
            },
            "href": "https://api.spotify.com/v1/artists/3E9wPDeQ4FoB8okbcGF0Q7",
            "id": "3E9wPDeQ4FoB8okbcGF0Q7",
            "name": "Arooh",
            "type": "artist",
            "uri": "spotify:artist:3E9wPDeQ4FoB8okbcGF0Q7"
        }
    ],
    "uri": "spotify:track:5YyXq5rzZyyEbNptsLFz3W"
}

{
    "detail": "Track 47EJ5d0ClIsqpMcfBt52Ji is not in your Top 10."
}

# http://127.0.0.1:8000/spotify/play/09yqW0E3KY8jMVBNYAp54k
{
    "detail": {
        "error": {
            "status": 403,
            "message": "Player command failed: Premium required",
            "reason": "PREMIUM_REQUIRED"
        }
    }
}
# ------------------------------------------------------------------------------
# new version of play any from top-10

# http://127.0.0.1:8000/spotify/top_tracks/play/2

# INFO:     Application startup complete.
# 3BsTZdumXj13kA6evuDybG
# I'll Be Fine
# INFO:     127.0.0.1:53588 - "PUT /spotify/top_tracks/play/2 HTTP/1.1" 403 Forbidden
