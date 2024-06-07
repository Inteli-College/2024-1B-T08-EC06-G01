CREATE TABLE users (
  id serial PRIMARY KEY,
  username text,
  password text,
  admin bool
);

CREATE TABLE robot (
  id serial PRIMARY KEY,
  name text,
  user_id integer REFERENCES users (id)
);

CREATE TABLE media (
  uuid uuid PRIMARY KEY,
  title text,
  type bool,
  date timestamp,
  robot_id integer REFERENCES robot (id)
)

CREATE TABLE temp (
  id serial PRIMARY KEY,
  temp float,
  robot_id integer REFERENCES robot (id)
);

CREATE TABLE location (
  id serial PRIMARY KEY,
  location_x float,
  location_y float,
  robot_id integer REFERENCES robot (id)
);

CREATE TABLE log (
  id serial PRIMARY KEY,
  emergency_button bool,
  ia_request bool,
  username text,
  date timestamp,
  user_id integer REFERENCES users (id)
);
