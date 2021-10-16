from lib import MP4Converter


def main():
    converter = MP4Converter()
    converter.convert(filename='ocean.mts', output='output.mp4')


if __name__ == '__main__':
    main()
