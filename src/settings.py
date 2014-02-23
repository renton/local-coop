SETTINGS = {}

#SETTINGS['window_x_size'] = 800
#SETTINGS['window_y_size'] = 600
SETTINGS['window_x_size'] = 1280
SETTINGS['window_y_size'] = 1024

SETTINGS['map_window_x_size'] = 1280
SETTINGS['map_window_y_size'] = 1024

SETTINGS['fullscreen_mode'] = True
#SETTINGS['fullscreen_mode'] = False

SETTINGS['map_tile_width'] = 200
SETTINGS['map_tile_height'] = 200

SETTINGS['scale'] = 2
SETTINGS['raw_tile_size'] = 8
SETTINGS['tile_size'] = SETTINGS['scale']*SETTINGS['raw_tile_size']

# FPS
SETTINGS['default_fps'] = 60

# ASSETS
SETTINGS['asset_path'] = "resources/"
SETTINGS['asset_tileset_path'] = SETTINGS['asset_path']+"tilesets/"
SETTINGS['asset_bg_path'] = SETTINGS['asset_path']+"bg/"

# GRAVITY
SETTINGS['action_player_gravity'] = 0.01
SETTINGS['action_player_terminal_velocity'] = 2

SETTINGS['default_gravity'] = 0.9
SETTINGS['default_terminal_velocity'] = 20

# =========================== DATA =======================================

# BIOMES
SETTINGS['biomes'] = {
    'forest'    :{},
    'valley'    :{},
    'coastal'   :{},
    'smog'      :{},
    'floating'  :{},
    'desert'    :{},
    'midnight'  :{},
    'moutnain'  :{}
}

# PRIMARY WEAPONS
SETTINGS['primary_weapons'] = {
    'revolver'          :{},
    'shotgun'           :{},
    'grenade_launcher'  :{},
    'smg'               :{}
}

# SECONDARY WEAPONS
SETTINGS['secondary_weapons'] = {
    'mg'                :{},
    'beam_laser'        :{},
    'rockets'           :{},
    'sniper'            :{}
}

# SPECIAL WEAPONS
SETTINGS['special_weapons'] = {
    'homing_missiles'   :{},
    'needles'           :{},
    'chain_lightning'   :{},
    'reflect'           :{}
}
