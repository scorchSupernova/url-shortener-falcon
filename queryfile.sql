CREATE TABLE IF NOT EXISTS users (
    id serial PRIMARY KEY,
    username VARCHAR(512) default NULL,
    email VARCHAR(512) default NULL,
    is_active BOOLEAN default TRUE,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS authentications (
    id serial PRIMARY KEY,
    user_id INT references users (id),
    token TEXT default null,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS url_histories (
    id serial PRIMARY KEY,
    user_id INT,
    actual_url VARCHAR(255) NOT NULL,
    short_url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);