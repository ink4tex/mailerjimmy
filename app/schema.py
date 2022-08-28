instructions = [
    'DROP TABLE IF EXITS email;',
    """
        CREATE TABLE email(
            id SERIAL PRIMARY KEY,
            emial TEXT NOT NULL,
            subject TEXT NOT NULL,
            content TEXR NOT NULL
        )
    """
]