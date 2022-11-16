class Sundae:
    
    available_sizes = ["small", "medium", "large"]
    def __init__(self, ice_cream_flavor, *toppings):
        self.ice_cream_flavor = ice_cream_flavor
        self.toppings = toppings
        self.selected_size = next(iter(self.available_sizes))
    def select_size(self, size):
        if size in self.available_sizes:
            self.selected_size = size
            
    @classmethod
    def change_available_sizes(cls, newSizes):
        cls.available_sizes = newSizes 

    @classmethod
    def hot_fudge_sundae(cls):
        return cls("vanilla", "hot fudge", "whipped cream", "cherry")
    
    @classmethod
    def brownie_sundae(cls):
        return Sundae("vanilla", "brownie", "chocolate sauce", "whipped cream", "cherry")
    
# create this test instance if I am running this code directly from
# this file rather than as an import
if __name__ == "__main__":
    # make a sundae
    sundae = Sundae("strawberry", "sprinkles")
    
    # replace Sundae class with new sizes
    Sundae.change_available_sizes(["small", "medium", "large", "x-large"])

    # change my sundae to extra large
    sundae.select_size("x-large")

    # make another sundae
    your_sundae = Sundae("rocky road", "reese pieces", "caramel sauce")
    
    # make a hot fudge sundae
    my_fudgie = Sundae.hot_fudge_sundae()
    
    #make a brownie sundae
    my_fudgie.select_size("x-large")
    my_brownie = Sundae.brownie_sundae()
    
    print("My sundae flavor is " + sundae.ice_cream_flavor)
    print("My sundae size is " + sundae.selected_size)
    print("")
    print("Your sundae flavor is " + your_sundae.ice_cream_flavor)
    print("Your sundae size is " + your_sundae.selected_size)
    print("Your sundae toppings are " + str(your_sundae.toppings))
    print("")
    print("Jonathan's hot fudge sundae size is " + str(my_fudgie.selected_size))
    print("")
    print("Lydia's brownie sundae ice cream is " + my_brownie.ice_cream_flavor)
    