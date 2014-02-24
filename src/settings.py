SETTINGS = {}

#SETTINGS['window_x_size'] = 800
#SETTINGS['window_y_size'] = 600
SETTINGS['window_x_size'] = 1280
SETTINGS['window_y_size'] = 1024

SETTINGS['map_window_x_size'] = 1280
SETTINGS['map_window_y_size'] = 1024

#SETTINGS['fullscreen_mode'] = True
SETTINGS['fullscreen_mode'] = False

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
SETTINGS['default_terminal_velocity'] = 15

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
SETTINGS['w_param_order'] = ['min_dmg','max_dmg','bullet_life','speed','accuracy','num_projs','firerate','reload_time','clip_size','crit_chance','etype']

SETTINGS['primary_weapons'] = {
    'revolver'          :{
                            'min_dmg':5,
                            'max_dmg':10,
                            'bullet_life':100,
                            'speed':10,
                            'accuracy':5,
                            'num_projs':1,
                            'firerate':10,
                            'reload_time':100,
                            'clip_size':60000,
                            'crit_chance':10,
                            'etype':'f_projs'
                        },
    'shotgun'           :{},
    'grenade_launcher'  :{},
    'smg'               :{}
}

# SECONDARY WEAPONS
SETTINGS['secondary_weapons'] = {
    'mg'                :{
                            'min_dmg':5,
                            'max_dmg':10,
                            'bullet_life':100,
                            'speed':15,
                            'accuracy':10,
                            'num_projs':3,
                            'firerate':0,
                            'reload_time':100,
                            'clip_size':60000,
                            'crit_chance':10,
                            'etype':'f_projs'
                        },
    'beam_laser'        :{},
    'rockets'           :{},
    'sniper'            :{
                            'min_dmg':5,
                            'max_dmg':10,
                            'bullet_life':100,
                            'speed':15,
                            'accuracy':0,
                            'num_projs':1,
                            'firerate':200,
                            'reload_time':100,
                            'clip_size':600000,
                            'crit_chance':10,
                            'etype':'f_projs'
                        }
}

# SPECIAL WEAPONS
SETTINGS['special_weapons'] = {
    'homing_missiles'   :{},
    'needles'           :{},
    'chain_lightning'   :{},
    'reflect'           :{}
}
