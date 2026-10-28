from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Text,
)

engine = create_engine(
    "sqlite:///quiz.db",
    echo=False
)

metadata = MetaData()

questions = Table(
    "questions",
    metadata,

    Column("id", Integer, primary_key=True),

    Column("pdf_name", String),

    Column("question", Text),

    Column("option_a", Text),

    Column("option_b", Text),

    Column("option_c", Text),

    Column("option_d", Text),
)

metadata.create_all(engine)