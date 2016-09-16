# PART ONE
def draw_stars(x):
    for i in range(0,len(x)):
        for val in range(0, x[i]):
            print "*",
        print "\n"

# q = [4, 6, 1, 3, 5, 7, 25]
# draw_stars(q)

# PART TWO
def draw_stars(x):
    for i in range(0,len(x)):
        if isinstance(x[i],str):
            letter = x[i][0].lower()+"";
            print letter*len(x[i])
        else:
            print "*"*x[i]

# x = ["Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
# draw_stars(x)
