from src.google_meta import GoogleMeta


def main():
    meta = GoogleMeta()
    meta.run_to_local()
    meta.run_to_renpy()


if __name__ == '__main__':
    main()
