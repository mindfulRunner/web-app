DROP TABLE IF EXISTS comment;
DROP TABLE IF EXISTS forum;
DROP TABLE IF EXISTS user;

CREATE TABLE user (
    email TEXT PRIMARY KEY,
    salt BLOB NOT NULL,
    password_hash BLOB NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    is_admin INTEGER NOT NULL, -- 1 for true, 0 for false
    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE forum (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT NOT NULL,
    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    user_email TEXT NOT NULL,
    FOREIGN KEY(user_email) REFERENCES user(email)
);

CREATE TABLE comment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comment TEXT NOT NULL,
    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    forum_id INTEGER NOT NULL,
    user_email TEXT NOT NULL,
    FOREIGN KEY(forum_id) REFERENCES forum(id),
    FOREIGN KEY(user_email) REFERENCES user(email)
);

CREATE TABLE web_page_count (
    web_page TEXT NOT NULL,
    user_email TEXT NOT NULL DEFAULT 'nobody@nobody',
    visit_count INTEGER NOT NULL,
    PRIMARY KEY(web_page, user_email)
);