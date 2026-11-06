import random
import time

import minescript


def run_chunk_cmds(cmds):
    for cmd in cmds:
        try:
            minescript.execute(cmd)
        except Exception:
            pass
        time.sleep(0.005)

def main():
    px, py, pz = minescript.player_position()
    x, y, z = int(px), int(py), int(pz)

    base_clearing = [
        f"fill {x-20} {y} {z-15} {x+120} {y+60} {z+130} minecraft:air",
        f"fill {x-20} {y-1} {z-15} {x+120} {y-1} {z+130} minecraft:polished_blackstone"
    ]
    run_chunk_cmds(base_clearing)

    roads = [
        f"fill {x-20} {y-1} {z+50} {x+120} {y-1} {z+60} minecraft:smooth_quartz",
        f"fill {x-20} {y-1} {z+55} {x+120} {y-1} {z+56} minecraft:sea_lantern",
        f"fill {x+45} {y-1} {z-15} {x+55} {y-1} {z+130} minecraft:smooth_quartz",
        f"fill {x+50} {y-1} {z-15} {x+50} {y-1} {z+130} minecraft:sea_lantern",
    ]
    for h in range(12, 15):
        roads.append(f"fill {x-20} {y+h} {z+53} {x+120} {y+h} {z+57} minecraft:tinted_glass")
        roads.append(f"fill {x-20} {y+h-1} {z+55} {x+120} {y+h-1} {z+56} minecraft:ochre_froglight")
    for f in range(-10, 120, 25):
        roads.append(f"fill {x+50} {y} {z+f} {x+50} {y+11} {z+f+1} minecraft:iron_block")
    run_chunk_cmds(roads)

    street_scenery = []
    for sx in range(x-15, x+115, 12):
        if not (x+40 <= sx <= x+60):
            street_scenery.extend([
                f"setblock {sx} {y} {z+48} minecraft:iron_bars",
                f"setblock {sx} {y+1} {z+48} minecraft:iron_bars",
                f"setblock {sx} {y+2} {z+48} minecraft:sea_lantern",
                f"setblock {sx+1} {y+2} {z+48} minecraft:sculk_vein",
                f"setblock {sx-1} {y+2} {z+48} minecraft:sculk_vein",
                
                f"setblock {sx} {y} {z+62} minecraft:iron_bars",
                f"setblock {sx} {y+1} {z+62} minecraft:iron_bars",
                f"setblock {sx} {y+2} {z+62} minecraft:sea_lantern",
                f"setblock {sx+1} {y+2} {z+62} minecraft:sculk_vein",
                f"setblock {sx-1} {y+2} {z+62} minecraft:sculk_vein",
            ])

    for sx in range(x-18, x+115, 16):
        if not (x+40 <= sx <= x+60):
            street_scenery.extend([
                f"fill {sx} {y} {z+46} {sx+2} {y} {z+46} minecraft:mud_brick_stairs[facing=south]",
                f"fill {sx} {y} {z+64} {sx+2} {y} {z+64} minecraft:mud_brick_stairs[facing=north]",
                
                f"fill {sx+4} {y} {z+45} {sx+5} {y} {z+46} minecraft:moss_block",
                f"setblock {sx+4} {y+1} {z+45} minecraft:flowering_azalea",
                f"setblock {sx+5} {y+1} {z+46} minecraft:spore_blossom",
                
                f"fill {sx+4} {y} {z+64} {sx+5} {y} {z+65} minecraft:moss_block",
                f"setblock {sx+4} {y+1} {z+64} minecraft:flowering_azalea",
                f"setblock {sx+5} {y+1} {z+65} minecraft:spore_blossom",
            ])

    for sz in range(z-10, z+120, 20):
        if not (z+45 <= sz <= z+65):
            street_scenery.extend([
                f"setblock {x+43} {y} {sz} minecraft:polished_andesite",
                f"setblock {x+43} {y+1} {sz} minecraft:heavy_weighted_pressure_plate",
                f"setblock {x+57} {y} {sz} minecraft:polished_andesite",
                f"setblock {x+57} {y+1} {sz} minecraft:heavy_weighted_pressure_plate",
            ])
    run_chunk_cmds(street_scenery)

    monuments = [
        f"fill {x+35} {y} {z+25} {x+39} {y} {z+29} minecraft:chiseled_polished_blackstone",
        f"fill {x+36} {y+1} {z+26} {x+38} {y+3} {z+28} minecraft:netherite_block",
        f"fill {x+37} {y+4} {z+27} {x+37} {y+6} {z+27} minecraft:gilded_blackstone",
        f"setblock {x+37} {y+7} {z+27} minecraft:sea_lantern",
        f"setblock {x+37} {y+5} {z+26} minecraft:lightning_rod[facing=north]",
        f"setblock {x+37} {y+5} {z+28} minecraft:lightning_rod[facing=south]",
        f"setblock {x+36} {y+5} {z+27} minecraft:lightning_rod[facing=west]",
        f"setblock {x+38} {y+5} {z+27} minecraft:lightning_rod[facing=east]",
        
        f"fill {x+35} {y} {z+75} {x+39} {y} {z+79} minecraft:polished_andesite",
        f"fill {x+37} {y+1} {z+77} {x+37} {y+5} {z+77} minecraft:smooth_stone",
        f"fill {x+36} {y+4} {z+76} {x+38} {y+4} {z+78} minecraft:oxidized_cut_copper",
        f"setblock {x+37} {y+6} {z+77} minecraft:verdant_froglight",
    ]
    run_chunk_cmds(monuments)

    sector_alpha = [
        f"fill {x} {y} {z+10} {x+25} {y+50} {z+35} minecraft:smooth_quartz",
        f"fill {x+1} {y+1} {z+11} {x+24} {y+49} {z+34} minecraft:cyan_stained_glass",
    ]
    for floor in range(0, 50, 5):
        sector_alpha.append(f"fill {x-1} {y+floor} {z+9} {x+26} {y+floor} {z+36} minecraft:polished_blackstone_slab")
        sector_alpha.append(f"fill {x+2} {y+floor+1} {z+9} {x+23} {y+floor+1} {z+9} minecraft:flowering_azalea_leaves")
        sector_alpha.append(f"fill {x+2} {y+floor+1} {z+36} {x+23} {y+floor+1} {z+36} minecraft:flowering_azalea_leaves")
        if floor > 0 and floor < 45:
            sector_alpha.extend([
                f"fill {x+2} {y+floor} {z+12} {x+23} {y+floor} {z+33} minecraft:smooth_quartz",
                f"fill {x+3} {y+floor+1} {z+15} {x+5} {y+floor+1} {z+15} minecraft:polished_blackstone_stairs[facing=south]",
                f"setblock {x+4} {y+floor+1} {z+16} minecraft:heavy_weighted_pressure_plate",
                f"setblock {x+5} {y+floor+1} {z+16} minecraft:stone_button[face=floor,facing=south]",
                f"setblock {x+3} {y+floor+1} {z+16} minecraft:flower_pot",
                f"setblock {x+4} {y+floor+1} {z+17} minecraft:warped_stairs[facing=north]",
                f"fill {x+18} {y+floor+1} {z+30} {x+20} {y+floor+1} {z+30} minecraft:polished_blackstone_stairs[facing=north]",
                f"setblock {x+19} {y+floor+1} {z+29} minecraft:heavy_weighted_pressure_plate",
                f"setblock {x+18} {y+floor+1} {z+29} minecraft:stone_button[face=floor,facing=north]",
                f"setblock {x+19} {y+floor+1} {z+28} minecraft:warped_stairs[facing=south]",
                f"setblock {x+12} {y+floor+1} {z+22} minecraft:sea_lantern",
                f"setblock {x+12} {y+floor+1} {z+23} minecraft:glow_lichen",
                
                f"fill {x+22} {y+floor+1} {z+20} {x+22} {y+floor+3} {z+25} minecraft:cyan_terracotta",
                f"fill {x+22} {y+floor+2} {z+23} {x+22} {y+floor+2} {z+24} minecraft:repeater[facing=east]",
                f"setblock {x+21} {y+floor+2} {z+22} minecraft:observer[facing=west]",
            ])
    run_chunk_cmds(sector_alpha)

    sector_beta = [
        f"fill {x+70} {y} {z+10} {x+95} {y+45} {z+35} minecraft:dark_prismarine",
        f"fill {x+71} {y+1} {z+11} {x+94} {y+44} {z+34} minecraft:glass",
    ]
    for floor in range(0, 45, 5):
        sector_beta.append(f"fill {x+69} {y+floor} {z+9} {x+96} {y+floor} {z+36} minecraft:smooth_quartz_slab")
        if floor > 0 and floor < 40:
            sector_beta.extend([
                f"fill {x+72} {y+floor} {z+12} {x+93} {y+floor} {z+33} minecraft:smooth_basalt",
                f"fill {x+75} {y+floor+1} {z+15} {x+77} {y+floor+1} {z+15} minecraft:quartz_stairs[facing=south]",
                f"setblock {x+76} {y+floor+1} {z+16} minecraft:light_weighted_pressure_plate",
                f"setblock {x+76} {y+floor+1} {z+17} minecraft:oak_stairs[facing=north]",
                f"fill {x+88} {y+floor+1} {z+30} {x+90} {y+floor+1} {z+30} minecraft:quartz_stairs[facing=north]",
                f"setblock {x+89} {y+floor+1} {z+29} minecraft:light_weighted_pressure_plate",
                f"setblock {x+89} {y+floor+1} {z+28} minecraft:oak_stairs[facing=south]",
                f"setblock {x+83} {y+floor+1} {z+22} minecraft:ochre_froglight",
                
                f"setblock {x+72} {y+floor+1} {z+25} minecraft:sticky_piston[facing=east]",
                f"setblock {x+73} {y+floor+1} {z+25} minecraft:redstone_block",
                f"setblock {x+72} {y+floor+2} {z+25} minecraft:redstone_lamp",
            ])
    run_chunk_cmds(sector_beta)

    energy_cluster = []
    for sx in [x - 10, x + 20, x + 80, x + 105]:
        for sz in [z + 85, z + 115]:
            energy_cluster.extend([
                f"fill {sx} {y} {sz} {sx+1} {y+12} {sz+1} minecraft:iron_block",
                f"fill {sx-1} {y+13} {sz-1} {sx+2} {y+13} {sz+2} minecraft:smooth_quartz",
                f"fill {sx+0} {y+14} {sz-3} {sx+0} {y+14} {sz+4} minecraft:smooth_quartz",
                f"fill {sx-3} {y+14} {sz+0} {sx+4} {y+14} {sz+0} minecraft:smooth_quartz",
                f"setblock {sx} {y+13} {sz} minecraft:sea_lantern",
            ])
    for rz in range(z-10, z+10, 8):
        energy_cluster.append(f"fill {x+70} {y} {rz} {x+95} {y+1} {rz+5} minecraft:iron_block")
        energy_cluster.append(f"fill {x+71} {y+2} {rz+1} {x+94} {y+2} {rz+4} minecraft:daylight_detector")
    energy_cluster.extend([
        f"fill {x+80} {y} {z-12} {x+86} {y+7} {z-6} minecraft:copper_block",
        f"fill {x+81} {y+1} {z-11} {x+85} {y+6} {z-7} minecraft:air",
        f"fill {x+83} {y+2} {z-9} {x+83} {y+4} {z-9} minecraft:lightning_rod",
        f"fill {x+79} {y} {z-11} {x+87} {y-1} {z+5} minecraft:copper_bulb",
    ])
    run_chunk_cmds(energy_cluster)

    infrastructure = []
    for p in range(-10, 120, 20):
        infrastructure.append(f"fill {x+38} {y} {z+p} {x+39} {y+20} {z+p+1} minecraft:copper_bulb")
        infrastructure.append(f"setblock {x+38} {y+21} {z+p} minecraft:sea_lantern")
    for _ in range(5):
        cx = x + random.randint(-10, 100)
        cz = z + random.randint(52, 58)
        infrastructure.append(f"fill {cx} {y+13} {cz} {cx+4} {y+14} {cz+1} minecraft:warped_planks")
        infrastructure.append(f"fill {cx+1} {y+13} {cz} {cx+3} {y+13} {cz+1} minecraft:pearlescent_froglight")

    infrastructure.extend([
        f"fill {x+46} {y-1} {z+47} {x+54} {y-1} {z+47} minecraft:snow_block",
                f"fill {x+46} {y-1} {z+49} {x+54} {y-1} {z+49} minecraft:snow_block",
        f"fill {x+46} {y-1} {z+61} {x+54} {y-1} {z+61} minecraft:snow_block",
        f"fill {x+46} {y-1} {z+63} {x+54} {y-1} {z+63} minecraft:snow_block",
        
        f"setblock {x+30} {y} {z+47} minecraft:polished_deepslate_wall",
        f"setblock {x+30} {y+1} {z+47} minecraft:polished_blackstone",
        f"setblock {x+30} {y+2} {z+47} minecraft:target",
        f"setblock {x+30} {y+3} {z+47} minecraft:redstone_block",
        
        f"setblock {x+65} {y} {z+63} minecraft:polished_deepslate_wall",
        f"setblock {x+65} {y+1} {z+63} minecraft:polished_blackstone",
        f"setblock {x+65} {y+2} {z+63} minecraft:target",
        f"setblock {x+65} {y+3} {z+63} minecraft:redstone_block",
        
        f"fill {x+30} {y+25} {z+40} {x+65} {y+25} {z+40} minecraft:lightning_rod[facing=east]",
        f"fill {x+40} {y+5} {z-2} {x+40} {y+24} {z-2} minecraft:iron_bars",
        f"fill {x+110} {y+5} {z-2} {x+110} {y+24} {z-2} minecraft:iron_bars",
        
        f"fill {x-1} {y+2} {z+11} {x-1} {y+40} {z+13} minecraft:spore_blossom",
        f"fill {x+26} {y+2} {z+32} {x+26} {y+40} {z+34} minecraft:glow_lichen",
        
        f"fill {x-20} {y+15} {z+52} {x+120} {y+15} {z+52} minecraft:redstone_block",
        f"fill {x-20} {y+15} {z+58} {x+120} {y+15} {z+58} minecraft:redstone_block",

        f"fill {x+15} {y} {z+47} {x+15} {y+4} {z+47} minecraft:cobblestone_wall",
        f"fill {x+14} {y+4} {z+46} {x+16} {y+5} {z+48} minecraft:shroomlight",
        f"fill {x+13} {y+5} {z+45} {x+17} {y+5} {z+49} minecraft:warped_wart_block",
        
        f"fill {x+75} {y} {z+63} {x+75} {y+4} {z+63} minecraft:cobblestone_wall",
        f"fill {x+74} {y+4} {z+62} {x+76} {y+5} {z+64} minecraft:shroomlight",
        f"fill {x+73} {y+5} {z+61} {x+77} {y+5} {z+65} minecraft:warped_wart_block",

        f"fill {x+20} {y+8} {z+49} {x+25} {y+11} {z+49} minecraft:lime_stained_glass",
        f"fill {x+21} {y+9} {z+49} {x+24} {y+10} {z+49} minecraft:sea_lantern",
        
        f"fill {x+80} {y+8} {z+61} {x+85} {y+11} {z+61} minecraft:magenta_stained_glass",
        f"fill {x+81} {y+9} {z+61} {x+84} {y+10} {z+61} minecraft:sea_lantern",

        f"setblock {x+10} {y-1} {z+52} minecraft:sculk_sensor",
        f"setblock {x+35} {y-1} {z+58} minecraft:sculk_sensor",
        f"fill {x-5} {y-1} {z+51} {x+115} {y-1} {z+51} minecraft:iron_bars",
        f"fill {x-5} {y-1} {z+59} {x+115} {y-1} {z+59} minecraft:iron_bars",

        f"fill {x+5} {y} {z+46} {x+8} {y} {z+46} minecraft:smooth_quartz_stairs[facing=south]",
        f"fill {x+5} {y+3} {z+46} {x+8} {y+3} {z+47} minecraft:exposed_cut_copper_slab",
        f"setblock {x+5} {y+1} {z+46} minecraft:iron_bars",
        f"setblock {x+8} {y+1} {z+46} minecraft:iron_bars",
        
        f"fill {x+88} {y} {z+64} {x+91} {y} {z+64} minecraft:smooth_quartz_stairs[facing=north]",
        f"fill {x+88} {y+3} {z+63} {x+91} {y+3} {z+64} minecraft:exposed_cut_copper_slab",
        f"setblock {x+88} {y+1} {z+64} minecraft:iron_bars",
        f"setblock {x+91} {y+1} {z+64} minecraft:iron_bars",

        f"setblock {x+12} {y} {z+47} minecraft:composter",
        f"setblock {x+12} {y+1} {z+47} minecraft:iron_trapdoor[half=top]",
        f"setblock {x+93} {y} {z+63} minecraft:composter",
        f"setblock {x+93} {y+1} {z+63} minecraft:iron_trapdoor[half=top]",

        f"fill {x-15} {y} {z+115} {x-5} {y+12} {z+125} minecraft:gray_concrete",
        f"fill {x-14} {y+1} {z+116} {x-6} {y+11} {z+124} minecraft:air",
        f"fill {x-12} {y} {z+118} {x-8} {y+3} {z+122} minecraft:magma_block",
        f"fill {x-12} {y+4} {z+118} {x-8} {y+4} {z+122} minecraft:tinted_glass",
        f"fill {x-11} {y+5} {z+119} {x-9} {y+15} {z+121} minecraft:iron_block",
        f"fill {x-10} {y+16} {z+120} {x-10} {y+22} {z+120} minecraft:iron_bars",
        f"setblock {x-10} {y+23} {z+120} minecraft:soul_campfire",
        f"fill {x-15} {y+6} {z+117} {x-15} {y+8} {z+123} minecraft:cyan_stained_glass",
        f"fill {x-5} {y+6} {z+117} {x-5} {y+8} {z+123} minecraft:cyan_stained_glass",
        f"fill {x-13} {y+1} {z+115} {x-7} {y+2} {z+115} minecraft:copper_block",
        f"fill {x-11} {y+1} {z+114} {x-9} {y+1} {z+114} minecraft:lightning_rod[facing=north]",
        f"fill {x-10} {y+2} {z+114} {x-10} {y+2} {z+114} minecraft:sea_lantern",
        f"fill {x-10} {y} {z+114} {x-10} {y+1} {z+40} minecraft:lightning_rod[facing=north]",

        f"fill {x-15} {y-1} {z-10} {x+25} {y-1} {z+5} minecraft:moss_block",
        f"fill {x-10} {y-1} {z-8} {x+15} {y-1} {z+2} minecraft:water",
        f"fill {x-15} {y} {z-10} {x-15} {y+2} {z+5} minecraft:oak_leaves",
        f"fill {x-15} {y} {z-10} {x+25} {y+2} {z-10} minecraft:oak_leaves",
        f"fill {x+25} {y} {z-10} {x+25} {y+2} {z+5} minecraft:oak_leaves",
        f"fill {x-5} {y} {z-4} {x-5} {y+4} {z-4} minecraft:oak_log",
        f"fill {x-7} {y+4} {z-6} {x-3} {y+6} {z-2} minecraft:flowering_azalea_leaves",
        f"fill {x+10} {y} {z-2} {x+10} {y+5} {z-2} minecraft:iron_block",
        f"fill {x+9} {y+5} {z-3} {x+11} {y+6} {z-1} minecraft:pearlescent_froglight",
        f"setblock {x+5} {y} {z+3} minecraft:mossy_cobblestone_stairs[facing=north]",
        f"setblock {x+6} {y} {z+3} minecraft:mossy_cobblestone_stairs[facing=north]",

        f"fill {x-1} {y+5} {z+10} {x-1} {y+20} {z+10} minecraft:verdant_froglight",
        f"fill {x+96} {y+5} {z+10} {x+96} {y+20} {z+10} minecraft:pearlescent_froglight"
    ])
    run_chunk_cmds(infrastructure)

if __name__ == "__main__":
    main()
