import unittest
from missao import Status
from missao_heranca import GatheringMission, CombatMission, ExplorationMission
from personagem import Character


class Tests(unittest.TestCase):
    def test_gathering(self):
        print("TEST_GATHERING")

        miss = GatheringMission("Fortuna de cogumelos", "", 10, "Cogumelos Azuis", 5)
        self.assertEqual(miss.nome, "Fortuna de cogumelos")
        self.assertEqual(miss.descricao, "")
        self.assertEqual(miss.recompensa, 10)
        self.assertEqual(miss.item_necessario, "Cogumelos Azuis")
        self.assertEqual(miss.quantidade_item, 5)

        miss.nome = "Mudanças sutis"
        miss.descricao = "No topo da montanha Valverte"
        miss.recompensa = 50
        miss.item_necessario = "Rosas Verdes"
        miss.quantidade_item = 10
        self.assertEqual(miss.nome, "Mudanças sutis")
        self.assertEqual(miss.descricao, "No topo da montanha Valverte")
        self.assertEqual(miss.recompensa, 50)
        self.assertEqual(miss.item_necessario, "Rosas Verdes")
        self.assertEqual(miss.quantidade_item, 10)

        miss.iniciar_missao()
        self.assertEqual(miss.status, Status.em_andamento)
        with self.assertRaises(ValueError):
            miss.iniciar_missao()

        miss.concluir_missao(10)
        self.assertEqual(miss.status, Status.concluido)
        with self.assertRaises(ValueError):
            miss.iniciar_missao()
        with self.assertRaises(ValueError):
            miss.concluir_missao(10)

        miss.show()

        print("\n \n")

    def test_combat(self):
        print("TEST_COMBAT")

        miss = CombatMission("Esqueleto gordo", "", 10, "Esqueleto Chefe", 2)
        self.assertEqual(miss.nome, "Esqueleto gordo")
        self.assertEqual(miss.descricao, "")
        self.assertEqual(miss.recompensa, 10)
        self.assertEqual(miss.tipo_inimigo, "Esqueleto Chefe")
        self.assertEqual(miss.inimigos_a_derrotar, 2)

        miss.nome = "Fogo no parquinho"
        miss.descricao = "A criatura recebeu uma melhoria"
        miss.recompensa = 50
        miss.tipo_inimigo = "Ornintorrinco de Fogo"
        miss.inimigos_a_derrotar = 4
        self.assertEqual(miss.nome, "Fogo no parquinho")
        self.assertEqual(miss.descricao, "A criatura recebeu uma melhoria")
        self.assertEqual(miss.recompensa, 50)
        self.assertEqual(miss.tipo_inimigo, "Ornintorrinco de Fogo")
        self.assertEqual(miss.inimigos_a_derrotar, 4)

        miss.iniciar_missao()
        self.assertEqual(miss.status, Status.em_andamento)
        with self.assertRaises(ValueError):
            miss.iniciar_missao()

        miss.concluir_missao(4)
        self.assertEqual(miss.status, Status.concluido)
        with self.assertRaises(ValueError):
            miss.iniciar_missao()
        with self.assertRaises(ValueError):
            miss.concluir_missao(4)

        miss.show()

        print("\n \n")

    def test_exploration(self):
        print("\n \n TEST_EXPLORATION")

        miss = ExplorationMission("Ninguém pode te ouvir", "", 10, "Espaço", 700)
        self.assertEqual(miss.nome, "Ninguém pode te ouvir")
        self.assertEqual(miss.descricao, "")
        self.assertEqual(miss.recompensa, 10)
        self.assertEqual(miss.regiao_destino, "Espaço")
        self.assertEqual(miss.distancia_km, 700)

        miss.nome = "Novos horizontes"
        miss.descricao = "Vamos ver onde o vento leva"
        miss.recompensa = 50
        miss.regiao_destino = "Grandes Prados"
        miss.distancia_km = 30
        self.assertEqual(miss.nome, "Novos horizontes")
        self.assertEqual(miss.descricao, "Vamos ver onde o vento leva")
        self.assertEqual(miss.recompensa, 50)
        self.assertEqual(miss.regiao_destino, "Grandes Prados")
        self.assertEqual(miss.distancia_km, 30)

        miss.iniciar_missao()
        self.assertEqual(miss.status, Status.em_andamento)
        with self.assertRaises(ValueError):
            miss.iniciar_missao()

        miss.concluir_missao(30)
        self.assertEqual(miss.status, Status.concluido)
        with self.assertRaises(ValueError):
            miss.iniciar_missao()
        with self.assertRaises(ValueError):
            miss.concluir_missao(30)

        miss.show()

        print("\n \n")

    def test_character_mission(self):
        print("TEST_CHARACTER_MISSION")

        explore = ExplorationMission("Ninguém pode te ouvir", "", 10, "Espaço", 700)

        combat = CombatMission("Esqueleto gordo ta bombado", "", 10, "Esqueleto Chefe", 2)

        gather = GatheringMission("Fortuna de cogumelos", "", 10, "Cogumelos Azuis", 5)

        charac = Character("Josefino Olambino")

        charac.add_mission(explore)
        charac.add_mission(combat)
        charac.add_mission(gather)

        self.assertEqual(charac.missoes, [explore, combat, gather])

        charac.finish_mission(explore, 700)
        self.assertEqual(charac.xp, 10)
        self.assertEqual(explore.status, Status.concluido)

        with self.assertRaises(ValueError):
            charac.finish_mission(combat, 1)

        outside = ExplorationMission("Missao nao vai estar no personagem", "", 10, "local", 1)
        with self.assertRaises(ValueError):
            charac.finish_mission(outside, 1)

        charac.finish_mission(combat, 2)
        self.assertEqual(charac.xp, 20)
        self.assertEqual(combat.status, Status.concluido)

        charac.finish_mission(gather, 5)
        self.assertEqual(charac.xp, 30)
        self.assertEqual(gather.status, Status.concluido)

        print("\n \n")


if __name__ == "__main__":
    unittest.main()
