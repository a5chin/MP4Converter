from lib import MTSConverter


def main():
    converter = MTSConverter()
    converter.convert(filename='ocean.mts', output='output.mp4')


if __name__ == '__main__':
    main()
