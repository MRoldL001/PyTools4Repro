import os
import json
import numpy as np

# === configure input and output paths ===
input_dir = '/path/to/rps_folder'
output_dir = '/path/to/output_txts'

os.makedirs(output_dir, exist_ok=True)

for fname in os.listdir(input_dir):
    if not fname.endswith('.rps'):
        continue

    rps_path = os.path.join(input_dir, fname)
    with open(rps_path, 'r') as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"读取 {fname} 失败：{e}")
            continue

    if 'environmentMap' not in data or 'coefficients' not in data['environmentMap']:
        print(f"文件 {fname} 中缺少 environmentMap，已跳过")
        continue

    coeffs = np.array(data['environmentMap']['coefficients'])
    out_path = os.path.join(output_dir, fname.replace('.rps', '.txt'))

    np.savetxt(out_path, coeffs, fmt='%.8f')
    print(f"已保存 SH 光照系数到：{out_path}")
