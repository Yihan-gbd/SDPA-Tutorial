import math
class FlowerShop:
    Bouquet_Data = {
        "Fern-tastic":{
            "materials":{"Greenery":4, "Roses":0, "Daisies":2},
            "Prepare_Time":20,
            "Demand":175,
            "Price":18.50,
        },
        "Be-Leaf in Yourself ":{
            "Materials":{"Greenery":2, "Roses":3, "Daisies":3}, 
            "Prepare_Time":30,
            "Demand":100,
            "Price":17.75,
        },
        "You Rose to the Occasion":{
            "Materials":{"Greenery":2, "Roses":4, "Daisies":2},
            "Prepare_Time":45,
            "Demand":250,
            "Price":32.50,
        }, 
    }
    class Greenhouse:{
        "Roses":{"Capacity":200, "Depreciation":0.40, "Costs":1.50},
        "Daisies":{"Capacity":250, "Depreciation":0.15, "Costs":0.80},
        "Greenery":{"Capacity":400, "Depreciation":0.05, "Costs":0.20},
    }
    class Vendor:{
        "Evergreen Essentials":{"Rose":2.80, "Daisies":1.50, "Greenery" :0.95},
        "FloraGrowDistributions":{"Roses":1.60, "Daisies":1.20, "Greenery":1.80},
    }
    Rent = 800
    Florists_Hours = 80
    Flourists_Salary = 15.50