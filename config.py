# Current configuration are for zoom of 100

# Region coordinates
region_x1 = 584
region_y1 = 164
region_x2 = 1336
region_y2 = 352

# obstacle coordinates
obstacle_x1 = 665 
obstacle_y1 = 312 #309
obstacle_x2 = 760    
obstacle_y2 = 316

# pterodactyl coordinates
pterodactyl_x1 = 680
pterodactyl_y1 = 267  
pterodactyl_x2 = 715 #710
pterodactyl_y2 = 275

# sky coordinates
sky_x1 = 1320
sky_y1 = 342
sky_x2 = 1332
sky_y2 = 348

region = {
    "top": region_y1,
    "left": region_x1,
    "width": region_x2-region_x1,
    "height": region_y2-region_y1
}

cactus = {
    "top": obstacle_y1-region_y1,
    "left": obstacle_x1 - region_x1,
    "width": obstacle_x2 - obstacle_x1,
    "height": obstacle_y2 - obstacle_y1
}

pterodactyl = {
    "top": pterodactyl_y1-region_y1,
    "left": pterodactyl_x1-region_x1,
    "width": pterodactyl_x2-pterodactyl_x1,
    "height": pterodactyl_y2-pterodactyl_y1
}

sky = {
    "top": sky_y1-region_y1,
    "left": sky_x1 - region_x1,
    "width": sky_x2 - sky_x1,
    "height": sky_y2-sky_y1
}
