import cv2
from tqdm import tqdm


class MP4Converter:
    def convert(self, filename='ocean.mts', output='output.mp4'):
        video = cv2.VideoCapture('input/' + filename)
        frame_count, fmt, fps, size = self._get_info(video)
        writer = cv2.VideoWriter('output/' + output, fmt, fps, size)

        for _ in tqdm(range(frame_count)):
            ret, frame = video.read()
            writer.write(frame)

        video.release()
        writer.release()

    def _get_info(self, video: cv2.VideoCapture):
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        fmt = cv2.VideoWriter_fourcc(*'mp4v')
        fps = video.get(cv2.CAP_PROP_FPS)
        size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        return frame_count, fmt, fps, size
