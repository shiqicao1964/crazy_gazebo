import numpy as np

# 定义旋转矩阵
def rotation_matrix(theta, phi):
    Rz = np.array([[np.cos(theta), -np.sin(theta), 0],
                   [np.sin(theta), np.cos(theta), 0],
                   [0, 0, 1]])
    Ry = np.array([[np.cos(phi), 0, np.sin(phi)],
                   [0, 1, 0],
                   [-np.sin(phi), 0, np.cos(phi)]])
    return np.dot(Rz, Ry)

# 定义向量T在平面局部坐标系中的表示
Tp = np.array([0, 0, L])

# 定义平面法向量
N0 = np.array([0, 0, 1])

# 定义偏移角度
theta = np.deg2rad(30) # pitch偏移30度
phi = np.deg2rad(45) # roll偏移45度

# 计算旋转矩阵
R = rotation_matrix(theta, phi)

# 计算向量T在world frame中的表示
Tw = Tp + np.dot(Tp.dot(R), N0) * np.dot(R, N0)

# 计算向量T在z轴方向上的分量
Tz = Tw.dot(np.array([0, 0, 1]))

print("向量T在垂直方向上的分量为：", Tz)
