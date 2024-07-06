import torch
import numpy as np

torch.manual_seed(1)   # torch.manual_seed(seed)函数用于设置CPU中随机数生成的种子

# ===============================  exmaple 1 ===============================
# 通过torch.tensor创建张量
#
# flag = True
flag = False
if flag:
    arr = np.ones((3, 3))
    print("ndarray的数据类型：", arr.dtype)

    # t = torch.tensor(arr, device='cuda')
    t = torch.tensor(arr)

    print(t)

# ===============================  exmaple 2 ===============================
# 通过torch.from_numpy创建张量  (tensor和numpy原ndarray共享内存)
# flag = True
flag = False
if flag:
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    t = torch.from_numpy(arr)
    # print("numpy array: ", arr)
    # print("tensor : ", t)

    # print("\n修改arr")
    # arr[0, 0] = 0
    # print("numpy array: ", arr)
    # print("tensor : ", t)

    print("\n修改tensor")
    t[0, 0] = -1
    print("numpy array: ", arr)
    print("tensor : ", t)

# ===============================  exmaple 3 ===============================
# 通过torch.zeros创建张量（全0张量）
# flag = True
flag = False
if flag:
    out_t = torch.tensor([1])

    t = torch.zeros((3, 3), out=out_t)

    print(t, '\n', out_t)
    print(id(t), id(out_t), id(t) == id(out_t))

# ===============================  exmaple 4 ===============================
# 通过torch.full创建 全1张量
# flag = True
flag = False
if flag:
    t = torch.full((3, 3), 1)
    print(t)

# ===============================  exmaple 5 ===============================
# 通过torch.arange创建 等差数列张量
# flag = True
flag = False
if flag:
    t = torch.arange(2, 10, 2)
    print(t)

# ===============================  exmaple 6 ===============================
# 通过torch.linspace创建 均分数列张量
# flag = True
flag = False
if flag:
    # t = torch.linspace(2, 10, 5)
    t = torch.linspace(2, 10, 6)
    print(t)

# ===============================  exmaple 7 ===============================
# 通过torch.normal创建 正态分布张量
flag = True
# flag = False
if flag:

    # mean：张量 std: 张量
    # mean = torch.arange(1, 5, dtype=torch.float)
    # std = torch.arange(1, 5, dtype=torch.float)
    # t_normal = torch.normal(mean, std)
    # print("mean:{}\nstd:{}".format(mean, std))
    # print(t_normal)

    # mean：标量 std: 标量
    # mean和std都是标量还要再定义一个size
    # t_normal = torch.normal(0., 1., size=(4,))
    # print(t_normal)

    # mean：张量 std: 标量
    mean = torch.arange(1, 5, dtype=torch.float)
    std = 1
    t_normal = torch.normal(mean, std)
    print("mean:{}\nstd:{}".format(mean, std))
    print(t_normal)


# 通过torch.randn创建 均值为0 标准差为1 的 标准正态分布
    # size:张量的形状
    # t_randn = torch.randn(size=(4,))
    # print(t_randn)

# 通过torch.rand创建 在区间[0,1）上的均匀分布
    # size:张量的形状
    # t_randn = torch.rand(size=(4,))
    # print(t_randn)

# 通过torch.randint创建 在区间[low,high）上的整数均匀分布
    # mean：标量 std: 标量 size:张量的形状
    # t_randn = torch.randint(1, 6, size=(4,))
    # print(t_randn)

# 通过torch.randprem生成从0-1的随机排列
    # n:张量的长度
    # t_randn = torch.randperm(6)
    # print(t_randn)

# 通过torch.bernoulli 以input为概率，生成伯努利分布（0-1分布，两点分布）
    # input:概率
    # input = torch.ones(3,3)
    # t_randn = torch.bernoulli(input)
    # print(t_randn)




