import express from 'express';
import cors from 'cors';
import jwt from 'jsonwebtoken';
import { v4 as uuidv4 } from 'uuid';
import pg from 'pg';

const app = express();
app.use(cors({ origin: true, credentials: true }));
app.use(express.json());

const JWT_SECRET = 'dev-secret';

// Optional Postgres
const pool = process.env.DATABASE_URL ? new pg.Pool({ connectionString: process.env.DATABASE_URL }) : null;

// In-memory stores for MVP / fallback
const db = {
  users: [
    { id: uuidv4(), username: 'demo', fullName: 'Demo User', email: 'demo@example.com', password: 'demo123', kycStatus: 'pending', role: 'tourist' },
    { id: uuidv4(), username: 'devansh', fullName: 'Devansh Kumar', email: 'devansh@example.com', password: 'password123', kycStatus: 'verified', role: 'tourist' },
    { id: uuidv4(), username: 'police', fullName: 'Police Officer', email: 'police@example.com', password: 'police123', kycStatus: 'verified', role: 'police' }
  ],
  resetOtps: new Map(),
  kyc: [],
  locations: [],
  geofences: [
    { id: uuidv4(), name: 'Safe Zone', center: { lat: 26.172, lng: 91.745 }, radius_m: 800, risk_level: 'safe' },
    { id: uuidv4(), name: 'Medium Risk', center: { lat: 26.18, lng: 91.74 }, radius_m: 600, risk_level: 'medium' },
    { id: uuidv4(), name: 'Danger Zone', center: { lat: 26.175, lng: 91.735 }, radius_m: 400, risk_level: 'danger' }
  ],
  sos: [],
  alerts: [
    { id: uuidv4(), type: 'gov', severity: 'warning', title: 'Heavy Rain Alert', description: 'Expect waterlogging in low-lying areas', area: null, starts_at: Date.now(), ends_at: Date.now() + 86400000 }
  ],
  efir: [],
  trips: [],
  helpCenters: [
    { id: uuidv4(), type: 'police', name: 'Panbazar Police Station', phone: '100', location: { lat: 26.183, lng: 91.742 }, address: 'Panbazar, Guwahati', hours: '24x7' },
    { id: uuidv4(), type: 'hospital', name: 'GMCH', phone: '108', location: { lat: 26.173, lng: 91.744 }, address: 'Bhangagarh, Guwahati', hours: '24x7' },
    { id: uuidv4(), type: 'fire', name: 'Dispur Fire Station', phone: '101', location: { lat: 26.145, lng: 91.793 }, address: 'Dispur, Guwahati', hours: '24x7' },
    { id: uuidv4(), type: 'ngo', name: 'Red Cross Assam', phone: '+91-361-2549620', location: { lat: 26.193, lng: 91.751 }, address: 'Ambari, Guwahati', hours: '10:00-17:00' }
  ]
};

function signToken(user) {
  return jwt.sign({ sub: user.id, username: user.username, role: user.role || 'tourist' }, JWT_SECRET, { expiresIn: '2h' });
}

function auth(req, res, next) {
  const authz = req.headers.authorization || '';
  const token = authz.startsWith('Bearer ') ? authz.slice(7) : null;
  if (!token) return res.status(401).json({ error: 'Unauthorized' });
  try {
    req.user = jwt.verify(token, JWT_SECRET);
    next();
  } catch {
    res.status(401).json({ error: 'Invalid token' });
  }
}

// Auth
app.post('/api/auth/signup', async (req, res) => {
  const { fullName, email, username, password, dob, gender } = req.body || {};
  if (!fullName || !email || !username || !password) return res.status(400).json({ error: 'Missing fields' });
  if (pool) {
    try {
      const { rows } = await pool.query('select 1 from users where username=$1', [username]);
      if (rows.length) return res.status(409).json({ error: 'Username exists' });
      const id = uuidv4();
      await pool.query('insert into users(id, username, full_name, email, password_hash, dob, gender, kyc_status, role) values($1,$2,$3,$4,$5,$6,$7,$8,$9)', [id, username, fullName, email, password, dob, gender, 'pending', 'tourist']);
      const user = { id, username, fullName, role: 'tourist' };
      return res.json({ ok: true, user, token: signToken(user) });
    } catch (e) { console.error(e); return res.status(500).json({ error: 'db error' }); }
  } else {
    if (db.users.find(u => u.username === username)) return res.status(409).json({ error: 'Username exists' });
    const user = { id: uuidv4(), username, fullName, email, password, dob, gender, kycStatus: 'pending' };
    db.users.push(user);
    res.json({ ok: true, user: { id: user.id, username, fullName }, token: signToken(user) });
  }
});

app.post('/api/auth/login', async (req, res) => {
  const { username, password } = req.body || {};
  if (pool) {
    try {
      const { rows } = await pool.query('select id, username, full_name as "fullName", kyc_status as "kycStatus", coalesce(role,\'tourist\') as role from users where username=$1 and password_hash=$2', [username, password]);
      if (!rows.length) return res.status(401).json({ error: 'Invalid credentials' });
      const user = rows[0];
      return res.json({ ok: true, user, token: signToken(user) });
    } catch (e) { console.error(e); return res.status(500).json({ error: 'db error' }); }
  } else {
    const user = db.users.find(u => u.username === username && u.password === password);
    if (!user) return res.status(401).json({ error: 'Invalid credentials' });
    res.json({ ok: true, user: { id: user.id, username: user.username, fullName: user.fullName, kycStatus: user.kycStatus, role: user.role }, token: signToken(user) });
  }
});

// Forgot password (simulate email OTP)
app.post('/api/auth/forgot', (req, res) => {
  const { email } = req.body || {};
  const user = db.users.find(u => u.email === email);
  if (!user) return res.status(404).json({ error: 'Email not found' });
  const otp = String(Math.floor(100000 + Math.random()*900000));
  db.resetOtps.set(email, { otp, expires: Date.now() + 10*60*1000 });
  // In MVP, we just return the OTP for demo
  res.json({ ok: true, otp });
});

app.post('/api/auth/reset', (req, res) => {
  const { email, otp, newPassword } = req.body || {};
  const entry = db.resetOtps.get(email);
  if (!entry || entry.otp !== otp || Date.now() > entry.expires) return res.status(400).json({ error: 'Invalid/expired OTP' });
  const user = db.users.find(u => u.email === email);
  if (!user) return res.status(404).json({ error: 'User not found' });
  user.password = newPassword;
  db.resetOtps.delete(email);
  res.json({ ok: true });
});

// KYC
app.get('/api/kyc/me', auth, (req, res) => {
  const user = db.users.find(u => u.id === req.user.sub);
  res.json({ status: user?.kycStatus || 'pending' });
});

app.post('/api/kyc/start', auth, (req, res) => {
  const { method, documentType } = req.body || {};
  const record = { id: uuidv4(), user_id: req.user.sub, method, document_type: documentType, status: 'in_progress', created_at: Date.now() };
  db.kyc.push(record);
  res.json({ ok: true, kycId: record.id });
});

app.post('/api/kyc/verify-e-kyc', auth, (req, res) => {
  // simulate success
  res.json({ ok: true, verified: true, kycHash: uuidv4() });
});

app.post('/api/kyc/verify-video', auth, (req, res) => {
  // simulate success
  res.json({ ok: true, verified: true, kycHash: uuidv4() });
});

app.post('/api/kyc/complete', auth, (req, res) => {
  const user = db.users.find(u => u.id === req.user.sub);
  if (user) user.kycStatus = 'verified';
  res.json({ ok: true, status: user?.kycStatus || 'pending' });
});

// Geofences & Alerts
app.get('/api/geofences', (req, res) => {
  res.json(db.geofences);
});

// Admin Geofence CRUD (police)
app.post('/api/admin/geofences', auth, (req, res) => {
  if ((req.user.role || 'tourist') !== 'police') return res.status(403).json({ error: 'forbidden' });
  const { name, center, radius_m, risk_level } = req.body || {};
  if (!name || !center || !radius_m || !risk_level) return res.status(400).json({ error: 'Missing fields' });
  const entry = { id: uuidv4(), name, center, radius_m, risk_level };
  db.geofences.push(entry);
  res.json({ ok: true, geofence: entry });
});

app.delete('/api/admin/geofences/:id', auth, (req, res) => {
  if ((req.user.role || 'tourist') !== 'police') return res.status(403).json({ error: 'forbidden' });
  db.geofences = db.geofences.filter(g => g.id !== req.params.id);
  res.json({ ok: true });
});

app.get('/api/alerts', (req, res) => {
  res.json(db.alerts);
});

// Help Centers (simple distance filter)
app.get('/api/help-centers', (req, res) => {
  const { near, radius = 5000, type } = req.query;
  let list = db.helpCenters;
  if (type) list = list.filter(h => h.type === type);
  if (near) {
    const [latStr, lngStr] = String(near).split(',');
    const lat = parseFloat(latStr), lng = parseFloat(lngStr);
    const toMeters = (a, b) => Math.sqrt(((a.lat - b.lat) * 111000) ** 2 + ((a.lng - b.lng) * 111000) ** 2);
    list = list.map(h => ({ ...h, distance_m: Math.round(toMeters(h.location, { lat, lng })) }))
               .filter(h => h.distance_m <= Number(radius))
               .sort((a, b) => a.distance_m - b.distance_m);
  }
  res.json(list);
});

// Location
app.post('/api/location', auth, async (req, res) => {
  const { lat, lng, accuracy, speed, heading, recordedAt } = req.body || {};
  if (pool) {
    try {
      const id = uuidv4();
      await pool.query(
        'insert into locations(id, user_id, lat, lng, accuracy, speed, heading, recorded_at) values($1,$2,$3,$4,$5,$6,$7, to_timestamp($8/1000.0))',
        [id, req.user.sub, lat, lng, accuracy, speed, heading, recordedAt || Date.now()]
      );
      return res.json({ ok: true });
    } catch (e) { console.error(e); return res.status(500).json({ error: 'db error' }); }
  } else {
    const rec = { id: uuidv4(), user_id: req.user.sub, lat, lng, accuracy, speed, heading, recordedAt: recordedAt || Date.now() };
    db.locations.push(rec);
    res.json({ ok: true });
  }
});

app.get('/api/location/last', auth, async (req, res) => {
  if (pool) {
    try {
      const { rows } = await pool.query('select id, user_id, lat, lng, accuracy, speed, heading, extract(epoch from recorded_at)*1000 as "recordedAt" from locations where user_id=$1 order by recorded_at desc limit 1', [req.user.sub]);
      return res.json(rows[0] || null);
    } catch (e) { console.error(e); return res.status(500).json({ error: 'db error' }); }
  } else {
    const last = [...db.locations].reverse().find(l => l.user_id === req.user.sub);
    res.json(last || null);
  }
});

// SOS
app.post('/api/sos', auth, (req, res) => {
  const { mode = 'manual', notify = ['police','ambulance'], shareLive = true, location } = req.body || {};
  const entry = { id: uuidv4(), user_id: req.user.sub, status: 'active', mode, notify, shareLive, location, created_at: Date.now() };
  db.sos.push(entry);
  res.json({ ok: true, sosId: entry.id });
});

// SOS Admin
app.get('/api/admin/sos', auth, (req, res) => {
  if ((req.user.role || 'tourist') !== 'police') return res.status(403).json({ error: 'forbidden' });
  res.json(db.sos.slice(-100).reverse());
});

app.post('/api/admin/sos/:id/ack', auth, (req, res) => {
  if ((req.user.role || 'tourist') !== 'police') return res.status(403).json({ error: 'forbidden' });
  const s = db.sos.find(x => x.id === req.params.id);
  if (!s) return res.status(404).json({ error: 'not found' });
  s.status = 'acknowledged'; s.acknowledged_at = Date.now();
  res.json({ ok: true });
});

app.post('/api/admin/sos/:id/resolve', auth, (req, res) => {
  if ((req.user.role || 'tourist') !== 'police') return res.status(403).json({ error: 'forbidden' });
  const s = db.sos.find(x => x.id === req.params.id);
  if (!s) return res.status(404).json({ error: 'not found' });
  s.status = 'resolved'; s.resolved_at = Date.now();
  res.json({ ok: true });
});

// E-FIR
app.post('/api/efir', auth, async (req, res) => {
  const { category, subcategory, description, when, where, witnesses = [], evidence = [] } = req.body || {};
  const fir_number = `FIR-${Math.floor(Math.random()*100000)}`;
  if (pool) {
    try {
      const id = uuidv4();
      await pool.query(
        'insert into incident_reports(id, user_id, category, subcategory, description, incident_time, lat, lng, status, fir_number, evidence_urls) values($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11)',
        [id, req.user.sub, category, subcategory, description, when ? new Date(when) : new Date(), where?.lat || null, where?.lng || null, 'submitted', fir_number, JSON.stringify(evidence)]
      );
      return res.json({ ok: true, fir: { id, fir_number } });
    } catch (e) { console.error(e); return res.status(500).json({ error: 'db error' }); }
  } else {
    const entry = { id: uuidv4(), user_id: req.user.sub, category, subcategory, description, when, where, witnesses, evidence, status: 'submitted', fir_number, created_at: Date.now() };
    db.efir.push(entry);
    res.json({ ok: true, fir: entry });
  }
});

// Admin list E-FIR (police only)
app.get('/api/efir', auth, async (req, res) => {
  if ((req.user.role || 'tourist') !== 'police') return res.status(403).json({ error: 'forbidden' });
  if (pool) {
    try {
      const { rows } = await pool.query('select id, user_id, category, subcategory, description, incident_time, lat, lng, status, fir_number from incident_reports order by incident_time desc nulls last limit 100');
      return res.json(rows);
    } catch (e) { console.error(e); return res.status(500).json({ error: 'db error' }); }
  } else {
    res.json(db.efir.slice(-100).reverse());
  }
});

// Trips
app.post('/api/trips', auth, async (req, res) => {
  const { destinationState, startDate, endDate } = req.body || {};
  if (pool) {
    try {
      const id = uuidv4();
      await pool.query('insert into trips(id, user_id, destination_state, start_date, end_date, status) values($1,$2,$3,$4,$5,$6)', [id, req.user.sub, destinationState, startDate, endDate, 'planned']);
      return res.json({ ok: true, trip: { id, user_id: req.user.sub, destinationState, startDate, endDate, status: 'planned' } });
    } catch (e) { console.error(e); return res.status(500).json({ error: 'db error' }); }
  } else {
    const entry = { id: uuidv4(), user_id: req.user.sub, destinationState, startDate, endDate, status: 'planned', created_at: Date.now() };
    db.trips.push(entry);
    res.json({ ok: true, trip: entry });
  }
});

app.get('/api/trips', auth, async (req, res) => {
  if (pool) {
    try {
      const { rows } = await pool.query('select id, user_id, destination_state as "destinationState", start_date as "startDate", end_date as "endDate", status from trips where user_id=$1 order by created_at desc nulls last', [req.user.sub]);
      return res.json(rows);
    } catch (e) { console.error(e); return res.status(500).json({ error: 'db error' }); }
  } else {
    const mine = db.trips.filter(t => t.user_id === req.user.sub);
    res.json(mine);
  }
});

// Emergency Contacts CRUD
app.get('/api/contacts', auth, async (req, res) => {
  if (pool) {
    try {
      const { rows } = await pool.query('select id, name, phone, priority from emergency_contacts where user_id=$1 order by priority asc, name asc', [req.user.sub]);
      return res.json(rows);
    } catch (e) { console.error(e); return res.status(500).json({ error: 'db error' }); }
  } else {
    const list = (db.emergency_contacts || []).filter(c => c.user_id === req.user.sub);
    res.json(list);
  }
});

app.post('/api/contacts', auth, async (req, res) => {
  const { name, phone, priority = 1 } = req.body || {};
  if (!name || !phone) return res.status(400).json({ error: 'Missing fields' });
  if (pool) {
    try {
      const id = uuidv4();
      await pool.query('insert into emergency_contacts(id, user_id, name, phone, priority) values($1,$2,$3,$4,$5)', [id, req.user.sub, name, phone, priority]);
      return res.json({ ok: true, contact: { id, name, phone, priority } });
    } catch (e) { console.error(e); return res.status(500).json({ error: 'db error' }); }
  } else {
    if (!db.emergency_contacts) db.emergency_contacts = [];
    const entry = { id: uuidv4(), user_id: req.user.sub, name, phone, priority };
    db.emergency_contacts.push(entry);
    res.json({ ok: true, contact: entry });
  }
});

app.delete('/api/contacts/:id', auth, async (req, res) => {
  if (pool) {
    try {
      await pool.query('delete from emergency_contacts where id=$1 and user_id=$2', [req.params.id, req.user.sub]);
      return res.json({ ok: true });
    } catch (e) { console.error(e); return res.status(500).json({ error: 'db error' }); }
  } else {
    if (!db.emergency_contacts) db.emergency_contacts = [];
    db.emergency_contacts = db.emergency_contacts.filter(c => !(c.id === req.params.id && c.user_id === req.user.sub));
    res.json({ ok: true });
  }
});

// Police Dashboard (stub)
app.get('/api/dashboard/tourists', (req, res) => {
  const rows = db.users.map(u => {
    const last = [...db.locations].reverse().find(l => l.user_id === u.id);
    return { id: u.id, name: u.fullName, username: u.username, kycStatus: u.kycStatus, lastLocation: last ? { lat: last.lat, lng: last.lng, at: last.recordedAt } : null };
  });
  res.json(rows);
});

app.get('/api/dashboard/heatmap', (req, res) => {
  // Bucket by simple rounding to 3 decimals (~110m)
  const buckets = new Map();
  for (const l of db.locations) {
    const key = `${l.lat.toFixed(3)},${l.lng.toFixed(3)}`;
    buckets.set(key, (buckets.get(key) || 0) + 1);
  }
  const points = Array.from(buckets.entries()).map(([k, c]) => {
    const [lat, lng] = k.split(',').map(Number);
    return { lat, lng, count: c };
  });
  res.json(points);
});

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => console.log(`API running on http://localhost:${PORT}`));


