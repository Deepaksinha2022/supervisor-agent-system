from app.prompts.ab_router import choose_prompt

v1 = 0
v2 = 0

for _ in range(100):

    version = choose_prompt()

    if version == "v1":
        v1 += 1
    else:
        v2 += 1

print("v1:", v1)
print("v2:", v2)