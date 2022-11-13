def get_velocity(x, y):
    y = y - 1
    if x > 0:
        x = x - 1

    return x, y


X_TARGET_MIN = 236
X_TARGET_MAX = 262
Y_TARGET_MIN = -78
Y_TARGET_MAX = -58

VEL_Y_0_MIN = Y_TARGET_MIN
VEL_Y_0_MAX = -Y_TARGET_MIN - 1
VEL_X_0_MAX = X_TARGET_MAX

for i in range(X_TARGET_MAX):
    add_factorial = (i * (i + 1)) / 2
    if add_factorial >= X_TARGET_MIN:
        VEL_X_0_MIN = i
        break

count = 0
results = []

for vel_x_0 in range(VEL_X_0_MIN, VEL_X_0_MAX + 1):
    for vel_y_0 in range(VEL_Y_0_MIN, VEL_Y_0_MAX + 1):
        vel_x = vel_x_0
        vel_y = vel_y_0
        x = vel_x
        y = vel_y
        while True:
            if x > X_TARGET_MAX or y < Y_TARGET_MIN:
                break

            if x >= X_TARGET_MIN and x <= X_TARGET_MAX and y >= Y_TARGET_MIN and y <= Y_TARGET_MAX:
                count += 1
                results.append((vel_x_0, vel_y_0))
                break

            vel_x, vel_y = get_velocity(vel_x, vel_y)
            x += vel_x
            y += vel_y

print(count)
