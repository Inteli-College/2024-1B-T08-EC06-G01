-- Criação da tabela users
CREATE TABLE users (
  id serial PRIMARY KEY,
  username text,
  password text,
  admin bool
);

-- Criação da tabela robot
CREATE TABLE robot (
  id serial PRIMARY KEY,
  name text,
  user_id integer REFERENCES users (id)
);

-- Criação da tabela media
CREATE TABLE media (
  uuid uuid PRIMARY KEY,
  title text,
  type bool,
  date timestamp,
  robot_id integer REFERENCES robot (id)
);

-- Criação da tabela log
CREATE TABLE log (
  id serial PRIMARY KEY,
  emergency_button bool,
  ia_request bool,
  username text,
  date timestamp,
  user_id integer REFERENCES users (id)
);
