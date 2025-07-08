import random




name = input("What's your name oh Brave Adventurer: ")
def main():
    
    while True:
        cl = input("choose your class:- A) Mage B)Knight ").capitalize()
        if cl in ["Mage","Knight"]:
            break
        else:
            print("please choose a valid class: ")
    enemy1 = "Atreus"
    enemy2 = "Wezaemon"
    while True:
        direction = input("Go left or right?").lower().strip()
        if direction in ["left","right"]:
        
            if direction == "left":
                print(f"{enemy1} the {cl} Slayer has appeared get ready to fight ")
            else:
                print(f"{enemy2} the Tombguard has appeared get ready to fight")
            break           
        else:
                print("Please choose left or right.")
                
    player_attacks(cl,direction)
   

    ... 
               

def player_attacks(cl,direction):
    Mage_attacks=["fireball","moonlight_shard","frost_bite","mana_burst"]
    Knight_attacks=["shield_dash","crushing_lunge","judgement_slash","kingslayer"]
    Mage_dmg =           {"fireball":10,
                         "moonlight_shard":12,
                         "frost_bite":8,
                         "mana_burst": 9,}
    Knight_dmg       = {"shield_dash":10,
                         "crushing_lunge":12,
                         "judgement_slash":8,
                         "kingslayer": 9,}
    
    enemy_attack_Atreus={"bladed_frenzy":10,
                         "executioner's_lunge":12,
                         "crimson_flurry":8,
                         "heart_piercer": 9,}
    enemy_attack_Wezaemon={"grave_smash":10,
                         "soul_drain":12,
                         "rot_burst":8,
                         "wailing_tombstone": 9,}
    boss_H=100
    player_H=100
    while boss_H>0 and player_H>0:
        
        

        if cl=="Mage":
            while True:
                p=input(f"your turn:\nchoose your attack {Mage_attacks}").strip().lower()
                if p in Mage_attacks:


                    
                    print(f"{name} used {p} it did {Mage_dmg[p]} damage")
                    boss_H= boss_H-Mage_dmg[p]
                    if boss_H<=0:
                        boss_H=0
                        print(f"{boss_H} hp left you win")
                        break
                        
                    else:
                        print(f"Enemy: {boss_H} hp left")
                        break
                    
                else:
                    print("execute a valid attack")

                
            
            
        else:
            while True:
                p=input(f"your turn:\nchoose your attack {Knight_attacks}").strip().lower()
                if p in Knight_attacks:


                    
                    print(f"{name} used {p} it did {Knight_dmg[p]} damage")
                    boss_H= boss_H-Knight_dmg[p]
                    if boss_H<=0:
                        boss_H=0
                        print(f"{boss_H}/100 hp left you win")
                        break
                        
                        
                    else:
                        print(f"Enemy: {boss_H}/100 hp left")
                        break    
                else:
                    print("enter a valid attack")
        if boss_H==0:
            break            
        if direction== "left":
            
            
            attacks = random.choice(["bladed_frenzy",
                                    "executioner's_lunge",
                                    "crimson_flurry",
                                    "heart_piercer"])
            player_H=player_H-enemy_attack_Atreus[attacks]
            print(f"Atreus chooses {attacks}")
            print(f"this attack did {enemy_attack_Atreus[attacks]} damage")
            if player_H<=0:
                player_H=0
                print(f"your hp: {player_H} you lose")
                break
                
            else:
                print(f"your hp: {player_H}")

            

            

        else:
            attacks=random.choice(["grave_smash",
                                "soul_drain",
                                "rot_burst",
                                "wailing_tombstone"])
            print(f"wezaemon chooses {attacks}")
            print(f"this attack did {enemy_attack_Wezaemon[attacks]} damage")
            player_H=player_H-enemy_attack_Wezaemon[attacks]
            if player_H<=0:
                player_H=0
                print(f"your hp: {player_H} you lose")
                break
                
            else:
                print(f"your hp: {player_H}")               
    if player_H == 0:
        print("You have been defeated. Better luck next time!")
    elif boss_H == 0:
        print("Victory! The enemy has been slain!")
        
    ...
while True:
    main()
    play_again= input("Do you want to play again? (yes/no):").lower().strip()
    if play_again!="yes":
        print("Thanks for playing adventurer")
        break



    
    
        

    
         
 
    
    
