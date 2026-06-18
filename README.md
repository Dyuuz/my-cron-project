# render-keepalive

A lightweight Vercel cron job that periodically pings your Render free-tier
apps to prevent them from spinning down due to inactivity.

## Why

Render's free tier spins down services after 15 minutes of inactivity.
Cold starts can take 30–60 seconds, which is bad UX. This project runs
a scheduled function on Vercel that hits your Render URLs at a fixed
interval, keeping them warm.

## How it works

- A Python serverless function loops through your list of Render URLs
- Vercel's cron scheduler triggers it every 5 minutes (configurable)
- Each run logs the response status of every URL
- Zero cost — runs entirely within Vercel's free hobby tier limits

## Project structure

render-keepalive/
├── api/
│   └── cron.py        # serverless function that pings your URLs
├── requirements.txt
└── vercel.json        # cron schedule config

## Setup

1. Clone the repo
2. Add your Render URLs to the TARGET_URLS list in api/cron.py
3. Install the Vercel CLI and deploy

npm i -g vercel
vercel deploy --prod

## Configuration

Cron schedule in vercel.json:

| Interval       | Expression     |
|----------------|----------------|
| Every 5 min    | */5 * * * *    |
| Every 10 min   | */10 * * * *   |
| Every hour     | 0 * * * *      |

Render spins down after 15 minutes of inactivity, so anything under
that threshold works. Every 5–10 minutes is the sweet spot.

## Logs

View run logs in your Vercel dashboard under the Logs tab.
Each run prints the status of every pinged URL.

## Requirements

- Vercel account (free Hobby tier works)
- Python 3.9+
- requests
