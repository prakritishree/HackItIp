import smartpy as sp

class Tossgame(sp.Contract):
    def __init__(self, winner):
        self.init(
            winner=winner,
            bet_amount=sp.map(l={}, tkey=sp.TAddress, tvalue=sp.TNat),
            side_choice=sp.map(l={}, tkey=sp.TAddress, tvalue=sp.TString)
        )
    
    @sp.entry_point
    def select(self):

        #check
        choices = sp.map({"heads": 1, "tails": 1})
        sp.verify(choices.contains(self.data.side_choice[sp.sender]), message="Invalid side choice(all in lowercase).")
        sp.verify(self.data.bet_amount[sp.sender] < sp.nat(20), message="Enter bet amount more than 20 mutez")

    @sp.entry_point
    def toss_run(self,random_number):
        # Perform coin toss
        new_number=random_number%2
        sp.set_type(new_number, sp.TNat) # 0:heads ; 1:tails ; else re-enter

        sp.if new_number==0:
            sp.if self.data.side_choice[sp.sender] == "heads":
                winner=sp.sender

        sp.else:
            sp.if self.data.side_choice[sp.sender] == "tails":
                winner=sp.sender

        # else:
        #     #re-enter
        #     sp.set_type(random_number, sp.TNat)

    @sp.entry_point
    def get_prize(self):
        sp.if self.data.winner == sp.sender:
            # Send the reward to the winner
            sp.send(self.data.winner, sp.balance)

    @sp.add_test(name = "main")
    def test():
        scenario = sp.test_scenario()
        # Test accounts
        admin = sp.test_account("admin")
        Prakriti = sp.test_account("Prakriti")
        Bhavika = sp.test_account("Bhavika")
        
        # Contract instance
        toss = Tossgame(winner=admin.address)
        scenario += toss
        
        #get Prize
        scenario.h2("Prize recieving")
        scenario += toss.get_prize().run(amount = sp.tez(1), sender = Prakriti)
        scenario += toss.get_prize().run(amount = sp.tez(1), sender = Bhavika)