class Role(object):
    nationality = "US"
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("%s shooting..." % self.name)

    def got_shot(self):
        print("%s ah...,I got shot..." % self.name)

    def buy_gun(self, gun_name):
        print("just bought %s" % gun_name)
        self.weapon = gun_name


r1 = Role('Alex', 'police', 'AK47')  # 生成一个角色
r2 = Role('Jack', 'terrorist', 'B22')  # 生成一个角色
r2.buy_gun("niubi")
print(r2.weapon,r2.role,r2.nationality)
r1.nationality = "JP"
print(r1.nationality)
Role.nationality = "CN"
print(r1.nationality,r2.nationality)
print(r2)


