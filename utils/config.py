# Region coordinates
region_x1 = 584
region_y1 = 164
region_x2 = 1336
region_y2 = 352

# obstacle coordinates
obstacle_x1 = 673
obstacle_y1 = 301
obstacle_x2 = 699
obstacle_y2 = 320

region = {
    "top": region_y1,
    "left": region_x1,
    "width": region_x2-region_x1,
    "height": region_y2-region_y1
}

obstacle = {
    "top": obstacle_y1-region_y1,
    "left": obstacle_x1 - region_x1,
    "width": obstacle_x2 - obstacle_x1,
    "height": obstacle_y2 - obstacle_y1
}
