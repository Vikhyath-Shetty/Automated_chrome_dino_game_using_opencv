import numpy as np
from typing import Tuple
from .utils import draw_bbox, is_night, get_contours
from .extract import extract_game_region, extract_obstacles_region, extract_sky_region
from config import region, cactus, pterodactyl, sky


def detect_cactus(image: np.ndarray, night: bool) -> bool:
    """Detects cactus(using contours) and returns True if found"""
    contours = get_contours(image, night)
    return len(contours) > 0


def detect_pterodactyl(image: np.ndarray, night: bool) -> bool:
    """Detects pterodactyl(using contours) and returns True if found"""
    contours = get_contours(image, night)
    return len(contours) > 0


def detect_obstacles() -> Tuple[np.ndarray, bool, bool]:
    """Detects obstacles(cactus and pterodactyl) in Game region
    Return: Game Region(for display) and tuple of boolean(cactus,pterodactyl)"""
    game_img = extract_game_region(region)
    cactus_img, pterodactyl_img = extract_obstacles_region(
        game_img, cactus, pterodactyl)
    sky_image = extract_sky_region(game_img, sky)

    # draw_bbox(game_img, cactus, pterodactyl)

    night = is_night(sky_image)
    cactus_detected = detect_cactus(cactus_img, night)
    pterodactyl_detected = detect_pterodactyl(pterodactyl_img, night)

    return game_img, cactus_detected, pterodactyl_detected
