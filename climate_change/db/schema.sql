DROP TABLE IF EXISTS comment;
DROP TABLE IF EXISTS forum;
DROP TABLE IF EXISTS user;

CREATE TABLE user (
    email TEXT PRIMARY KEY,
    salt BLOB NOT NULL,
    password_hash BLOB NOT NULL,
    -- first_name TEXT NOT NULL,
    -- last_name TEXT NOT NULL,
    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE forum (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT NOT NULL,
    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE comment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comment TEXT NOT NULL,
    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    forum_id INTEGER,
    user_email TEXT,
    FOREIGN KEY(forum_id) REFERENCES forum(id),
    FOREIGN KEY(user_email) REFERENCES user(email)
);