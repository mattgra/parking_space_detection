import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import time

"""
Source / Inspiration: https://github.com/arunponnusamy/cvlib (install opencv-python, tensorflow, cvlib)
Bug: due to this bug - https://github.com/opencv/opencv/issues/20923 - had to change line 29 in
site-packages/cvlib/object_detection.py" from
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
to output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()] and
comment out line 166 based on this bugfix: https://github.com/opencv/opencv/issues/20923
"""


def run_inference(
    img_fp: str,
    output_fp: str = "data/outputs/{timestamp}.png",
    plot_result=False,
) -> list:
    """
    Run inference on input image to count number of cars seen in image.
    :param img_fp: path to input image
    :param output_fp: path where output image will be saved
    :param plot_result: boolean indicating whether to visualize result or not
    :return: list of strings containing detected labels - e.g., ['car', 'tree', ...]
    """

    img = cv2.imread(img_fp)
    bbox, label, conf = cv.detect_common_objects(img, confidence=0.25, model="yolov4-tiny")

    output_image = draw_bbox(img, bbox, label, conf)

    if plot_result:
        plt.ion()
        plt.imshow(output_image)

    output_fp = output_fp.format(timestamp=time.strftime("%Y-%b-%d_%H:%M:%S"))
    plt.imsave(output_fp, output_image)

    return label, output_fp


if __name__ == "__main__":
    run_inference(img_fp="data/test_img_1.png", plot_result=False)
