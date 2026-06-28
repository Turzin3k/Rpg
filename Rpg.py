import random

player_name = input("Qual seu nome, guerreiro? ")

print("\nEscolha sua classe:")
print("1 - Guerreiro ⚔️")
print("2 - Mago 🧙‍♂️")
print("3 - Tank 🛡️")

classe = input("Classe: ")

player_hp = 150
xp = 0
level = 1
potion = 2

boss_name = "Rei das Sombras"
boss_hp = 280

print(f"\n⚔️ {player_name}, a batalha lendária começou!")

while player_hp > 0 and boss_hp > 0:

    print("\n--- SUA VEZ ---")
    print("1 - Atacar")
    print("2 - Usar poção")
    print("3 - Habilidade especial 🔥")

    escolha = input("Escolha: ")

    # ⚔️ ataque
    if escolha == "1":
        dano = random.randint(10, 25)

        crit = random.randint(1, 6)
        if crit == 6:
            dano *= 2
            print("💥 CRÍTICO LENDÁRIO!")

        boss_hp -= dano
        xp += 20
        print(f"⚔️ Você deu {dano} de dano!")

    # 💚 poção
    elif escolha == "2":
        if potion > 0:
            heal = random.randint(25, 40)
            player_hp += heal
            potion -= 1
            print(f"💚 Você curou {heal} HP! ({potion} poções restantes)")
        else:
            print("❌ Sem poções!")

    # 🔥 habilidade
    elif escolha == "3":

        if classe == "1":
            dano = random.randint(25, 45)
            print("⚔️ GOLPE DO GUERREIRO!")

        elif classe == "2":
            dano = random.randint(20, 55)
            print("🧙‍♂️ FEITIÇO ARCANO!")

        elif classe == "3":
            dano = random.randint(5, 15)
            player_hp += 25
            print("🛡️ DEFESA REFORÇADA!")

        else:
            dano = 0
            print("❌ Classe inválida!")

        boss_hp -= dano
        xp += 30

    else:
        print("❌ Ação inválida!")

    # 👹 boss
    if boss_hp > 0:
        atk = random.randint(8, 18)

        ultimate = random.randint(1, 8)
        if ultimate == 8:
            atk *= 2
            print("🔥 O BOSS USOU ULTIMATE!")

        player_hp -= atk
        print(f"👹 {boss_name} te deu {atk} de dano!")

    # 📊 status
    print(f"\n❤️ HP: {player_hp}")
    print(f"💀 Boss: {boss_hp}")
    print(f"⭐ XP: {xp} | Level: {level}")

    # 📈 level up
    if xp >= 40:
        level += 1
        xp = 0
        player_hp += 30
        print("📈 LEVEL UP! Você ficou mais forte!")

print("\n--- FIM DA BATALHA LENDÁRIA ---")

if player_hp > 0:
    print(f"🏆 {player_name} DERROTOU O {boss_name}!")
    print("🔥 VOCÊ É UMA LENDA!")
else:
    print(f"☠️ O {boss_name} TE DERROTOU...")
    print("💀 Tente novamente, guerreiro...")