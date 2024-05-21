from db import DB

class ForumDB(DB):
    def __init__(self):
        super().__init__(DB.FORUM_DB, DB.FORUM_MAIN_TABLE)

    def create_table(self):
        super().execute_script('data/schema.sql')

    def create_user(self, first_name, last_name, email, salt, password_hash, is_admin):
        sql, args = 'INSERT INTO user (first_name, last_name, email, salt, password_hash, is_admin) VALUES (?, ?, ?, ?, ?, ?)', (first_name, last_name, email, salt, password_hash, is_admin)
        super().insert(sql, args)

    def update_password(self, email, new_password_hash):
        sql, args = 'UPDATE user SET password_hash = ? WHERE email = ?', (new_password_hash, email)
        super().update(sql, args)

    def select_user(self, email):
        sql, args = 'SELECT * FROM user WHERE email = ?', (email,)
        user = super().select_one(sql, args)
        return user

    def get_all_users(self):
        sql, args = 'SELECT * FROM user', ()
        users = super().select_all(sql, args)
        return users

    def create_forum(self, topic, user_email):
        sql, args = 'INSERT INTO forum (topic, user_email) VALUES (?, ?)', (topic, user_email)
        super().insert(sql, args)

    def get_all_forums(self):
        sql, args = 'SELECT * FROM forum', ()
        forums = super().select_all(sql, args)
        return forums

    def create_comment(self, comment, forum_id, user_email):
        sql, args = 'INSERT INTO comment (comment, forum_id, user_email) VALUES (?, ?, ?)', (comment, forum_id, user_email)
        super().insert(sql, args)

    def get_all_comments(self):
        sql, args = 'SELECT * FROM comment', ()
        comments = super().select_all(sql, args)
        return comments
    
    def get_all_comments_by_forum_id(self, forum_id):
        sql, args = 'SELECT * FROM comment WHERE forum_id = ?', (forum_id,)
        comments = super().select_all(sql, args)
        return comments
    
    def delete_forum(self, forum_id):
        # first, delete all comments belonging to this forum
        comments = self.get_all_comments_by_forum_id(forum_id)
        for comment in comments:
            comment_id = comment['id']
            self.delete_comment(comment_id)

        # then delete the forum itself
        sql, args = 'DELETE FROM forum WHERE id = ?', (forum_id,)
        super().delete(sql, args)
    
    def delete_comment(self, comment_id):
        sql, args = 'DELETE FROM comment WHERE id = ?', (comment_id,)
        super().delete(sql, args)
    
    def increment_web_page_visit_count(self, web_page, user_email):
        sql, args = 'SELECT visit_count FROM web_page_count WHERE web_page = ? AND user_email = ?', (web_page, user_email)
        visit_count = super().select_one(sql, args)
        visit_count = 0 if not visit_count else visit_count[0] # if visit_count is None, set it to 0. Otherwise, get its 1st row
        visit_count += 1
        # if this is 1st one, insert it
        # otherwise, update it
        if visit_count == 1:
            sql, args = 'INSERT INTO web_page_count (visit_count, web_page, user_email) VALUES (?, ?, ?)', (visit_count, web_page, user_email)
            super().insert(sql, args)
        else:
            sql, args = 'UPDATE web_page_count SET visit_count = ? WHERE web_page = ? AND user_email = ?', (visit_count, web_page, user_email)
            super().update(sql, args)
    
    def get_web_page_visit_count_by_user(self, web_page, user_email):
        sql, args = 'SELECT visit_count FROM web_page_count WHERE web_page = ? AND user_email = ?', (web_page, user_email)
        count = super().select_one(sql, args)
        return count
    
    def get_web_page_visit_count(self, web_page):
        sql, args = 'SELECT visit_count FROM web_page_count WHERE web_page = ?', (web_page)
        count = super().select_one(sql, args)
        return count
    
    def get_web_site_visit_count(self):
        sql, args = 'SELECT web_page, user_email, visit_count FROM web_page_count ORDER BY web_page, user_email', ()
        visit_report = super().select_all(sql, args)
        return visit_report