-- Run after creating tables

insert into users (id, username, full_name, email, password_hash, kyc_status, role)
values
  (gen_random_uuid(), 'demo', 'Demo User', 'demo@example.com', 'demo123', 'pending', 'tourist'),
  (gen_random_uuid(), 'devansh', 'Devansh Kumar', 'devansh@example.com', 'password123', 'verified', 'tourist'),
  (gen_random_uuid(), 'police', 'Police Officer', 'police@example.com', 'police123', 'verified', 'police')
on conflict do nothing;

-- Sample trips (link to existing users by username)
with u as (
  select id, username from users where username in ('demo','devansh')
)
insert into trips (id, user_id, destination_state, start_date, end_date, status)
select gen_random_uuid(), (select id from u where username='devansh'), 'Assam', current_date, current_date + interval '3 days', 'planned'
on conflict do nothing;

-- Contacts
with u as (select id from users where username='devansh')
insert into emergency_contacts (id, user_id, name, phone, priority)
values (gen_random_uuid(), (select id from u), 'Parent', '+91-90000-00000', 1)
on conflict do nothing;

-- Incident reports
with u as (select id from users where username='demo')
insert into incident_reports (id, user_id, category, description, incident_time, lat, lng, status, fir_number)
values (gen_random_uuid(), (select id from u), 'Theft', 'Bag snatched at market', now() - interval '1 day', 26.172, 91.745, 'submitted', 'FIR-12345')
on conflict do nothing;

-- Locations heat
with u as (select id from users where username='devansh')
insert into locations (id, user_id, lat, lng, accuracy, recorded_at)
values
  (gen_random_uuid(), (select id from u), 26.172, 91.745, 10, now() - interval '10 minutes'),
  (gen_random_uuid(), (select id from u), 26.176, 91.748, 12, now() - interval '8 minutes'),
  (gen_random_uuid(), (select id from u), 26.179, 91.742, 9,  now() - interval '5 minutes');

