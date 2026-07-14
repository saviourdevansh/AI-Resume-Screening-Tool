SafeTraveler MVP (SIH)

Run locally (Node 18+)

Backend
- cd safetraveler/backend
- npm install
- npm run dev (http://localhost:4000)

Frontend
- cd safetraveler/frontend
- npx serve (open printed URL)

Demo credentials
- demo / demo123
- devansh / password123

Flow
- Start → Auth Choice → Sign Up (OTP 123456) or Log In → KYC (e‑KYC / Video) → Home → Map / Alerts / E‑FIR

Features
- Auth (signup/login), KYC (simulated), Home
- Map + geofences + alert banner
- SOS button (floating)
- E‑FIR (dummy FIR number)
- i18n (EN/HI/AS) + theme toggle

Docker (one command)
- cd safetraveler
- docker compose up
- Frontend: http://localhost:3000
- Backend API: http://localhost:4000

Seed DB (optional)
- docker exec -it $(docker ps -qf name=db) psql -U safetraveler -d safetraveler -c "create extension if not exists pgcrypto;"
- docker exec -i $(docker ps -qf name=db) psql -U safetraveler -d safetraveler < db_seed.sql

