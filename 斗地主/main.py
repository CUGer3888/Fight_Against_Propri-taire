"""
游戏名称：斗地主
牌：花色+点数
牌型：单张、对子、三张、三带一、三带二、顺子、连对、飞机、飞机带翅膀、四带二、炸弹
"""

class player:
    def __init__(self, name, cards): # 初始化玩家姓名和牌
        self.name = name
        self.cards = cards
        self.回合 = False