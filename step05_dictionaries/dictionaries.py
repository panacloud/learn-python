best_languages = {"ml": "python", "web": "javascript", "enterprise": "java", "webassembly": "rust"}
print(best_languages)
print(best_languages["ml"])

best_languages["datascience"] = "R"
print(best_languages)

del best_languages["datascience"]
print(best_languages)

for key, value in best_languages.items():
    print(key)