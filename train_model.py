import joblib
from sklearn.neighbors import KNeighborsClassifier

# Mashq uchun oddiy dataset (real loyihada katta dataset ishlatiladi)
# Har bir qator: [matematika, fizika, biologiya, informatika, tarix, ingliz_tili]
X = [
    [9, 8, 3, 10, 1, 6],  # Dasturlash
    [8, 9, 2, 9, 2, 5],   # Dasturlash
    [2, 1, 10, 1, 3, 4],  # Tibbiyot
    [3, 2, 9, 2, 1, 3],   # Tibbiyot
    [2, 3, 2, 1, 9, 8],   # Tarixshunoslik
    [1, 2, 1, 2, 10, 9],  # Tarixshunoslik
    [5, 4, 2, 3, 6, 10],  # Tilshunoslik
    [4, 3, 1, 2, 5, 9],   # Tilshunoslik
    [8, 7, 3, 6, 3, 5],   # Muhandislik
    [7, 8, 2, 5, 2, 4],   # Muhandislik
]

y = [
    "Dasturlash",
    "Dasturlash",
    "Tibbiyot",
    "Tibbiyot",
    "Tarixshunoslik",
    "Tarixshunoslik",
    "Tilshunoslik",
    "Tilshunoslik",
    "Muhandislik",
    "Muhandislik",
]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

joblib.dump(model, 'recommender_model.pkl')
print("Model saqlandi ✅")