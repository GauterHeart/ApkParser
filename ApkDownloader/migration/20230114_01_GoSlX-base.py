"""
Base
"""

from yoyo import step

__depends__: dict = {}

steps = [
    step(
        """
         create table download(
            id bigserial primary key unique,
            url varchar(2048) not null,
            filename varchar(512) not null,
            folder varchar(512) not null,
            file_size bigint not null,
            folder_size bigint not null,
            date_create timestamp default now())
         """,
        "drop table download",
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
