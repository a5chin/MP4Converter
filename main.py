import argparse
from pathlib import Path

from moviepy.editor import VideoFileClip


def make_parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--inputs",
        default="inputs",
        type=str,
        help="plese set input file path",
    )
    parser.add_argument(
        "--outputs",
        default="outputs",
        type=str,
        help="plese set gray image path",
    )
    parser.add_argument(
        "--ext",
        default="mp4",
        type=str,
        help="plese set extension",
    )

    return parser.parse_args()


def main():
    args = make_parse()

    inputs = Path(args.inputs)
    input_list = [filename for filename in inputs.glob("**/*")]

    for filename in input_list:
        video = VideoFileClip(filename.as_posix())
        video.write_videofile(
            f"outputs/{filename.stem}.{args.ext}",
            codec='libx264',
            audio_codec='aac',
            remove_temp=True
        )


if __name__ == '__main__':
    main()
