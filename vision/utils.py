import cv2 as cv 
import numpy as np
from typing import Sequence

def is_night(image: np.ndarray) -> bool:
    """Checks for day or night and returns True if night"""
    threshold = 127
    mean = image.mean()
    return mean < threshold


def draw_bbox(region_img: np.ndarray, obstacle1: dict, obstacle2: dict) -> None:
    """Draws bounding boxes for the extracted region"""
    cv.rectangle(region_img, (obstacle1["left"], obstacle1["top"]), (
        obstacle1["left"]+obstacle1["width"], obstacle1["top"]+obstacle1["height"]), (0, 255, 0), 1)
    cv.rectangle(region_img,(obstacle2["left"], obstacle2["top"]), (
        obstacle2["left"]+obstacle2["width"], obstacle2["top"]+obstacle2["height"]), (0, 0, 255), 1)
    

def get_contours(image: np.ndarray, Night: bool) -> Sequence[np.ndarray]:
    """Finds contours in images and returns them"""
    if Night:
        _, threshold = cv.threshold(image, 127, 255, cv.THRESH_BINARY)
    else:
        _, threshold = cv.threshold(image, 127, 255, cv.THRESH_BINARY_INV)
    contour, _ = cv.findContours(
        threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    return contour  


