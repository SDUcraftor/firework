
execute store result score @s x run random value -10..10
execute store result entity @s Pos[0] double 1.0 run scoreboard players operation @s x += base x
execute store result score @s y run random value -10..10
execute store result entity @s Pos[1] double 1.0 run scoreboard players operation @s y += base y
execute store result score @s z run random value -100..100
execute store result entity @s Pos[2] double 1.0 run scoreboard players operation @s z += base z
execute at @s run summon firework_rocket ~ ~ ~ {LifeTime:20,FireworksItem:{id:firework_rocket,Count:1,tag:{Fireworks:{Explosions:[{Type:0,Trail:1,Colors:[I;11743532,14188952,14602026],FadeColors:[I;11743532,14188952,14602026]}],Flight:1}}}}
scoreboard players add @e[tag=countingMan2] time 1

kill @e[tag=random,limit=1]