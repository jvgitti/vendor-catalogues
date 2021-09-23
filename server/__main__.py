from server import init_api, HOST, PORT


def main():
    app = init_api()
    app.run(host=HOST, port=PORT)


if __name__ == "__main__":
    main()