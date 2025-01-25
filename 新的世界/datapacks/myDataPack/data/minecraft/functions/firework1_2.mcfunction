#在比如5*5内随机的位置召唤一堆存活时间短的花里胡哨的烟花，再在超大范围召唤超多花里胡哨的烟花
execute store result score @s x run data get entity @s UUID[0]
scoreboard players operation @s x %= h x
execute store result entity @s Pos[0] double 1.0 run scoreboard players operation @s x += base x
execute store result score @s y run data get entity @s UUID[1]
scoreboard players operation @s y %= h y
execute store result entity @s Pos[1] double 1.0 run scoreboard players operation @s y += base y
execute store result score @s z run data get entity @s UUID[2]
scoreboard players operation @s z %= h z
execute store result entity @s Pos[2] double 1.0 run scoreboard players operation @s z += base z
execute at @s run summon firework_rocket ~ ~ ~ {LifeTime:0,FireworksItem:{id:firework_rocket,Count:1,tag:{Fireworks:{Explosions:[{Type:0,Flicker:1,Colors:[I;3887386,4312372,14602026],Trail:0b}]}}}}
scoreboard players add @e[tag=countingMan] time 1
execute store result score @s x run random value -5..5
execute store result entity @s Pos[0] double 1.0 run scoreboard players operation @s x += base x
execute store result score @s y run random value -10..10
execute store result entity @s Pos[1] double 1.0 run scoreboard players operation @s y += base y
execute store result score @s z run random value -10..10
execute store result entity @s Pos[2] double 1.0 run scoreboard players operation @s z += base z
execute at @s run summon firework_rocket ~ ~ ~ {LifeTime:0,FireworksItem:{id:firework_rocket,Count:1,tag:{Fireworks:{Explosions:[{Type:0,Flicker:1,Colors:[I;3887386,4312372,14602026],Trail:0b}]}}}}
scoreboard players add @e[tag=countingMan] time 1
execute store result score @s x run random value -5..5
execute store result entity @s Pos[0] double 1.0 run scoreboard players operation @s x += base x
execute store result score @s y run random value -10..10
execute store result entity @s Pos[1] double 1.0 run scoreboard players operation @s y += base y
execute store result score @s z run random value -10..10
execute store result entity @s Pos[2] double 1.0 run scoreboard players operation @s z += base z
execute at @s run summon firework_rocket ~ ~ ~ {LifeTime:0,FireworksItem:{id:firework_rocket,Count:1,tag:{Fireworks:{Explosions:[{Type:0,Flicker:1,Colors:[I;3887386,4312372,14602026],Trail:0b}]}}}}
scoreboard players add @e[tag=countingMan] time 1
execute store result score @s x run random value -5..5
execute store result entity @s Pos[0] double 1.0 run scoreboard players operation @s x += base x
execute store result score @s y run random value -10..10
execute store result entity @s Pos[1] double 1.0 run scoreboard players operation @s y += base y
execute store result score @s z run random value -10..10
execute store result entity @s Pos[2] double 1.0 run scoreboard players operation @s z += base z
execute at @s run summon firework_rocket ~ ~ ~ {LifeTime:0,FireworksItem:{id:firework_rocket,Count:1,tag:{Fireworks:{Explosions:[{Type:0,Flicker:1,Colors:[I;3887386,4312372,14602026],Trail:0b}]}}}}
scoreboard players add @e[tag=countingMan] time 1
execute store result score @s x run random value -5..5
execute store result entity @s Pos[0] double 1.0 run scoreboard players operation @s x += base x
execute store result score @s y run random value -10..10
execute store result entity @s Pos[1] double 1.0 run scoreboard players operation @s y += base y
execute store result score @s z run random value -10..10
execute store result entity @s Pos[2] double 1.0 run scoreboard players operation @s z += base z
execute at @s run summon firework_rocket ~ ~ ~ {LifeTime:0,FireworksItem:{id:firework_rocket,Count:1,tag:{Fireworks:{Explosions:[{Type:0,Flicker:1,Colors:[I;3887386,4312372,14602026],Trail:0b}]}}}}
scoreboard players add @e[tag=countingMan] time 1
execute store result score @s x run random value -5..5
execute store result entity @s Pos[0] double 1.0 run scoreboard players operation @s x += base x
execute store result score @s y run random value -10..10
execute store result entity @s Pos[1] double 1.0 run scoreboard players operation @s y += base y
execute store result score @s z run random value -10..10
execute store result entity @s Pos[2] double 1.0 run scoreboard players operation @s z += base z
execute at @s run summon firework_rocket ~ ~ ~ {LifeTime:0,FireworksItem:{id:firework_rocket,Count:1,tag:{Fireworks:{Explosions:[{Type:0,Flicker:1,Colors:[I;3887386,4312372,14602026],Trail:0b}]}}}}
scoreboard players add @e[tag=countingMan] time 1
kill @e[tag=random,limit=1]