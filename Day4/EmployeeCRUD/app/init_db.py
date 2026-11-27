from app.database import Base, get_engine
from app.model import Employee  # noqa: F401


def main() -> None:
    Base.metadata.create_all(get_engine())


if __name__ == "__main__":
    main()