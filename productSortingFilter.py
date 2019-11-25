proArr = [
    {
        "pid": 1,
        "p_name": "Laptop",
        "p_cost": 50000,
        "p_brand": "HP",
        "p_rating": 4,
        "p_dis": 30,
        "p_category": "Electronics"
    },
    {
        "pid": 2,
        "p_name": "Laptop",
        "p_cost": 40000,
        "p_brand": "HP",
        "p_rating": 5,
        "p_dis": 20,
        "p_category": "Electronics"
    },
    {
        "pid": 3,
        "p_name": "Laptop",
        "p_cost": 30000,
        "p_brand": "HP",
        "p_rating": 5,
        "p_dis": 55,
        "p_category": "Electronics"
    },
    {
        "pid": 4,
        "p_name": "Laptop",
        "p_cost": 20000,
        "p_brand": "HP",
        "p_rating": 3,
        "p_dis": 60,
        "p_category": "Home"
    }
]

pro = [["p_cost", False], ["p_cost", True], ["p_rating", False], ["p_rating", True], ["p_dis", False], ["p_dis", True]]
sortbyN = int(input(
    "Enter how to sort: 1. Cost Ascending 2. Cost Descending 3. Rating Ascending 4. Rating Descending 5. Discount Ascending 6. Discount Descending "))

proArr.sort(key=lambda e: e[pro[sortbyN - 1][0]], reverse=pro[sortbyN - 1][1])

for i in proArr:
    print(i)
fil = ["p_name", "p_brand", "p_category"]
i = int(input("Enter how to filter 1. Name 2. Brand 3. Category"))
f = filter(None, proArr)

filter(lambda e: e[fil[i - 1]] == name, proArr)
