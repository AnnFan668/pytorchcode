import torch
import numpy as np
torch.manual_seed(1)

# ======================================= example 1 =======================================
# torch.cat 将张量按维度dim进行拼接
# tensors:张量序列 dim:拼接维度

# flag = True
flag = False
if flag:
    t = torch.ones((2, 3))

    t_0 = torch.cat([t, t], dim=0)
    t_1 = torch.cat([t, t, t], dim=1)

    print("t_0:{} shape:{}\nt_1:{} shape:{}".format(t_0, t_0.shape, t_1, t_1.shape))


# ======================================= example 2 =======================================
# torch.stack 在新创建的维度dim上进行拼接

# flag = True
flag = False
if flag:
    t = torch.ones((2, 3))

    t_stack = torch.stack([t, t, t], dim=2)

    print("\nt_stack:{} shape:{}".format(t_stack, t_stack.shape))


# ======================================= example 3 =======================================
# torch.chunk 将张量按维度dim进行平均切分

# flag = True
flag = False

if flag:
    a = torch.ones((2, 7))  # 7
    list_of_tensors = torch.chunk(a, dim=1, chunks=2)   # 3

    for idx, t in enumerate(list_of_tensors):
        print("第{}个张量：{}, shape is {}".format(idx+1, t, t.shape))


# ======================================= example 4 =======================================
# torch.split 将张量按维度dim进行切分
# split_size_or_sections : 为int时，表示每一份的长度；为list时，按list元素切分

# flag = True
flag = False

if flag:
    t = torch.ones((2, 5))

    list_of_tensors = torch.split(t, 2, dim=1)  # [2 , 1, 2]
    for idx, t in enumerate(list_of_tensors):
        print("第{}个张量：{}, shape is {}".format(idx+1, t, t.shape))

    # list_of_tensors = torch.split(t, [2, 1, 2], dim=1)
    # for idx, t in enumerate(list_of_tensors):
    #     print("第{}个张量：{}, shape is {}".format(idx, t, t.shape))


# ======================================= example 5 =======================================
# torch.index_select 在维度dim上，按index索引数据

# flag = True
flag = False

if flag:
    t = torch.randint(0, 9, size=(3, 3))
    idx = torch.tensor([0, 2], dtype=torch.long)    # index必须是long型数据
    t_select = torch.index_select(t, dim=0, index=idx)
    print("t:\n{}\nt_select:\n{}".format(t, t_select))


# ======================================= example 6 =======================================
# torch.masked_select 按mask中的True进行索引 返回值为一维张量
# mask: 与input同形状的布尔类型张量

# flag = True
flag = False

if flag:

    t = torch.randint(0, 9, size=(3, 3))
    mask = t.le(5)  # ge is mean greater than or equal/   gt: greater than  le  lt
    # ge大于等于  gt大于  le小于等于  lt小于

    t_select = torch.masked_select(t, mask)
    print("t:\n{}\nmask:\n{}\nt_select:\n{} ".format(t, mask, t_select))


# ======================================= example 7 =======================================
# torch.reshape 变换张量形状  注意：当张量在内存中是连续时，新张量与input共享数据内存
# shape: 新张量的形状

# flag = True
flag = False

if flag:
    t = torch.randperm(8)
    # t_reshape = torch.reshape(t, (2, 4))
    t_reshape = torch.reshape(t, (-1, 2, 2))
    print("t:{}\nt_reshape:\n{}".format(t, t_reshape))

    t[0] = 1024
    print("t:{}\nt_reshape:\n{}".format(t, t_reshape))
    print("t.data 内存地址:{}".format(id(t.data)))
    print("t_reshape.data 内存地址:{}".format(id(t_reshape.data)))


# ======================================= example 8 =======================================
# torch.transpose 交换张量的两个维度

# flag = True
flag = False

if flag:
    torch.transpose
    t = torch.rand((2, 3, 4))
    t_transpose = torch.transpose(t, dim0=1, dim1=2)    # c*h*w     h*w*c
    print(t)
    print(t_transpose)
    print("t shape:{}\nt_transpose shape: {}".format(t.shape, t_transpose.shape))

    # arr = np.array([[2, 3, 4], [5, 6, 7]])
    # t = torch.tensor(arr)
    # t_transpose = torch.transpose(t, dim0=0, dim1=1)
    # print(t)
    # print(t_transpose)
    # print("t shape:{}\nt_transpose shape:{}".format(t.shape, t_transpose.shape))


# ======================================= example 9 =======================================
# torch.squeeze 压缩长度为1的维度（轴）
# dim: 若为None，移除所有长度为1的轴；若指定维度，当且仅当该轴长度为1时，可以被移除

# flag = True
flag = False

if flag:
    t = torch.rand((1, 2, 3, 1))
    t_sq = torch.squeeze(t)
    t_0 = torch.squeeze(t, dim=0)
    t_1 = torch.squeeze(t, dim=1)
    print(t.shape)
    print(t_sq.shape)
    print(t_0.shape)
    print(t_1.shape)
    print(t)
    print(t_sq)

# torch.unsqueeze() 依据dim扩展维度
# dim: 扩展的维度
if flag:
    t = torch.rand((1, 2, 3, 1))
    t_0 = torch.unsqueeze(t, dim=0)
    t_1 = torch.unsqueeze(t, dim=1)
    print(t.shape)
    print(t_0.shape)
    print(t_1.shape)
    print(t)


# ======================================= example 8 =======================================
# torch.add 逐元素计算 input+alpha×other
# input: 第一个张量  alpha: 乘项因子  other: 第二个张量

flag = True
# flag = False

if flag:
    t_0 = torch.randn((3, 3))
    t_1 = torch.ones_like(t_0)
    t_add = torch.add(t_0, 10, t_1)

    print("t_0:\n{}\nt_1:\n{}\nt_add_10:\n{}".format(t_0, t_1, t_add))

