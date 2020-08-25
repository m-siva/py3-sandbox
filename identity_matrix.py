# matrix = []
# for r_idx in range(0,3):
#     row = []
#     for c_idx in range(0,3):
#         if r_idx == c_idx:
#             row.append(1)
#         else:
#             row.append(0)
# matrix.append(row)

imx = [[1 if c_idx == r_idx else 0 for c_idx in range(0,3)] for r_idx in range(0,3)]