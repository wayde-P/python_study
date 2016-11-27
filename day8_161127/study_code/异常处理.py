try:
    int("4")
    li = [11,22]
except IndexError as e:
    pass
except ValueError as e:
    pass
else:
    print("else")
finally:
    print("zuihou ")