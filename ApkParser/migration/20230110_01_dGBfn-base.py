"""
Base
"""

from yoyo import step

__depends__: dict = {}

steps = [
    step(
        """
         create table link(
            id bigserial primary key unique,
            link varchar(2048) not null,
            date_create timestamp default now())
         """,
        "drop table link",
    ),
    step(
        """
         create table client(
            id serial primary key unique,
            name name not null,
            public_key varchar(256) not null,
            private_key varchar(512) not null,
            date_create timestamp default now())
         """,
        "drop table client",
    ),
]
