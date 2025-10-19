import mss
import cv2 as cv
from typing import Dict
import numpy as np


def extract_game_region(region: Dict[str, int]) -> np.ndarray:
    """Extracts game region from screen and returns BGR image"""
    with mss.mss() as sct:
        screenshot = sct.grab(region)
    region_img = np.array(screenshot)
    region_img = cv.cvtColor(region_img, cv.COLOR_BGRA2BGR)
    return region_img


def extract_obstacles_region(region: np.ndarray, obstacle1: Dict[str, int], obstacle2: Dict[str, int]) -> tuple:
    """Extracts obstacles(cactus and pterodactyl) and returns grayscale image"""
    cactus_img = region[obstacle1["top"]:obstacle1["top"]+obstacle1["height"] +
                        1, obstacle1["left"]:obstacle1["left"]+obstacle1["width"]]
    pterodactyl_img = region[obstacle2["top"]:obstacle2["top"] +
                             obstacle2["height"], obstacle2["left"]:obstacle2["left"]+obstacle2["width"]]
    cactus_img = cv.cvtColor(cactus_img, cv.COLOR_BGR2GRAY)
    pterodactyl_img = cv.cvtColor(pterodactyl_img, cv.COLOR_BGR2GRAY)
    return cactus_img, pterodactyl_img


def extract_sky_region(region: np.ndarray, sky: Dict[str, int]) -> np.ndarray:
    """Extracts sky region and returns grayscale image"""
    sky_img = region[sky["top"]:sky["top"]+sky["height"] +
                     1, sky["left"]:sky["left"]+sky["width"]]

    sky_img = cv.cvtColor(sky_img, cv.COLOR_BGR2GRAY)
    return sky_img
