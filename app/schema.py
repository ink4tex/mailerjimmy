instructions = [
    'DROP TABLE IF EXISTS email;',
    """
        CREATE TABLE email(
            id SERIAL PRIMARY KEY,
            emial TEXT NOT NULL,
            subject TEXT NOT NULL,
            content TEXt NOT NULL
        )
    """
]