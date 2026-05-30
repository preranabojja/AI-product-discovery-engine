from recommender import recommend_products

results = recommend_products(
    "wireless headphones for gym workouts"
)

for r in results:
    print(r)