# date : 2021/02/16
# author : BoB1754
# Help by : Molly1302
# description : For Music Maker in minecraft world.

blocks = {
	'planks':'bass',
	'sand':'snare',
	'soul_soil':'snare',
	'glass':'hat',
	'stained_glass':'hat',
	'stone':'bd',
	'gold_block':'bell',
	'clay':'flute',
	'packed_ice':'chime',
	'wool':'guitar',
	'bone_block':'xylophone',
	'iron_block':'iron_xylophone',
	'soul_sand':'cow_bell',
	'pumpkin':'didgeridoo',
	'emerald_block':'bit',
	'hay_block':'banjo',
	'glowstone':'pling',
	'honey_block':'harp'
}

pitch = [
	0.5,
	0.529732,
	0.561231,
	0.594604,
	0.629961,
	0.667420,
	0.707107,
	0.749154,
	0.793701,
	0.840896,
	0.890899,
	0.943874,
	1,
	1.059463,
	1.122462,
	1.189207,
	1.259921,
	1.334840,
	1.414214,
	1.498307,
	1.587401,
	1.681793,
	1.781797,
	1.887749,
	2
]

def get_pitch(n) :
	return str(pitch[n-1])

def chest_func(index, block, sound_name, high) :
	result = ""
	for h in range(high) :
		result += f"execute @e[type=chest_minecart] ~ ~ ~ detect ^-{index+1} ^{h} ^ {block} -1 execute @a ~ ~ ~ playsound note.{sound_name} @s ~ ~ ~ 1.0 {get_pitch(index)}" + "\n"
	return result

with open('detect_blocks.mcfunction', 'w') as f :
	for block in list(blocks.keys()) :
		for i in range(1, 26) :
			f.write(chest_func(i, block, blocks[block], 10))