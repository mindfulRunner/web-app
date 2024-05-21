GitHub
    https://github.com/mindfulRunner/web-app


Data source:
    https://climatedata.imf.org/pages/access-data


Flask project setup steps:

    - create virtual environment
        - python -m venv run_venv
            - C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\web_python\climate_change>python -m venv run_venv

    - activate virtual environment
        - activate
        - deactivate
            - C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\web_python\climate_change>run_venv\Scripts\activate

    - install Flask
        - pip install flask
            - (run_venv) C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\web_python\climate_change>pip install flask

    - check Flask installation status
        (run_venv) C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\web_python\climate_change>flask --version
        Python 3.12.2
        Flask 3.0.2
        Werkzeug 3.0.1

    - install dotenv
        - pip install python-dotenv
            - (run_venv) C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\web_python\climate_change>pip install python-dotenv

    - HTML form doesn't support PUT / DELETE, need to use POST instead
        - https://stackoverflow.com/questions/5162960/should-put-and-delete-be-used-in-forms

Bootstrap
    - navbar color
        - https://getbootstrap.com/docs/5.0/components/navbar/#color-schemes

    - W3Schools Color Picker
        - https://www.w3schools.com/colors/colors_picker.asp

Online CSV reader
    - Tablecruncher
        - https://app.tablecruncher.com/

Pandas
    - https://pandas.pydata.org/docs/reference/index.html
    - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html

    - pip install pandas

PySpark
    - https://spark.apache.org/docs/3.5.1/api/python/reference/pyspark.sql/api/pyspark.sql.SparkSession.read.html#pyspark.sql.SparkSession.read

Matplotlib
    - https://matplotlib.org/stable/api/index.html
    - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html
    - https://www.w3schools.com/python/matplotlib_pyplot.asp

    - pip install matplotlib

Seaborn
    - https://seaborn.pydata.org/api.html
    - https://www.w3schools.com/python/numpy/numpy_random_seaborn.asp

    - pip install seaborn

Email
    - use smtplib (based on Simple Mail Transfer Protocol)
        - https://docs.python.org/3.2/library/smtplib.html
    - https://realpython.com/python-send-email/
        - 2 ways
            - sending email to a public email server requires authentication (login, password for the `from` email)
            - sending email to a local email server - doesn't require authentication
    - choose Option 2 (local email server)
        - need to start email server
            - use aiosmtpd
                - install it
                    pip install aiosmtpd
                
                - start mail server
                    C:\Users\pingl>aiosmtpd -l localhost:1025 -n
        - use local email server
            - means to send email to local email server
                - therefore, not expect to receive real email like gmail
                - but check output of local email server, the output is a kind of email as below

                    ---------- MESSAGE FOLLOWS ----------
                    Subject: forgot password
                    From: admin
                    To: z@z
                    Content-Type: text/plain; charset="utf-8"
                    Content-Transfer-Encoding: 7bit
                    MIME-Version: 1.0
                    X-Peer: ('::1', 63517, 0, 0)

                    temporary password: da5178ca5fb24bae8d729e5c02eee56e
                    ------------ END MESSAGE ------------

How to change password?
    - make sure local email server (aiosmtpd) is started and running as above

    - Sign in -> Forgot password? -> enter Email -> Forgot Password page

    -> then go to command line console to get aiosmtpd SMTP server's email output as follows

        ---------- MESSAGE FOLLOWS ----------
        Subject: forgot password
        From: admin
        To: z@z
        Content-Type: text/plain; charset="utf-8"
        Content-Transfer-Encoding: 7bit
        MIME-Version: 1.0
        X-Peer: ('::1', 63517, 0, 0)

        temporary password: da5178ca5fb24bae8d729e5c02eee56e
        ------------ END MESSAGE ------------

    -> copy temporary password: da5178ca5fb24bae8d729e5c02eee56e to Forgot Password page
    -> continue on Reset Password