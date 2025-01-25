execute as @e[tag=fire_1] run scoreboard players add @s time 1
execute as @e[tag=fire_1,scores={time=30}] at @s run summon minecraft:firework_rocket ~ ~1 ~ {Tags:["fire_1_1"], LifeTime:30, FireworksItem:{id:"minecraft:firework_rocket",Count:1, tag:{Fireworks:{Explosions:[{Colors:[I;114514, 114514, 114514], Type:1b, Trail:1b, Flicker:false}]}}}}
kill @e[tag=fire_1,scores={time=30}]
execute as @e[tag=fire_1_1] run scoreboard players add @s time 1
execute as @e[tag=fire_1_1,scores={time=30}] at @s run summon minecraft:firework_rocket ~ ~1 ~ {Tags:["fire_1_2"], LifeTime:30, FireworksItem:{id:"minecraft:firework_rocket",Count:1, tag:{Fireworks:{Explosions:[{Colors:[I;1000000, 1000000, 100], Type:1b, Trail:1b, Flicker:false}]}}}}
kill @e[tag=fire_1_1,scores={time=30}]
#execute as @e[tag=fire_1] run scoreboard players add @s time 1
execute as @e[tag=fire_1_2] at @s run function firework2
execute as @e[tag=fire_1_2,score={time=30}] at @s run function firework1_2